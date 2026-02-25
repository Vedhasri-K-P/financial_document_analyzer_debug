# 🧠 Financial Document Analyzer — Debugged Submission

## 📌 GenAI Internship Debug Challenge

This repository contains a **fully debugged and stabilized version** of a CrewAI-based Financial Document Analyzer.

The original project contained multiple runtime issues, unsafe prompts, and broken dependencies.
This submission focuses on **systematic debugging, safety alignment, and production-style stabilization** to make the system reliable and maintainable.

---

## ✅ Assignment Objectives Completed

✔ Fixed deterministic runtime errors
✔ Stabilized CrewAI compatibility
✔ Removed unsafe / hallucination-prone prompts
✔ Repaired broken dependency graph
✔ Delivered working FastAPI + CrewAI pipeline

---

## 🧰 Tech Stack

* **FastAPI** — Backend API
* **CrewAI** — Agent orchestration
* **LangChain OpenAI** — LLM integration
* **PyPDF** — Document parsing
* **Python-dotenv** — Secure environment config

---

## 🐛 Key Bugs Identified & Fixes

### 1️⃣ CrewAI Import Compatibility

**Issue:**
`from crewai.agents import Agent` failed due to newer CrewAI versions.

**Fix:**

```python
from crewai import Agent
```

Ensured compatibility with latest CrewAI API.

---

### 2️⃣ Broken External Dependency

**Issue:**
Project depended on `crewai_tools` (SerperDevTool), causing runtime failures.

**Fix:**
Removed the unused dependency because:

* It wasn’t used in the execution path
* It blocked server startup
* It added instability

---

### 3️⃣ Unsafe Prompt Engineering

**Issue:**
Original prompts encouraged:

* Hallucinated financial advice
* Fake URLs and data
* Contradictory outputs

**Fix:**
Rewrote prompts to enforce:

* Document-grounded reasoning
* Financial safety
* Structured outputs
* Clear disclaimers

---

### 4️⃣ Invalid Tool Implementations

**Issues:**

* Async misuse in CrewAI tools
* Undefined PDF loader
* No error handling

**Fixes:**

* Converted tools to synchronous format
* Replaced loaders with `PdfReader`
* Added safe error handling

---

### 5️⃣ File Input Propagation Bug

**Issue:**
Uploaded PDF path wasn’t passed into Crew inputs.

**Fix:**

```python
crew.kickoff({"query": query, "file_path": file_path})
```

Enabled full end-to-end analysis.

---

### 6️⃣ Import Graph Stabilization

Removed dangling imports after dependency cleanup.

---

## 🧠 Improvements Beyond Debugging

### ✅ Prompt Safety Alignment

* Removed hallucination triggers
* Enforced grounded responses
* Added financial disclaimers

### ✅ Dependency Stabilization

* Removed fragile tools
* Reduced runtime failure surface

### ✅ Improved Error Handling

* Safer PDF parsing
* Better API responses
* Graceful failure modes

---

## 🚀 How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd financial_document_analyzer_debug
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key
```

---

### 5️⃣ Run Server

```bash
uvicorn main:app --reload
```

---

### 6️⃣ Access API

* Health Check → http://127.0.0.1:8000
* Swagger UI → http://127.0.0.1:8000/docs

---

## 🧪 Testing

### API Running Successfully

![Swagger UI](assets/swagger-ui.png)

> Swagger UI showing working FastAPI endpoints

---

## ⚠️ Note on OpenAI Quota

During testing, the system returned:

**HTTP 429 — insufficient_quota**

This confirms:

* End-to-end pipeline works
* LLM integration is correct

The limitation is billing-related, not functional.

---

## 📡 API Documentation

### Base URL

```
http://127.0.0.1:8000
```

---

### 1️⃣ Health Check

**GET /**
Returns server status.

**Response**

```json
{
  "message": "Financial Document Analyzer API is running"
}
```

---

### 2️⃣ Analyze Financial Document

**POST /analyze**

Upload a financial PDF and receive AI-powered insights.

**Form Data**

* `file` → Financial document (PDF)
* `query` *(optional)* → Custom analysis prompt

---

### Swagger Docs

Interactive API docs available at:

```
http://127.0.0.1:8000/docs
```

---

## 🧱 System Architecture

```
FastAPI → CrewAI Agents → Tools → LLM → JSON Response
```

### Flow:

1. User uploads financial document
2. PDF parsed via custom tool
3. CrewAI agents analyze content
4. LLM generates insights
5. API returns JSON response

---

## 🚀 Future Improvements

* Database integration for result storage
* Async workers (Celery/Redis)
* Result caching
* Observability & logging

---

## 🏁 Final Result

The system now provides:

* Stable backend execution
* Safe LLM outputs
* Deterministic behavior
* Production-quality debugging

---

## 🙌 Closing Note

This assignment was approached as a **real-world GenAI debugging exercise**, focusing on:

* Reliability
* Safety
* Maintainability
* Practical engineering decisions

Thank you for the opportunity!
