from app.tools.tool import get_incident_tool, search_logs_tool, search_runbooks_tool

print(search_logs_tool.invoke({
    "service_id" : "svc-payments",
    "query" : "payments issue"
}))