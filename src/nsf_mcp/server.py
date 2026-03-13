"""
Entry point for running the MCP server.
"""

from .tools import mcp


def main():
    """
    Start the MCP server.
    """

    mcp.run()


if __name__ == "__main__":
    main()
