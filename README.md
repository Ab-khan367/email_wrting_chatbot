# 🚀 AI-Powered Cold Email Generator

> Automate your job application outreach with intelligent, personalized cold emails powered by Google Gemini AI

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/🦜_LangChain-Powered-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

**Cold Email Generator** is an intelligent API that automatically extracts job postings from career pages and generates personalized, professional cold emails tailored to each position. Using advanced AI (Google Gemini) and natural language processing, it analyzes job requirements and matches them with your portfolio to create compelling outreach emails.

Perfect for:
- 💼 Job seekers applying to multiple positions
- 🎯 Recruiters reaching out to candidates
- 🚀 Business developers pitching services
- 📧 Anyone needing personalized email outreach at scale

---

## ✨ Features

- 🤖 **AI-Powered Extraction**: Automatically scrapes and extracts job details from any career page URL
- 📝 **Smart Email Generation**: Creates personalized cold emails using Google Gemini 2.5 Flash
- 🎨 **Customizable Tone**: Professional, Casual, Enthusiastic, or your custom tone
- 🔗 **Portfolio Integration**: Automatically matches job requirements with relevant portfolio links
- 💾 **Vector Database**: Uses ChromaDB for intelligent skill-based portfolio retrieval
- 🌐 **RESTful API**: Easy-to-integrate FastAPI backend
- ⚡ **Fast & Efficient**: Processes multiple job postings in seconds
- 🔒 **Secure**: Environment-based configuration for API keys

---

## 🎥 Demo

```bash
# Example Request
POST /generate-emails
{
  "url": "https://example.com/careers",
  "sender": {
    "name": "Muhammad Abdullah",
    "role": "Full Stack Developer"
  },
  "company_details": "TechCorp Solutions - Leading AI/ML consultancy",
  "tone": "Professional"
}

# Example Response
{
  "emails": [
    "Subject: Full Stack Developer Position at Your Company\n\nDear Hiring Manager,\n\n..."
  ]
}
```

---

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **Python 3.11+** - Core programming language
- **LangChain** - Framework for developing LLM applications
- **Google Gemini 2.5 Flash** - Advanced AI model for text generation

### AI & ML
- **LangChain Community** - Document loaders and utilities
- **HuggingFace Embeddings** - Semantic search capabilities
- **ChromaDB** - Vector database for portfolio storage
- **Sentence Transformers** - Text embedding models

### Data Processing
- **BeautifulSoup4** - Web scraping and HTML parsing
- **Pandas** - Data manipulation and analysis
- **lxml** - XML/HTML processing

### Deployment
- **Uvicorn** - ASGI server
- **Python-dotenv** - Environment variable management

---

## 📦 Installation

### Prerequisites
- Python 3.11 or higher
- pip package manager
- Google AI API key ([Get it here](https://makersuite.google.com/app/apikey))

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/cold-email-generator.git
cd cold-email-generator
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv genai-env
genai-env\Scripts\activate

# Linux/Mac
python3 -m venv genai-env
source genai-env/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
```bash
# Copy the example env file
cp .env.example .env

# Edit .env and add your API keys
GOOGLE_API_KEY=your_google_api_key_here
GROQ_API_KEY=your_groq_api_key_here  # Optional
```

### Step 5: Run the Application
```bash
uvicorn app.backend.main:app --reload
```

🎉 Your API is now running at `http://localhost:8000`

---

## 🎯 Usage

### Basic Example

```python
import requests

url = "http://localhost:8000/generate-emails"

payload = {
    "url": "https://careers.google.com/jobs/results/",
    "sender": {
        "name": "John Doe",
        "role": "Software Engineer"
    },
    "company_details": "ABC Tech - Innovative software solutions provider",
    "tone": "Professional"
}

response = requests.post(url, json=payload)
emails = response.json()["emails"]

for email in emails:
    print(email)
    print("\n" + "="*50 + "\n")
```

### Using cURL

```bash
curl -X POST "http://localhost:8000/generate-emails" \
     -H "Content-Type: application/json" \
     -d '{
       "url": "https://example.com/careers",
       "sender": {
         "name": "Your Name",
         "role": "Your Role"
       },
       "company_details": "Your Company",
       "tone": "Professional"
     }'
```

---

## 📚 API Documentation

### Endpoint: `POST /generate-emails`

#### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `url` | string | ✅ | URL of the job posting or careers page |
| `sender` | object | ✅ | Sender information |
| `sender.name` | string | ✅ | Your name |
| `sender.role` | string | ✅ | Your professional role |
| `company_details` | string | ✅ | Your company description |
| `tone` | string | ❌ | Email tone (default: "Professional") |

#### Response

```json
{
  "emails": [
    "Generated email content here..."
  ],
  "error": "Error message if any" // Optional
}
```

#### Status Codes

- `200 OK` - Successfully generated emails
- `400 Bad Request` - Failed to load webpage
- `500 Internal Server Error` - Server error

### Interactive API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 📁 Project Structure

```
cold-email-generator/
│
├── app/
│   ├── __init__.py
│   ├── backend/
│   │   ├── __init__.py
│   │   ├── main.py           # FastAPI application
│   │   ├── chains.py          # LangChain logic
│   │   ├── portfolio.py       # Portfolio management
│   │   └── utils.py           # Utility functions
│   └── frontend/
│       └── streamlit_app.py   # Streamlit UI (optional)
│
├── resource/
│   └── my_portfolio.csv       # Your portfolio data
│
├── vectorstore/               # ChromaDB storage (auto-generated)
│
├── .env.example               # Example environment variables
├── .gitignore                 # Git ignore rules
├── .dockerignore              # Docker ignore rules
├── Procfile                   # Deployment configuration
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

---

## ⚙️ Configuration

### Portfolio Setup

Create or edit `resource/my_portfolio.csv`:

```csv
Techstack,Links
"React, Node.js, MongoDB","https://github.com/yourusername/ecommerce-app"
"Python, FastAPI, PostgreSQL","https://github.com/yourusername/api-project"
"Machine Learning, TensorFlow","https://github.com/yourusername/ml-model"
```

### Supported Tones

- `Professional` (default)
- `Casual`
- `Enthusiastic`
- `Formal`
- Custom (specify your own)

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Google Gemini API key | ✅ |
| `GROQ_API_KEY` | Groq API key (optional) | ❌ |

---

## 🚀 Deployment

### Deploy to Render

1. Push your code to GitHub
2. Go to [Render](https://render.com)
3. Create new Web Service
4. Connect your repository
5. Set build command: `pip install -r requirements.txt`
6. Set start command: `uvicorn app.backend.main:app --host 0.0.0.0 --port $PORT`
7. Add environment variables
8. Deploy! 🎉

### Deploy to Fly.io

```bash
# Install Fly CLI
curl -L https://fly.io/install.sh | sh

# Login and deploy
fly auth login
fly launch
fly deploy
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🔨 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🎉 Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Add tests for new features
- Update documentation as needed
- Keep commits atomic and descriptive

---

## 🐛 Bug Reports

Found a bug? Please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment details

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Muhammad Abdullah**

- GitHub: [@yourusername](https://github.com/Ab-khan367)
- LinkedIn: [Your LinkedIn]([https://linkedin.com/in/yourprofile](https://www.linkedin.com/in/muhammad-abdullah-ba79b9325?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3Besx5wxt4SnaGkojfjGtL4Q%3D%3D))
- Email: mabdulpanialvi@gmail.com

---

## 🙏 Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain) for the amazing framework
- [FastAPI](https://fastapi.tiangolo.com/) for the excellent web framework
- [Google AI](https://ai.google.dev/) for Gemini API
- All contributors and users of this project

---

## ⭐ Star History

If you find this project useful, please consider giving it a star! ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/cold-email-generator&type=Date)](https://star-history.com/#yourusername/cold-email-generator&Date)

---

<div align="center">

### 💡 Built with passion using AI & Python

**[⬆ back to top](#-ai-powered-cold-email-generator)**

Made with ❤️ by [Muhammad Abdullah](https://github.com/yourusername)

</div>
