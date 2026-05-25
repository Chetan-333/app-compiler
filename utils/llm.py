from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()
model =ChatGoogleGenerativeAI(model ="gemini-2.5-flash" )

def generate_response(prompt):
    response = model.invoke(prompt)
    return response.text