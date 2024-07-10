from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_anthropic import ChatAnthropic

## get from env
from dotenv import load_dotenv
import os

load_dotenv()



class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)


### use Anthropic for LLM
llm = ChatAnthropic(model="claude-3-haiku-20240307")


def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}


# The first argument is the unique node name
# The second argument is the function or object that will be called whenever
# the node is used.
graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")

graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

###get langgrpah flow photo
from IPython.display import Image
from PIL import Image as PILImage
import io

try:
    # Generate the image
    img_data = graph.get_graph().draw_mermaid_png()

    # Convert the image data to a PIL Image
    img = PILImage.open(io.BytesIO(img_data))

    # Save the image to a file
    img.save('langGraph_work_flow.png')
except Exception as e:
    print(f"An error occurred: {e}")


#### User Chat bot
while True:
    user_input = input("User: ")
    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
    for event in graph.stream({"messages": ("user", user_input)}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)