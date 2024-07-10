
# Project Name

## Overview
This project demonstrates how to use LangGraph and LangSmith with Python. It includes setup instructions for different operating systems and a sample script `langgraph_lesson1.py`.

## Prerequisites
- Python 3.x
- pip (Python package installer)
- Git

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/winkotun007/langGraph_chatbot.git
cd langGraph_chatbot
```

### 2. Create a `.env` File
Create a file named `.env` in the root of your project directory and add the following keys:

```
ANTHROPIC_API_KEY=sk--test--key
LANGCHAIN_API_KEY=langsmithkey
LANGCHAIN_TRACING_V2=true
```

### 3. Set Up a Virtual Environment

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Requirements
Make sure your virtual environment is activated, then run:

#### Windows
```bash
pip install -r requirements.txt
```

#### macOS / Linux
```bash
pip3 install -r requirements.txt
```

### 5. Run the Script

#### Windows
```bash
python langgraph_lesson1.py
```

#### macOS / Linux
```bash
python3 langgraph_lesson1.py
```
