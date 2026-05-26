import streamlit as st

from agents.intent_agent import extract_intent
from agents.design_agent import generate_design

from agents.schema_agent import (
    generate_database_schema,
    generate_api_schema,
    generate_ui_schema,
    generate_auth_schema,
)

from agents.validator_agent import validate_system
from agents.runtime_agent import generate_application

st.set_page_config(page_title="AI App Compiler", layout="wide")

st.title("AI App Compiler")
st.caption("Natural Language → Structured Config → Validation → Runtime App Generation")

user_input = st.text_area(
    "Describe your application",
    height=180,
    placeholder="Example: Build a CRM with login, contacts, dashboard, role-based access, payments, and analytics."
)

demo_mode = st.checkbox("Demo Mode (use cached output, no API calls)")

generate = st.button("Generate Application")

# ---------------- DEMO MODE ----------------

if demo_mode:
    st.info("Demo Mode enabled — no API calls will be used.")

    demo_intent = {
        "app_name": "CRM",
        "app_type": "SaaS Application",
        "features": ["Login", "Contacts", "Dashboard", "Payments", "Analytics"],
        "roles": ["Admin", "User"],
        "entities": ["User", "Contact", "Payment", "Plan"],
        "monetization": "Subscription",
    }

    demo_design = {
        "pages": ["Login", "Dashboard", "Contacts", "Payments", "Analytics"],
        "modules": ["Authentication", "Contact Management", "Payment Processing", "Analytics"],
        "role_permissions": {
            "Admin": {
                "Dashboard": ["view", "edit"],
                "Contacts": ["view", "create", "edit", "delete"],
                "Analytics": ["view"],
            },
            "User": {
                "Dashboard": ["view"],
                "Contacts": ["view", "create"],
                "Payments": ["view", "pay"],
            },
        },
        "dashboards": [
            {"name": "Admin Dashboard", "access_roles": ["Admin"]},
            {"name": "User Dashboard", "access_roles": ["User"]},
        ],
    }

    demo_db_schema = {
        "tables": [
            {
                "table_name": "users",
                "columns": [
                    {"name": "id", "type": "integer"},
                    {"name": "email", "type": "string"},
                    {"name": "role", "type": "string"},
                ],
            },
            {
                "table_name": "contacts",
                "columns": [
                    {"name": "id", "type": "integer"},
                    {"name": "name", "type": "string"},
                    {"name": "email", "type": "string"},
                ],
            },
        ]
    }

    demo_api_schema = {
        "endpoints": [
            {"path": "/users", "method": "GET", "description": "Fetch users"},
            {"path": "/contacts", "method": "GET", "description": "Fetch contacts"},
            {"path": "/payments", "method": "POST", "description": "Create payment"},
        ]
    }

    demo_ui_schema = {
        "pages": [
            {"name": "Login", "components": ["Email Input", "Password Input", "Login Button"]},
            {"name": "Dashboard", "components": ["Sidebar", "Stats Cards", "Analytics Chart"]},
            {"name": "Contacts", "components": ["Contact Table", "Add Contact Button"]},
        ]
    }

    demo_auth_schema = {
        "roles": {
            "Admin": ["manage_users", "view_analytics", "manage_contacts"],
            "User": ["view_dashboard", "manage_own_contacts"],
        }
    }

    demo_validation = {
        "status": "success",
        "issues": [],
        "needs_repair": False,
    }

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Intent", "Design", "Schemas", "Validation", "Runtime"]
    )

    with tab1:
        st.json(demo_intent)

    with tab2:
        st.json(demo_design)

    with tab3:
        st.subheader("Database Schema")
        st.json(demo_db_schema)

        st.subheader("API Schema")
        st.json(demo_api_schema)

        st.subheader("UI Schema")
        st.json(demo_ui_schema)

        st.subheader("Auth Schema")
        st.json(demo_auth_schema)

    with tab4:
        st.json(demo_validation)

    with tab5:
        st.success("Demo app generated successfully.")
        st.code("generated_apps/CRM/app.py")

# ---------------- LIVE MODE ----------------

if generate:

    if not user_input.strip():
        st.warning("Please enter a valid application description.")
        st.stop()

    if user_input.strip().lower() in ["hi", "hello", "hey", "test"]:
        st.warning("Please describe an application, not just a greeting.")
        st.stop()

    try:
        with st.spinner("Generating application..."):

            intent = extract_intent(user_input)
            design = generate_design(intent)

            db_schema = generate_database_schema(intent, design)
            api_schema = generate_api_schema(intent, design)
            ui_schema = generate_ui_schema(intent, design)
            auth_schema = generate_auth_schema(intent, design)

            validation = validate_system(
                db_schema,
                api_schema,
                ui_schema,
                auth_schema,
            )

            generated = generate_application(
                intent=intent,
                app_name=intent.app_name.replace(" ", "_"),
                db_schema=db_schema,
                api_schema=api_schema,
                ui_schema=ui_schema,
                auth_schema=auth_schema,
            )

        st.success("Application generated successfully!")

        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            ["Intent", "Design", "Schemas", "Validation", "Runtime"]
        )

        with tab1:
            st.json(intent.model_dump())

        with tab2:
            st.json(design.model_dump())

        with tab3:
            st.subheader("Database Schema")
            st.json(db_schema.model_dump())

            st.subheader("API Schema")
            st.json(api_schema.model_dump())

            st.subheader("UI Schema")
            st.json(ui_schema.model_dump())

            st.subheader("Auth Schema")
            st.json(auth_schema.model_dump())

        with tab4:
            st.json(validation)

        with tab5:
            st.success(f"Generated app path: {generated['path']}")
            st.code(f"streamlit run {generated['path']}/app.py")

    except Exception as e:
        st.error("Generation failed. API quota may be exhausted or output validation failed.")
        st.code(str(e))
        