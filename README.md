# ChatAGH_UI

**ChatAGH_UI** is a web-based chat application that allows users to create conversations, send messages, and interact with an assistant.
The application is built using **Django** for the backend and **JavaScript** for the frontend.

---

## Features

- ✅ User authentication (login, registration)
- ✅ Conversation management (create, view, and list conversations)
- ✅ Real-time message streaming
- ✅ Markdown support for assistant messages
- ✅ Responsive design for desktop and mobile devices

---

## Project Structure

```
ChatAGH_UI/
├── .env.example          # Environment variables
├── .gitignore            # Git ignore file
├── poetry.lock           # Poetry lock file
├── pyproject.toml        # Poetry configuration
├── web_app/              # Main Django application
│   ├── db.sqlite3        # SQLite database
│   ├── manage.py         # Django management script
│   ├── accounts/         # User authentication app
│   │   ├── apps.py       # App configuration
│   │   ├── forms.py      # User forms
│   │   ├── urls.py       # URL routing
│   │   └── views.py      # View logic
│   ├── chat/             # Chat app
│   │   ├── apps.py       # App configuration
│   │   ├── models.py     # Database models
│   │   ├── selectors.py  # Query utilities
│   │   ├── services.py   # Business logic
│   │   ├── urls.py       # URL routing
│   │   ├── views.py      # View logic
│   │   ├── migrations/   # Database migrations
│   │   │   ├── __init__.py
│   │   │   └── 0001_initial.py
│   │   ├── static/       # Static files
│   │   │   ├── css/      # CSS files
│   │   │   │   └── style.css
│   │   │   └── js/       # JavaScript files
│   │   │       └── chat.js
│   ├── static/           # Global static files
│   │   └── agh_1.jpg
│   ├── templates/        # HTML templates
│   │   ├── base.html     # Base template
│   │   ├── accounts/     # Templates for authentication
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── chat/         # Templates for chat
│   │       └── conversation.html
│   ├── web_app/          # Django project settings
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
└── README.md             # Project documentation
```

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ChatAGH/ChatAGH_UI
   cd ChatAGH_UI
   ```

2. **Download, install and activate poetry for dependency management**
   ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"
    poetry install
    poetry env activate
   ```

3. **Set up environment variables**
   - Copy the example environment file and modify it as needed:
   ```bash
   cp .env.example .env
   # Edit .env to set your environment variables

4. ***Run project***
   ```bash
   python manage.py migrate # Apply database migrations
   python manage.py runserver # Start the development server
   ```

---

## Usage

- Register a new account or log in with an existing account.
- Create a new conversation or select an existing one from the sidebar.
- Type messages in the input box and send them to interact with the assistant.

---

## Technologies Used

- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default, can be replaced with other databases)
- **Styling:** Custom CSS
- **Markdown Rendering:** Marked.js

---

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add feature"
   ```
4. Push to your fork:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

---

## License

This project is licensed under the **MIT License**.

---

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Marked.js](https://marked.js.org/)
