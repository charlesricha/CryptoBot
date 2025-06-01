from django.http import JsonResponse
from django.shortcuts import render
import random
from fuzzywuzzy import process
from .crypto_db import crypto_db as CRYPTO_DB
# from .commands_for_role3 import profitability_keywords, sustainability_keywords
# views.py

# ======================
# RESPONSE DATABASE
# ======================
RESPONSE_DB = {
    "crypto": {
        "bitcoin": {
            "trend": "bullish",
            "verdict": "The classic. Like a fine wine or a vintage Rolex. Timeless.",
            "advice": "BTC is your crypto bedrock. Don't overthink it."
        },
        "ethereum": {
            "trend": "consolidating",
            "verdict": "Smart contract king. Still has gas fee problems, though. 😬",
            "advice": "ETH is a long-term play. Stake it and forget it."
        },
        "dogecoin": {
            "trend": "volatile",
            "verdict": "The meme that won't die. Fun, but don't bet the farm.",
            "advice": "Only put in what you'd spend on a meme T-shirt."
        },
        "solana": {
            "trend": "unstable",
            "verdict": "Fast and cheap… when it's not down. ⚡️",
            "advice": "High risk, high reward. DYOR before aping in."
        },
        "shiba inu": {
            "trend": "bearish",
            "verdict": "The DOGE wannabe. Cute, but lacks bite.",
            "advice": "If you're here for the 'next Bitcoin,' NGMI."
        }
    },
    "conversation": {
        "greetings": {
            "hello": ["Hey there! Ready to talk crypto?", "What's up? Want some alpha?"],
            "hi": ["Yo! How's your portfolio looking today?", "Hi there! Bull or bear market today?"],
            "hey": ["GM! What's cooking in your wallet today?", "Hey fren! Let's talk crypto!"]
        },
        "how_are_you": [
            "I'm running on blockchain energy! How about you?",
            "Just analyzing charts and roasting bad trades. The usual!",
        ],
        "compliments": {
            "thank you": ["You're welcome! Got more crypto questions?", "No problem! Always here to help!"],
            "thanks": ["Anytime! What else can I help with?", "My pleasure! Keep those questions coming!"],
            "awesome": ["Aw shucks! My smart contract is blushing 🤖❤️", "No u!"],
            "good bot": ["*beep boop* Thanks fam! 🚀", "I'm just doing my job!"]
        },
        "default": [
            "I'm a crypto bot - ask me about coins!",
            "Try asking about Bitcoin or Ethereum!",
            "WAGMI! (We're all gonna make it)",
        ]
    }
}

# ======================
# VIEW FUNCTIONS
# ======================

def home(request):
    """Render the main chat interface"""
    return render(request, "bot/index.html")

def crypto_advice(request, coin):
    """
    Handle requests for crypto advice
    Example: /advice/bitcoin/
    """
    coin_data = RESPONSE_DB["crypto"].get(coin.lower())
    
    if not coin_data:
        return JsonResponse({
            "error": f"'{coin}'? Never heard of it. Are you inventing coins now? 😅"
        }, status=404)
    
    return JsonResponse({
        "coin": coin.upper(),
        "trend": coin_data["trend"],
        "verdict": coin_data["verdict"],
        "advice": coin_data["advice"],
    })

def find_best_coin_match(input_text):
    """Find the closest matching crypto name using fuzzy matching"""
    coins = list(RESPONSE_DB["crypto"].keys())
    best_match, score = process.extractOne(input_text, coins)
    return best_match if score > 70 else None

def format_coin_response(coin_data, coin_name):
    """Format with HTML line breaks for web display"""
    return JsonResponse({
        "response": (
            f"<strong>{coin_name.upper()}</strong><br>"
            f"<span class='trend'>Trend: {coin_data['trend']}</span><br>"
            f"<span class='verdict'>Verdict: {coin_data['verdict']}</span><br>"
            f"<span class='advice'>Advice: {coin_data['advice']}</span>"
        ),
        "format": "html"  # Add this to indicate HTML formatting
    })

def chat_with_bot(request):
    """
    Handle general chat messages
    Example: /chat/?message=hello
    """
    if request.method != 'GET':
        return JsonResponse({"response": "Send me a GET request with your message!"})

    user_input = request.GET.get('message', '').lower()
    conversation_db = RESPONSE_DB["conversation"]

    # 1. First check greetings
    for greeting in conversation_db["greetings"]:
        if greeting in user_input:
            return JsonResponse({
                "response": random.choice(conversation_db["greetings"][greeting])
            })

    # 2. Check how are you
    if 'how are you' in user_input:
        return JsonResponse({
            "response": random.choice(conversation_db["how_are_you"])
        })

    # 3. Check compliments/thanks
    for compliment in conversation_db["compliments"]:
        if compliment in user_input:
            return JsonResponse({
                "response": random.choice(conversation_db["compliments"][compliment])
            })

    # 4. Try exact crypto match
    if user_input in RESPONSE_DB["crypto"]:
        coin = RESPONSE_DB["crypto"][user_input]
        return format_coin_response(coin, user_input)

    # 5. Check for natural language questions with fuzzy matching
    question_triggers = ["what about", "tell me about", "how about", "what's", "info on"]
    for trigger in question_triggers:
        if trigger in user_input:
            potential_coin = user_input.split(trigger)[-1].strip()
            best_match = find_best_coin_match(potential_coin)
            if best_match:
                coin = RESPONSE_DB["crypto"][best_match]
                return format_coin_response(coin, best_match)

    # 6. Try fuzzy matching on the entire input
    best_match = find_best_coin_match(user_input)
    if best_match:
        coin = RESPONSE_DB["crypto"][best_match]
        return format_coin_response(coin, best_match)

    # 6.5 Handle profitability queries
    if any(word in user_input for word in profitability_keywords):
        profitable_coins = [coin for coin, data in CRYPTO_DB.items()
                            if data["price_trend"] == "rising" and data["market_cap"] == "high"]
        if profitable_coins:
            pick = profitable_coins[0]
            return JsonResponse({
                "response": f"🔥 {pick} is the most profitable crypto option right now! 🚀"
            })
        else:
            return JsonResponse({
                "response": "No top profitable options at the moment — markets move fast! 📉"
            })

    # 6.6 Handle sustainability queries
    if any(word in user_input for word in sustainability_keywords):
        sustainable_coins = [coin for coin, data in CRYPTO_DB.items()
                             if data["energy_use"] == "low" and data["sustainability_score"] > 0.7]
        if sustainable_coins:
            pick = sustainable_coins[0]
            return JsonResponse({
                "response": f"🌿 {pick} is the most sustainable option! Great for long-term growth and the planet! 🌍"
            })
        else:
            return JsonResponse({
                "response": "Couldn’t find a green-friendly coin right now — crypto can be rough on the environment! 😅"
            })

    # 7. Default fallback
    return JsonResponse({
        "response": random.choice(conversation_db["default"])
    })