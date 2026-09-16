from dataclasses import dataclass
from app.enums import Role
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import GOOGLE_API_KEY
from app.tools.tool import get_incident_tool, get_recent_deployments_tool, search_logs_tool, get_metrics_tool, search_runbooks_tool, get_service_status_tool
from app.investigation_workflow import graph

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite", 
    api_key=GOOGLE_API_KEY,
    temperature = 0.1
)

@dataclass
class RuntimeContext:
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

context = RuntimeContext(
    engineer_id="eng-001",
    team_id="payments",
    role="senior_engineer",
    environment="production"
)

# result = agent.invoke({
#     "messages" : [
#         {
#             "role" : "user",
#             "content" : "Investigate INC-167042 and tell me the likely root cause."
#         }
        
#     ]
# }, context=context)

initial_state = {
    "incident_id": "INC-1042",
    "incident": {},
    "service": "",
    "deployments": [],
    "logs": [],
    "metrics": [],
    "runbooks": [],
    "conclusion": ""
}

result = graph.invoke(initial_state)

print(result["conclusion"])


# for message in result["messages"]:
#     print("\n---")
#     print(type(message).__name__)
#     print(message)

# print(result["messages"][-1].text)