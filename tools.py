from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

# Function to save research content to a text file with a timestamp
def save_to_text_file(content: str, filename: str = "research_notes.txt") -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = (
        f"---\nTimestamp: {timestamp}\nContent:\n{content}\n---\n"
    )
    with open(filename, "a", encoding="utf-8") as file:
        file.write(formatted_text)
    return f"Content saved to {filename} at {timestamp}"

# Tool for saving research content
save_tool = Tool(
    name="save_to_text_file",
    func=save_to_text_file,
    description=(
        "Saves the provided content to a text file with a timestamp. "
        "Useful for keeping research notes."
    )
)

# Web search tool using DuckDuckGo
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Searches the web for the provided query using DuckDuckGo. Returns a list of search results."
)

# Wikipedia query tool with limited output
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(
    api_wrapper=api_wrapper,
    name="wikipedia_query_run",
    description="Queries Wikipedia for the provided topic. Returns a summary of the topic and relevant links."
)
