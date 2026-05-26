def repair_api_schema(issues, intent, design, api_schema):
    """
    Repairs only API schema based on validation issues
    """

    repaired_endpoints = api_schema.endpoints.copy()

    for issue in issues:

        if "API endpoint" in issue and "no matching database table" in issue:

            # extract endpoint path
            endpoint_path = issue.split("'")[1]

            # simple heuristic repair: map to closest entity/table
            for entity in intent.entities:

                if entity.lower() in endpoint_path.lower():

                    repaired_endpoints.append({
                        "path": f"/{entity.lower()}",
                        "method": "GET",
                        "description": f"Auto-repaired endpoint for {entity}"
                    })

    return {"endpoints": repaired_endpoints}