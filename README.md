# Bell-Bot 🤖

A modern, real-time chatbot built with Django and Ollama, featuring a sleek UI with streaming responses.

## Features ✨

- Real-time response streaming using Server-Sent Events (SSE)
- Modern, responsive UI with glass-morphism design
- Powered by Gemma 2B model through Ollama
- Cross-platform compatibility (requires WSL for Windows)
- Interactive chat interface with typing indicators
- Mobile-responsive design

## Tech Stack 🛠️

- **Backend**: Django 5.2
- **Frontend**: HTML, JavaScript, TailwindCSS
- **AI Model**: Gemma 2B via Ollama
- **Styling**: 
  - Tailwind CSS
  - Phosphor Icons
  - Animate.css
  - Custom glass-morphism effects

## Prerequisites 📋

- Python 3.x
- Django 5.2+
- WSL (Windows Subsystem for Linux) - for Windows users
- Ollama with Gemma 2B model installed

## Installation 🚀

1. Clone the repository:
```bash
git clone <repository-url>
cd Bell-Bot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Unix/Linux
# OR
venv\Scripts\activate  # For Windows
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Install Ollama and the Gemma 2B model (in WSL for Windows users):
```bash
# In WSL:
curl -fsSL https://ollama.com/install.sh | sh
ollama pull gemma:2b
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

7. Visit `http://localhost:8000` in your browser

## Usage 💬

1. Open the application in your web browser
2. Type your message in the input field
3. Press Enter or click the send button to start the conversation
4. Watch as the AI responds in real-time with streaming text

## Project Structure 📁

```
Bell-Bot/
├── chat/                   # Main chat application
│   ├── templates/         # HTML templates
│   ├── views.py          # View controllers
│   └── urls.py           # URL routing
├── chatbot_project/       # Django project settings
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

## Development 🔧

- The chat interface is built with modern web technologies and features a responsive design
- Real-time responses are implemented using Server-Sent Events
- The backend communicates with Ollama through WSL (for Windows users)
- Custom styling includes glass-morphism effects and smooth animations

## License 📄

[Add your license information here]

## Contributing 🤝

[Add contribution guidelines here]

## Support 🆘

[Add support information here]