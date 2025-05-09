import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
import json

def get_api_key():
    load_dotenv()  
    api_key = os.getenv("my_api")
    if api_key is None:
        raise ValueError("API key not found. Please set the 'my_api' environment variable.")
    return api_key



def response_text(api, model_name):
    client = genai.Client(api_key=api)

    cfg_settings = types.GenerateContentConfig(
                system_instruction='you are a assistant',
                max_output_tokens= 3000,
                top_k= 2,
                top_p= 0.5,
                temperature= 0.5,
                # response_mime_type= 'application/json',
                # stop_sequences= ['\n'],
                seed=42,
                safety_settings=[
                    types.SafetySetting(
                        category='HARM_CATEGORY_HATE_SPEECH',
                        threshold='BLOCK_ONLY_HIGH'
                        # block=True
                    )
                ]
            )
    # model = genai.GenerationModel(model_name)
    # chat = client.start_chat(history=[])
    history=[]
    chat = client.chats.create(model=model_name)

    while True:
        content = input("Hi feel free to..Ask me anything: ")

        response = chat.send_message(content, config=cfg_settings)

        print(f"\n{model_name}: {response.text}")

          # Append the user input and model response to the chat history list
        history.append(f"User: {content}")
        history.append(f"Model: {response.text}")

        # Optionally, save the chat history to a text file
        with open("chat_his.json", "w", encoding="utf-8") as file:
            # Write the chat history in JSON format
            json.dump(history, file, ensure_ascii=False, indent=4)


def response_text2():
    response = input("Ask anything: ")

    return response

if __name__ == "__main__":
    model_name = "gemini-2.0-flash"
    api = get_api_key()
    file_his_path = r"C:\1.PIGGEST\05_Python\01_GEMINI\chat_his.json"
    answer = response_text(api, model_name)
    print(f"\n{model_name}: {answer}")




