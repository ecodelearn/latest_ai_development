# Enhanced Search Tool for CrewAI

This project extends CrewAI's search capabilities with advanced Google search operators, providing more precise and powerful search functionality.

## Features

The enhanced search tool includes support for various Google search operators:

- 🔍 **Exact Phrase Matching**: Search for exact phrases using quotation marks
- 📄 **File Type Filtering**: Limit results to specific file types (PDF, DOC, etc.)
- 🌐 **Site-Specific Search**: Search within specific websites or domains
- 📝 **Title Search**: Search for keywords in page titles
- 🔗 **URL Search**: Search for keywords in URLs
- 📚 **Text Content Search**: Search for keywords in page content
- 📅 **Date Range Filtering**: Filter results by date

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install crewai crewai-tools
```

## Usage

### Basic Configuration

```python
from latest_ai_development.tools.enhanced_search_tool import EnhancedSearchTool

# Create and configure the search tool
search_tool = EnhancedSearchTool()
search_config = search_tool.builder("your search topic")
search_tool.configure(search_config)
```

### Advanced Search Examples

1. **Search with File Type Filter**:
```python
search_config = search_tool.builder("AI research papers")
    .with_file_type("pdf")
    .with_date_range(after="2023-01-01")
```

2. **Site-Specific Search**:
```python
search_config = search_tool.builder("machine learning")
    .with_site("arxiv.org")
    .with_exact_phrase(True)
```

3. **Combined Filters**:
```python
search_config = search_tool.builder("neural networks")
    .with_file_type("pdf")
    .with_site("stanford.edu")
    .with_title("introduction")
    .with_date_range(after="2024-01-01")
```

### Integration with CrewAI

The enhanced search tool is automatically integrated with the researcher agent:

```python
# Configure search with topic
search_config = search_tool.builder("your research topic")
search_tool.configure(search_config)

# Create crew instance
crew = LatestAiDevelopment()
crew.researcher = lambda: Agent(
    config=crew.agents_config['researcher'],
    verbose=True,
    tools=[search_tool]
)

# Run the crew
crew.crew().kickoff(inputs=search_config.as_dict)
```

## Search Configuration Options

| Method | Description | Example |
|--------|-------------|---------|
| `with_file_type()` | Filter by file extension | `.with_file_type("pdf")` |
| `with_site()` | Search within specific domain | `.with_site("example.com")` |
| `with_title()` | Search in page titles | `.with_title("guide")` |
| `with_url()` | Search in URLs | `.with_url("docs")` |
| `with_text()` | Search in page content | `.with_text("python")` |
| `with_date_range()` | Filter by date | `.with_date_range(before="2024-12-31")` |
| `with_exact_phrase()` | Enable exact matching | `.with_exact_phrase(True)` |

## Best Practices

1. **Start Broad, Then Refine**:
   ```python
   # Start with basic search
   config = search_tool.builder("AI ethics")
   
   # Refine based on results
   config.with_site("academic-journals.com")
        .with_file_type("pdf")
        .with_date_range(after="2023-01-01")
   ```

2. **Combine Multiple Filters**:
   ```python
   config = search_tool.builder("machine learning tutorial")
        .with_file_type("pdf")
        .with_title("beginners")
        .with_exact_phrase(True)
   ```

3. **Use Date Ranges Effectively**:
   ```python
   # Recent results only
   config.with_date_range(after="2024-01-01")
   
   # Specific time period
   config.with_date_range(after="2023-01-01", before="2023-12-31")
   ```

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
