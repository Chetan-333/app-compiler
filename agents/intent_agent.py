import json
from schemas.intent_schema import IntentSchema
from utils.llm import generate_response


def extract_intent(user_input: str):

    prompt = f"""
You are an AI Intent Extraction System.

Extract structured app requirements from the user's request.

User Request:
{user_input}

Return ONLY valid JSON in this format:

{{
    "app_name": "",
    "app_type": "",
    "features": [],
    "roles": [],
    "entities": [],
    "monetization": ""
}}
"""

    response = generate_response(prompt)

    cleaned_response = response.strip().replace("```json", "").replace("```", "")

    parsed_json = json.loads(cleaned_response)

    validated_data = IntentSchema(**parsed_json)

    return validated_data
