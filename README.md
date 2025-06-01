# 🪙 Crypto Bot

Crypto Bot is a simple Django-based chatbot that provides advice and basic information about cryptocurrency. The bot retrieves its responses from a predefined dictionary in the `views.py` file. This project is ideal for learning how to integrate logic-based responses in a Django web app.

---

## 📚 Table of Contents

- [🚀 Features](#-features)
- [📁 Project Structure](#-project-structure)
- [🛠️ Installation and Setup](#️-installation-and-setup)
- [💡 How It Works](#-how-it-works)
- [📷 Screenshots ](#-screenshots-optional)
- [📈 Future Improvements](#-future-improvements)
- [👥 Contributors](#-contributors)
- [📄 License](#-license)
- [🙋‍♂️ Author](#-author)

---

## 🚀 Features

- 🔐 Simple and beginner-friendly Django chatbot.
- 📖 Static crypto-related advice pulled from a Python dictionary.
- 🧠 Easily customizable dictionary to update or expand bot knowledge.
- 🌐 Web-based UI for interactive responses.

---

## 📁 Project Structure

```bash
crypto_bot/
│
├── crypto_bot/             # Project settings
│   ├── settings.py
│   └── urls.py
│
├── bot/                    # Main chatbot app
│   ├── views.py            # Contains the dictionary and chatbot logic
│   ├── urls.py             # URL routes for the bot
│   └── templates/          # HTML templates
│       └── bot.html        # Basic UI for user interaction
│
├── manage.py               # Django management script
└── README.md               # Project documentation

```
## 🛠️ Installation and Setup

- Clone the repository

```bash
git clone https://github.com/yourusername/crypto-bot.git
cd crypto-bot
```
- Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
- Install dependencies

```bash
pip install django
```

- Run migrations and start the server
```bash
    python manage.py migrate
    python manage.py runserver
```
- Visit the bot

```bash
Open your browser and go to http://127.0.0.1:8000/ to interact with Crypto Bot.
```
💡 How It Works

    When a user types a message into the input field, it's sent to the Django backend.

    The views.py file contains a Python dictionary that maps common crypto-related questions or keywords to predefined answers.

    The bot checks for a matching keyword or phrase and returns the appropriate response.

    If no match is found, a default message is shown.

## 📷 Screenshots

<img src="" alt="screenshot.png">

## 📈 Future Improvements

   -  Integrate an AI model or external crypto news API.

   -  Add authentication so users can save past conversations.

   - Improve UI with CSS frameworks like Tailwind or Bootstrap.

   - Add more keywords and responses for broader coverage.

## 👥 Contributors

- Thank you to all the amazing people who have contributed to this project:
  
Name	                   GitHub Profile               Contributions
Charles Muthui             <a href="https://github.com/charlesricha/">@charlesricha</a>           Project creator, core logic, design
Karen Mumbi                 <a href="https://github.com/preciusmumbi/">@charlesricha</a>          Bot Cypto data analyzer

- You can be listed here too! Feel free to fork the repo, make changes, and open a pull request.

## 📄 License

- This project is open-source and available under the MIT License.
- 
## 🙋‍♂️ Author

Crypto Bot by [Charles Muthui]
Feel free to reach out with questions or contributions.

LET's Connect:
LinkedIn - <a href="[https://www.linkedin.com/in//muthui-charles](https://www.linkedin.com/in//muthui-charles)"></a>


