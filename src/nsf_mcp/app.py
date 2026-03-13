import os

from fastmcp import FastMCP

from nsf_mcp.routes import register_routes
from nsf_mcp.tools import register_tools

mcp = FastMCP("NSF Research Explorer")

register_routes(mcp)
register_tools(mcp)


# Expose ASGI app for uvicorn / cloud deployments
app = mcp.http_app(stateless_http=True)


def main() -> None:
    port_str = os.environ.get("PORT") or os.environ.get("DATABRICKS_APP_PORT")
    if port_str:
        import uvicorn

        uvicorn.run(app, host="0.0.0.0", port=int(port_str))
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()