from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI 
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
llm = ChatOpenAI(model="gpt-4o-mini")
response = llm.invoke("What is the capital of France?")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful research assistant. Your task is to help the user research a topic by summarizing information and providing sources."),
        ("user", "Research the topic: {query}. Provide a summary and list of sources used."),
        ("assistant", "{agent_scratchpad}")
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,   
    prompt=prompt,
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
query = input("Enter a topic to research: ")
raw_response = agent_executor.invoke({"query": query})

try:
    structured_response = parser.parse(raw_response["output"])     
    print
except Exception as e:
    print("Error parsing response", e, "Raw Response -", raw_response)