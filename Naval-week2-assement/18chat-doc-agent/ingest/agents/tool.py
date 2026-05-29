from datetime import datetime
from langchain.tools import tool

@tool
def current_time():
    """Return current time"""

    return str(datetime.now())