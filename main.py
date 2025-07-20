import sys
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import os
# Initialize FastMCP server
mcp = FastMCP("weather")

def load_codes():
    names = []
    names_to_code = {}
    with open("cityCodes.csv", "r") as city_codes_file:
        all_lines = city_codes_file.readlines()
        for line in all_lines:
            code, name = line.split("	")
            names.append(name)
            names_to_code[name] = code
    return names, names_to_code

def make_request(url: str) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling."""
    headers = {
        "api_key": os.getenv["AEM_API_KEY"],
        "Accept": "application/geo+json"
    }
    with httpx.Client() as client:
        try:
            response = client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None



@mcp.tool()
def get_prediction(state: str) -> str:
    """Get predition for a given province

    Args:
        state: The name of the province
    """
    names, names_to_code = load_codes()
    prediction = ""
    for name in names:
        if state in name:
            code = names_to_code[name]
            break
    if code:
        url = f"https://opendata.aemet.es/opendata/api/prediccion/provincia/hoy/{code}"
        data = make_request(url)
        if not data :
            prediction = f"Unable to retrieve prediction for state {state} and code {code}"
        else:
            data_url = data["datos"]
            with httpx.Client() as client:
                prediction = client.get(data_url).text

    else:
        prediction = f"Could not get prediction for {state}"

    return prediction





if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')