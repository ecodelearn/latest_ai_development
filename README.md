# LatestAiDevelopment Crew

Welcome to the LatestAiDevelopment Crew project, powered by [crewAI](https://crewai.com). This project now includes enhanced search capabilities with advanced Google search operators.

## Installation

Ensure you have Python >=3.11 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling.

First, if you haven't already, install uv:
```bash
pip install uv
```

Then install the required dependencies:
```bash
pip install crewai crewai-tools
```

(Optional) Lock the dependencies using the CLI command:
```bash
crewai install
```

## Configuration

Before running the project, set up the necessary API keys:
```bash
cp .env_example .env
```

Add your API keys to the `.env` file:
- `OPENAI_API_KEY`: Your API key for accessing OpenAI models
- `SERPER_API_KEY`: Your API key for using the SerperDevTool

## Enhanced Search Features

The project includes an advanced search tool with various Google search operators:

- 🔍 **Exact Phrase Matching**: Search for exact phrases using quotation marks
- 📄 **File Type Filtering**: Limit results to specific file types (PDF, DOC, etc.)
- 🌐 **Site-Specific Search**: Search within specific websites or domains
- 📝 **Title Search**: Search for keywords in page titles
- 🔗 **URL Search**: Search for keywords in URLs
- 📚 **Text Content Search**: Search for keywords in page content
- 📅 **Date Range Filtering**: Filter results by date

### Using the Enhanced Search

```python
from latest_ai_development.tools.enhanced_search_tool import EnhancedSearchTool

# Create and configure the search tool
search_tool = EnhancedSearchTool()
search_config = search_tool.builder("your search topic")
    .with_file_type("pdf")
    .with_site("example.com")
    .with_date_range(after="2024-01-01")
search_tool.configure(search_config)
```

### Search Configuration Options

| Method | Description | Example |
|--------|-------------|---------|
| `with_file_type()` | Filter by file extension | `.with_file_type("pdf")` |
| `with_site()` | Search within specific domain | `.with_site("example.com")` |
| `with_title()` | Search in page titles | `.with_title("guide")` |
| `with_url()` | Search in URLs | `.with_url("docs")` |
| `with_text()` | Search in page content | `.with_text("python")` |
| `with_date_range()` | Filter by date | `.with_date_range(before="2024-12-31")` |
| `with_exact_phrase()` | Enable exact matching | `.with_exact_phrase(True)` |

## Project Customization

- Modify `src/latest_ai_development/config/agents.yaml` to define your agents
- Modify `src/latest_ai_development/config/tasks.yaml` to define your tasks
- Modify `src/latest_ai_development/crew.py` to add your own logic and tools
- Modify `src/latest_ai_development/main.py` to set the `default_topic` variable

## Running the Project

Execute from the root folder:
```bash
$ crewai run
```

This will create a markdown file with research results on your specified topic.

## Understanding Your Crew

The LatestAiDevelopment Crew consists of multiple AI agents collaborating on tasks. Each agent has unique roles and tools, defined in:
- `config/agents.yaml`: Agent capabilities and configurations
- `config/tasks.yaml`: Task definitions and dependencies

## Search Best Practices

1. **Start Broad, Then Refine**:
   ```python
   config = search_tool.builder("AI ethics")
        .with_site("academic-journals.com")
        .with_file_type("pdf")
   ```

2. **Use Date Ranges Effectively**:
   ```python
   config.with_date_range(after="2024-01-01", before="2024-12-31")
   ```

## Support

- Visit our [documentation](https://docs.crewai.com)
- Join our [Discord](https://discord.com/invite/X4JWnZnxPb)
- Check our [GitHub repository](https://github.com/joaomdmoura/crewai)

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

# LatestAiDevelopment Crew (Português Brasileiro)

[Original Portuguese content remains unchanged...]
