import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
client = MultiServerMCPClient({
    "time": {
        "transport": "stdio",
        "command": "uvx",
        "args": [
            "--with", "mcp<2",
            "mcp-server-time",
            "--local-timezone=America/New_York",
        ],
    }
})


async def main():
    tools = await client.get_tools()

    model = init_chat_model(model="gemini-2.5-flash", model_provider="google-genai")

    agent = create_agent(model=model, tools=tools)

    question = HumanMessage(content="What time is it ?")

    response = await agent.ainvoke({"messages": [question]})

    pprint(response)


if __name__ == "__main__":
    asyncio.run(main())