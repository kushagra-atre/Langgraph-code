from fastapi import APIRouter, HTTPException
from app.models.chat_request_model import QueryRequest
from app.controller.workflow_controller import CodeWorkflow

router = APIRouter()
code_workflow = CodeWorkflow()

@router.post("/process")
async def process_query(request: QueryRequest):
    try:
        graph = code_workflow.create_workflow()
        inputs = {"messages": [("user", request.question)], "iterations": 0}
        results = graph.invoke(inputs)
        ai_messages_content = [message.content for message in results["messages"] if message.type == "ai"]
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
