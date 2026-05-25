prompt = f"""
You are a Software Architecture Agent.

Using the following intent data, design the application architecture.

Intent:
{intent_data}

Generate:
- pages
- navigation flow
- modules
- role permissions
- dashboards
- feature grouping

Return ONLY structured JSON.
"""