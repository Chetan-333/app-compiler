prompt = f"""
You are a Validation Agent.

Check:
- missing entities
- invalid API references
- missing role permissions
- inconsistent premium gating

Schemas:
{schema_data}

Return:
- validation_status
- issues
- fixes
"""