## Importing libraries and files
from crewai import Task

from agents import financial_analyst, verifier
from tools import FinancialDocumentTool


# ===============================
# Primary Financial Analysis Task
# ===============================
analyze_financial_document = Task(
    description=(
        "Analyze the uploaded financial document and respond to the user query: {query}.\n"
        "You must base your analysis strictly on the document content.\n"
        "Do not fabricate data or create fictional sources.\n"
        "If information is missing, clearly state the limitation.\n"
        "Focus on clarity, factual accuracy, and financial relevance."
    ),

    expected_output=(
        "A structured financial analysis including:\n"
        "1. Summary of the financial document\n"
        "2. Key financial insights (revenue, profitability, trends if available)\n"
        "3. Potential risks mentioned in the document\n"
        "4. Data-driven insights aligned with the user's query\n"
        "5. A short disclaimer that this is AI-generated analysis, not financial advice"
    ),

    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)


# ===============================
# Investment Analysis Task
# ===============================
investment_analysis = Task(
    description=(
        "Review the financial document and provide balanced investment insights.\n"
        "Base your reasoning only on the financial data provided.\n"
        "Avoid speculation, hype, or product promotion.\n"
        "If the document lacks sufficient data, explicitly mention it."
    ),

    expected_output=(
        "Investment insights including:\n"
        "- Key strengths from the financial data\n"
        "- Potential concerns or limitations\n"
        "- Neutral, data-driven investment interpretation\n"
        "- Clear statement that this is not financial advice"
    ),

    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)


# ===============================
# Risk Assessment Task
# ===============================
risk_assessment = Task(
    description=(
        "Evaluate potential financial risks based strictly on the document content.\n"
        "Identify risks such as declining revenue, liabilities, volatility, or uncertainties.\n"
        "Do not exaggerate or invent risks.\n"
        "Clearly differentiate between explicit risks and inferred risks."
    ),

    expected_output=(
        "A structured risk analysis including:\n"
        "- Explicit risks mentioned in the document\n"
        "- Potential inferred risks (if clearly supported)\n"
        "- Overall risk outlook\n"
        "- Confidence level of the assessment"
    ),

    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)


# ===============================
# Document Verification Task
# ===============================
verification = Task(
    description=(
        "Verify whether the uploaded file appears to be a financial document.\n"
        "Base your verification on document structure, terminology, and context.\n"
        "If unsure, explain why instead of making assumptions."
    ),

    expected_output=(
        "Verification output including:\n"
        "- Whether the document appears financial or not\n"
        "- Reasoning based on document characteristics\n"
        "- Confidence level (High / Medium / Low)"
    ),

    agent=verifier,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False
)