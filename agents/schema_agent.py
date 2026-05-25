prompt = f"""
You are a Schema Generation Agent.

Generate:
1. Database schema
2. API schema
3. UI schema
4. Auth schema

Architecture:
{design_data}

Return ONLY structured JSON.
"""