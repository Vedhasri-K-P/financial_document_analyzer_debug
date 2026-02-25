## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai.tools import tool
#from crewai_tools.tools.serper_dev_tool import SerperDevTool
from pypdf import PdfReader   # ✅ FIXED: correct PDF reader

## Creating search tool
#search_tool = SerperDevTool()

## Creating custom pdf reader tool
class FinancialDocumentTool:
    
    @tool("read_financial_document")
    def read_data_tool(path: str = 'data/sample.pdf') -> str:
        """Tool to read data from a pdf file from a path"""
        try:
            reader = PdfReader(path)   # ✅ FIXED
            full_report = ""

            for page in reader.pages:
                content = page.extract_text() or ""

                # Clean formatting
                while "\n\n" in content:
                    content = content.replace("\n\n", "\n")

                full_report += content + "\n"

            return full_report.strip()

        except Exception as e:
            return f"Error reading PDF: {str(e)}"


## Creating Investment Analysis Tool
class InvestmentTool:

    @tool("investment_analysis")
    def analyze_investment_tool(financial_document_data: str) -> str:
        """Basic investment analysis from financial text"""

        processed_data = financial_document_data

        # Clean double spaces
        while "  " in processed_data:
            processed_data = processed_data.replace("  ", " ")

        # Placeholder logic (but safe)
        return (
            "Basic Investment Insight:\n"
            "Document processed successfully. "
            "Further LLM-based investment analysis can be added."
        )


## Creating Risk Assessment Tool
class RiskTool:

    @tool("risk_assessment")
    def create_risk_assessment_tool(financial_document_data: str) -> str:
        """Basic risk extraction placeholder"""

        if not financial_document_data:
            return "No financial data provided for risk analysis."

        return (
            "Risk Assessment Summary:\n"
            "No automated risks detected yet. "
            "LLM-based risk extraction can be implemented."
        )