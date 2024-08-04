from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.messages import BaseMessage, AIMessage, convert_to_messages
from typing import Annotated, TypedDict
from langchain_core.documents import Document
from langgraph.graph.message import AnyMessage, add_messages

class code(BaseModel):

    prefix: str = Field(description="Description of the problem and approach")
    imports: str = Field(description="Code block import statements")
    code: str = Field(description="Code block not including import statements")
    description = "Schema for code solutions to questions about LCEL."
    
    
class GraphState(TypedDict):

    error: str
    messages: Annotated[list[AnyMessage], add_messages]
    generation: str
    iterations: int