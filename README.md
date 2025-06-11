# AI Agent CLI

This project is a command-line assistant that interacts with your local development environment using Google's Gemini API. It lets you perform tasks like listing files, reading and writing file contents, and running Python scripts by typing natural language prompts.

## Features

- List files in directories  
- Read contents of files  
- Write content to files  
- Run Python scripts  
- Uses structured function calls with Gemini API  
- Restricts file operations to allowed directories  

## Setup and Usage

Clone the repository, set up the environment, install dependencies, configure your API key, and run commands all in a few steps:

```bash
git clone https://github.com/ejaz0/aiagent
cd aiagent
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
echo "GEMINI_API_KEY=your_api_key_here" > .env
python3 main.py "read the contents of main.py"
# Add --verbose if you want more details
