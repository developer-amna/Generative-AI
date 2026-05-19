import os
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
import requests

os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY")
# os.environ["OPENWEATHERMAP_API_KEY"] = userdata.get("WEATHER_API_KEY")

llm = ChatGroq(model="llama-3.1-8b-instant")

search_tool = DuckDuckGoSearchRun()
# weather_api = OpenWeatherMapAPIWrapper()

# weather_api.run('Karachi')

search_tool.run("Ai Agents")

@tool
def calculator(first_num: float, second_num: float, operation: str) -> dict:
    """Perform basic arithmetic. Operations: add, sub, mul, div"""
    ops = {"add": first_num + second_num, "sub": first_num - second_num,
           "mul": first_num * second_num}
    if operation == "div":
        return {"result": "Division by zero" if second_num == 0 else first_num / second_num}
    return {"result": ops.get(operation, f"Unknown operation: {operation}")}

from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search the web for real-time information."""
    return DuckDuckGoSearchRun().run(query)

@tool
def get_stock_price(symbol: str) -> dict:
    """Fetch latest stock price for a symbol like AAPL or TSLA."""
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={userdata.get('STOCKS_API_KEY')}"
    return requests.get(url).json()

tools = [search_tool, calculator, get_stock_price]

llm_with_tools = llm.bind_tools(tools)

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    """LLM node that may answer or request a tool call."""
    messages = state['messages']
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

tool_node = ToolNode(tools)

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_node("tools", tool_node)
graph.add_edge(START, "chat_node")
graph.add_conditional_edges("chat_node", tools_condition)
graph.add_edge("tools", "chat_node")
agent = graph.compile()

def run_agent(query: str) -> str:
    result = agent.invoke({"messages": [HumanMessage(content=query)]})
    return result["messages"][-1].content

agent

run_agent("First find out the stock price of apple using get stock price tool then use price toll then use the calcultor tool to find out how much will it take to purcahse 50 shares? ")


run_agent("Explain me AI agents")