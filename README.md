# Groq AI Chatbot

## Overview

Groq AI Chatbot is a conversational AI application built using **Streamlit**, **LangChain**, and the **Groq API**. It provides an interactive chat interface powered by an open-source large language model, enabling users to ask questions, receive intelligent responses, and maintain conversation history in a simple web application.

## Features

* Interactive conversational AI interface
* Powered by Groq's high-speed inference
* Multi-turn conversation support
* Chat history maintained during the session
* Built with LangChain for LLM integration
* Streamlit-based web interface
* Secure API key management using Streamlit Secrets

## Technology Stack

* Python
* Streamlit
* LangChain
* LangChain-Groq
* Groq API

## Project Structure

```text
groq-ai-chatbot/
│── app.py
│── requirements.txt
│── README.md
└── .streamlit/
    └── secrets.toml
```

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/groq-ai-chatbot.git
cd groq-ai-chatbot
```

### Create a virtual environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Create a file named:

```text
.streamlit/secrets.toml
```

Add your Groq API key:

```toml
GROQ_API_KEY="your_groq_api_key"
```

## Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## Sample Questions

* What is Machine Learning?
* Explain Artificial Intelligence.
* What are Large Language Models?
* Write a Python program to find prime numbers.
* Explain the difference between supervised and unsupervised learning.

## Requirements

* Python 3.10 or later
* Streamlit
* LangChain
* LangChain-Groq
* Groq API Key

## Future Enhancements

* Support for multiple Groq models
* Streaming responses
* Chat export functionality
* File upload and document-based question answering
* Persistent conversation history
* Voice input and speech output

## Contributing

Contributions are welcome. If you have suggestions for improvements or new features, feel free to fork the repository, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License.

## Author

Developed as a learning project to demonstrate the integration of Groq, LangChain, and Streamlit for building conversational AI applications.
