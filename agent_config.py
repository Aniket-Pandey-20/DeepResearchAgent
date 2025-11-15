from agents import OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os;

load_dotenv()

gemini_client = AsyncOpenAI(base_url=os.environ['GEMINI_BASE_URL'], api_key=os.environ['GEMINI_API_KEY'])
gemini_model = OpenAIChatCompletionsModel(model=os.environ['GEMINI_MODEL_NAME'], openai_client=gemini_client)