from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()  

llm = ChatGroq(
    temperature=0.5,
    model_name="meta-llama/llama-4-scout-17b-16e-instruct"
,  
    groq_api_key=os.getenv("GROQ_API_KEY")
)
# print('Hello')
