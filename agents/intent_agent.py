from utils.llm import generate_response


def extract_intent(user_input: str):

    prompt = f"""
    Extract structured app requirements from the following request.

    User Request:
    {user_input}

    Return:
    - app_name
    - app_type
    - features
    - roles
    - entities
    """

    response = generate_response(prompt)

    return response