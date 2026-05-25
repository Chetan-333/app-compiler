from agents.intent_agent import extract_intent

user_input = """
Build a CRM with login, contacts, dashboard,
role-based access, and premium plan with payments.
Admins can see analytics.
"""

result = extract_intent(user_input)

print(result)
