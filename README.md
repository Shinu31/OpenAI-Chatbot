# ChatGPT Lite#

ChatGPT Lite is a simple and user-friendly chatbot interface built using Streamlit and OpenAI's API. This project aims to provide a conversational AI assistant that can interact with users in a natural and engaging manner.

# Features

- **Interactive Chat Interface**: A streamlined and intuitive chat interface powered by Streamlit.
- **OpenAI Integration**: Utilizes OpenAI's API to generate human-like responses.
- **Session Management**: Maintains chat history and session state for a seamless user experience.

## Requirements

- Python 3.7 or higher
- Streamlit
- OpenAI Python Client
- Python-dotenv

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/chatgpt-lite.git
    cd chatgpt-lite
    ```

2. Install the required packages:
    ```sh
    pip install streamlit openai python-dotenv
    ```

3. Create a `.env` file in the project directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

2. Open your browser and go to `http://localhost:8501` to start chatting with ChatGPT Lite.

## Code Overview

### `Chatbot_OpenAi.py`

 **Importing Libraries**:
    - `OpenAI`: Library for interfacing with OpenAI's API.
    - `os`: Standard library for interacting with the operating system.
    - `streamlit as st`: Streamlit library for creating web apps.
    - `dotenv`: Library for loading environment variables from a `.env` file.

 **Loading Environment Variables**:
    - `load_dotenv()`: This loads environment variables from a `.env` file.
    - `os.getenv("OPENAI_API_KEY")`: Retrieves the OpenAI API key from the environment variables.

- **Setting Up Streamlit Interface**:
    - Displaying a title and subtitle using `st.markdown`.

- **Initializing OpenAI Client**:
    - `client = OpenAI(api_key=OPENAI_API_KEY)`: Initializes the OpenAI client with the API key.

- **Maintaining Session State**:
    - Checking and initializing `openai_model` and `messages` in the session state.

- **Displaying Chat Messages**:
    - Iterating through `st.session_state.messages` to display each message using `st.chat_message`.

- **Handling User Input**:
    - If a user input (`prompt`) is received, it's added to `st.session_state.messages`.
    - Displays the user input message.
    - Generates a response using OpenAI's API (`client.chat.completions.create`).
    - Displays the assistant's response and adds it to `st.session_state.messages`.


