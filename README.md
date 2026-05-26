# AI App Compiler

An AI-powered multi-stage software generation system that converts natural language application requirements into structured schemas, validated configurations, and executable runtime applications.

This project was built as a systems-engineering-focused AI application compiler inspired by platforms like Base44.

---

# Overview

The system behaves like a compiler for software generation:

Natural Language Prompt
→ Intent Extraction
→ System Design
→ Schema Generation
→ Validation
→ Repair Layer
→ Runtime Generation
→ Executable Application

Unlike single-prompt AI generators, this system uses a modular multi-stage pipeline with strict schema enforcement, validation, and targeted repair mechanisms.

---

# Features

## Multi-Stage Generation Pipeline

* Intent Extraction Agent
* Design Agent
* Schema Generation Layer
* Validation Engine
* Repair System
* Runtime Generator

## Structured Schema Generation

The system generates:

* UI Schema
* API Schema
* Database Schema
* Authentication Schema

## Validation + Repair Engine

The system validates:

* Missing fields
* Invalid structures
* Schema mismatches
* API/Database inconsistencies
* Logical issues

If validation fails:

* only the affected layer is regenerated
* full pipeline reruns are avoided

## Runtime Generation

Generated schemas are converted into runnable Streamlit applications automatically.

The system produces:

* executable `app.py`
* generated runtime UI
* forms
* tables
* buttons
* charts
* game grids

## Cached Execution Mode

To reduce API costs and avoid free-tier quota exhaustion, the system supports a cached execution mode for reliable demonstrations and testing.

## Evaluation Framework

Includes:

* 10 normal product prompts
* 10 edge-case prompts
* evaluation metrics
* repair tracking
* latency tracking

---

# Architecture

User Prompt
↓
Intent Agent
↓
Design Agent
↓
Schema Generation
↓
Validation Engine
↓
Repair Layer
↓
Runtime Generator
↓
Executable Streamlit App

---

# Tech Stack

* Python
* Streamlit
* LangChain
* Gemini API
* Pydantic
* LangGraph
* JSON-based schema generation

---

# Project Structure

```bash
project/
│
├── app.py
├── main.py
├── requirements.txt
│
├── agents/
│   ├── intent_agent.py
│   ├── design_agent.py
│   ├── schema_agent.py
│   ├── validator_agent.py
│   ├── repair_agent.py
│   └── runtime_agent.py
│
├── runtime/
│   ├── generate_streamlit_app.py
│   └── file_writer.py
│
├── evaluation/
│   ├── test_prompts.json
│   ├── results.json
│   └── metrics.md
│
├── generated_apps/
│
└── README.md
```

---

# Running Locally

## 1. Clone Repository

```bash
git clone <your_repo_url>
cd app-compiler
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Add API Key

Create `.env`

```env
GOOGLE_API_KEY=your_api_key_here
```

## 5. Run Application

```bash
streamlit run app.py
```

---

# Runtime Execution

Generated applications can be executed directly.

Example:

```bash
streamlit run generated_apps/CRM/app.py
```

---

# Evaluation Metrics

## Metrics Tracked

* Validation Success Rate
* Repair Attempts
* Runtime Generation Success
* Average Latency
* Failure Types

## Example Results

```json
{
  "total_tests": 20,
  "successful_generations": 17,
  "validation_failures": 3,
  "repair_attempts": 3,
  "successful_repairs": 2,
  "repair_success_rate": "66%",
  "average_latency_seconds": 4.2,
  "runtime_generation_success_rate": "85%"
}
```

---

# Failure Handling

The system handles:

* vague prompts
* incomplete prompts
* conflicting requirements
* schema mismatches
* invalid outputs

The repair layer regenerates only affected components instead of rerunning the entire pipeline.

---

# Tradeoffs

## Quality vs Cost

The system uses modular generation and cached execution mode to reduce API costs and improve stability.

## Reliability vs Latency

Validation and repair stages increase reliability while slightly increasing generation latency.

---

# Future Improvements

* Full React frontend generation
* Dockerized deployment
* Persistent memory/thread system
* LangSmith tracing integration
* Advanced schema repair
* Multi-agent orchestration improvements
* Production-grade backend generation

---

# Live Demo

https://app-compiler.streamlit.app/

---

# Author

Chetan Mittal
