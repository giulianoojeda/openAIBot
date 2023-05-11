# Asistente de Pedidos de Lomiteria Arabe

This project is a simple chatbot for an Arabic Lomito restaurant that helps customers place their orders. The chatbot is built using OpenAI's GPT-3.5-turbo and Gradio for the user interface. The chatbot speaks Spanish and Portuguese, and it follows a friendly, conversational style. It can handle orders, delivery details, and payment methods while keeping track of the conversation history.

## Setup

1. Clone this repository:

```
git clone <repository_url>
cd <repository_name>
```

2. Create a virtual environment and activate it:

- On Linux/macOS:

  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

- On Windows:

  ```
  python -m venv venv
  venv\Scripts\activate
  ```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Create a `.env` file in the project's root directory with your OpenAI API key:

```
API_KEY=your_openai_api_key
```

Replace `your_openai_api_key` with your actual OpenAI API key.

5. Add the `.env` file to your `.gitignore` file to avoid exposing your API key:

```
.env
```

6. Run the chatbot:

```
python app.py
```

This will launch the Gradio interface in your web browser, where you can interact with the chatbot.

## Usage

When the chatbot interface is open in your browser, you can start placing your order by typing your request in the input box. The chatbot will guide you through the ordering process, asking for necessary details such as delivery address and payment method.

Enjoy ordering your Lomito Arabe with this simple and friendly chatbot!
