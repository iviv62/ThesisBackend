from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from app.config import get_settings

settings = get_settings()

# Initialize the LLM
llm = ChatOpenAI(
    api_key=settings.OPENAI_API_KEY,
    model=settings.OPENAI_MODEL,
    temperature=0.7,
    streaming=True,
    max_tokens=1000
)

# Create a simple chain
def create_simple_chain():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("user", "{input}")
    ])
    
    chain = prompt | llm | StrOutputParser()
    return chain

# Example function to use the chain
async def get_ai_response(user_input: str) -> str:
    chain = create_simple_chain()
    response = await chain.ainvoke({"input": user_input})
    return response 