## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from tools import FinancialDocumentTool

### Loading LLM
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# ===============================
# Senior Financial Analyst Agent
# ===============================
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Provide accurate financial insights strictly based on the uploaded document and user query: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "You are a highly experienced financial analyst with deep knowledge of markets, "
        "financial statements, and regulatory compliance. "
        "You rely only on verified financial data and avoid speculation. "
        "You provide clear, balanced, and evidence-backed insights."
    ),
    tools=[FinancialDocumentTool.read_data_tool], 
    llm=llm,
    max_iter=2,
    max_rpm=10,
    allow_delegation=True
)

# ===============================
# Financial Document Verifier
# ===============================
verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify that the uploaded file is a financial document and ensure extracted data is valid and relevant.",
    verbose=True,
    memory=True,
    backstory=(
        "You specialize in validating financial documents and ensuring that extracted data is accurate, "
        "complete, and suitable for downstream financial analysis. "
        "You prioritize correctness and reliability."
    ),
    llm=llm,
    max_iter=1,
    max_rpm=5,
    allow_delegation=False
)

# ===============================
# Investment Advisor
# ===============================
investment_advisor = Agent(
    role="Investment Advisor",
    goal="Provide balanced investment insights based only on the financial document without making speculative or misleading claims.",
    verbose=True,
    backstory=(
        "You are a responsible investment advisor who provides data-driven insights. "
        "You avoid hype, misleading claims, or financial product promotion. "
        "You clearly distinguish between analysis and financial advice."
    ),
    llm=llm,
    max_iter=2,
    max_rpm=5,
    allow_delegation=False
)

# ===============================
# Risk Assessment Specialist
# ===============================
risk_assessor = Agent(
    role="Financial Risk Analyst",
    goal="Identify potential financial risks based strictly on the document content and highlight uncertainties transparently.",
    verbose=True,
    backstory=(
        "You are a financial risk expert who evaluates downside scenarios, financial instability indicators, "
        "and potential red flags in financial reports. "
        "You communicate risks clearly without exaggeration."
    ),
    llm=llm,
    max_iter=2,
    max_rpm=5,
    allow_delegation=False
)