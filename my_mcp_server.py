from mcp.server.fastmcp import FastMCP

# Initialize server with name/description
mcp = FastMCP("Sample MCP Server")


# Register a simple tool
@mcp.tool()
def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to MCP Lab."


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    mcp.run()
