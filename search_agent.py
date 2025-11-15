from google import genai
from google.genai import types

INSTRUCTIONS = (
    "You are a research assistant. Given a search term, you search the web for that term and "
    "produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300 "
    "words. Capture the main points. Write succintly, no need to have complete sentences or good "
    "grammar. This will be consumed by someone synthesizing a report, so its vital you capture the "
    "essence and ignore any fluff. Do not include any additional commentary other than the summary itself."
)

search_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    system_instruction=INSTRUCTIONS,
    max_output_tokens=500,
    tools=[search_tool]
)

def search_agent(query: str):
    client = genai.Client()

    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=query,
        config=config,
    )
    return response.text
    


