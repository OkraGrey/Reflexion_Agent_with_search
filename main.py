from dotenv import load_dotenv
from typing import List
from langchain_core.messages import BaseMessage, ToolMessage
from langgraph.graph import END, MessageGraph
from chains import revisor, first_responder
from tool_executor import execute_tools

load_dotenv()

#Building The Graph

MAX_ITERATIONS=2

builder= MessageGraph()
# 3 Nodes
# 1- Creates the initial draft
# 2- Invoke the tools for search using Tavily
# 3- Make revision
builder.add_node("draft", first_responder)
builder.add_node("execute_tools",execute_tools)
builder.add_node("revisor",revisor)

# Creating Edges

builder.add_edge("draft", "execute_tools")
builder.add_edge("execute_tools","revisor")

# Conditional logic function
def event_loop(state: List[BaseMessage]):
    count_tool_visits = sum(isinstance(item, ToolMessage) for item in state)
    if count_tool_visits > MAX_ITERATIONS:
        return END
    return "execute_tools"


# Add conditional Edge

builder.add_conditional_edges("revisor",event_loop)

# Entry point of the graph
builder.set_entry_point("draft")    

graph = builder.compile()

# print(graph.get_graph().draw_ascii())
# graph.get_graph().draw_mermaid_png(output_file_path="graph.png")

if __name__=="__main__":
    
    user_query= "Write about AI powered SOC / autonomous SOC problem domain. List startups that do that and raised capitals." 
    res = graph.invoke(user_query)
    with open("response.txt","w") as file:
        
        file.write(str(res))