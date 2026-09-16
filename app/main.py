from dataclasses import dataclass
from app.enums import Role
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import GOOGLE_API_KEY
from app.tools.tool import get_incident_tool, get_recent_deployments_tool, search_logs_tool, get_metrics_tool, search_runbooks_tool, get_service_status_tool

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite", 
    api_key=GOOGLE_API_KEY,
    temperature = 0.1
)

@dataclass
class RuntimeContext():
    engineer_id : str
    team_id : str
    role : Role
    environment : str

tools = [
    get_service_status_tool,
    get_metrics_tool,
    get_recent_deployments_tool,
    get_incident_tool,
    search_runbooks_tool,
    search_logs_tool
]

agent = create_agent(
    model=model,
    tools=tools,
)