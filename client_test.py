import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    # Launch the server using stdio
    server_params = StdioServerParameters(command="python", args=["my_mcp_server.py"])
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # List available tools
            resp = await session.list_tools()
            print("Available tools:", [tool.name for tool in resp.tools])

            # Call the greet tool
            greet_result = await session.call_tool("greet", {"name": "Alice"})
            print(greet_result.content[0].text)

            # Call the add_numbers tool
            add_result = await session.call_tool("add_numbers", {"a": 3, "b": 5})
            print("Sum result:", add_result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())
