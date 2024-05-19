# Smart AI Medical Bot

Smart AI Medical Bot is a Streamlit-based application that allows users to chat with an AI bot specialized in providing responses to medical-related queries.

## Features

- **User-Friendly Interface:** Simple and intuitive interface for interacting with the AI bot.
- **AI-Powered Responses:** Provides intelligent and relevant responses to medical questions using Google Generative AI.
- **Real-Time Interaction:** Real-time chat interface for smooth and dynamic user experience.

## Requirements

- Python 3.7 or higher
- Streamlit
- google-generativeai
- python-dotenv

## Installation

### Clone the Repository

```bash
git clone https://github.com/saanvi1375/Medical_Chatbot.git
cd smart-ai-medical-bot
```

### Install Dependencies

Create a virtual environment and activate it:

#### On Linux or MacOS
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows use 
```bash
\`venv\\Scripts\\activate\`
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### Create a \.env\ File

Create a \.env\ file in the root directory and add your Google Generative AI API key:

```
API_KEY=your_api_key_here
```

## Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

This will start the Streamlit server and open the application in your default web browser. 

## Contributors
- Saanvi R Prabhu (https://github.com/saanvi1375)
- Kartekeya Sharma
