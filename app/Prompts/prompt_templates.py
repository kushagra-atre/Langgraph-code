from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain import hub

class Prompts:
    
    code_gen_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are a coding assistant. Ensure any code you provide can be executed with all required imports and variables \n
                defined. Structure your answer: 1) a prefix describing the code solution, 2) the imports, 3) the functioning code block.
                \n Here is the user question:""",
            ),
            ("placeholder", "{messages}"),
        ]
    )
