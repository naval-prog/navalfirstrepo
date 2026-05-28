from fastmcp import FastMCP

# Create an instance of FastMCP
mcp = FastMCP()

# Fetch Tool
@mcp.tool()
async def fetch():
    """Use this tool to fetch data from a source."""

    # Simulate fetching data
    return {"data": "Hello, MCP!"}


# Process Tool
@mcp.tool()
async def process(path: str):
    """Use this tool to process the fetched data."""

    # Simulate processing
    return {
        "processed_data": "Data has been processed at path: " + path
    }


# Calculator Tool
@mcp.tool()
async def calculate(a: float, b: float, operation: str):
    """
    Perform basic calculations.
    Operations: add, subtract, multiply, divide
    """

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return {"error": "Division by zero is not allowed"}
        result = a / b
    else:
        return {
            "error": "Invalid operation. Use add, subtract, multiply, or divide"
        }

    return {
        "a": a,
        "b": b,
        "operation": operation,
        "result": result
    }


if __name__ == "__main__":
    # Run the MCP server
    mcp.run(transport="stdio")