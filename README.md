# LatestAiDevelopment Crew

[English](#latestaidevelopment-crew-english) | [Português Brasileiro](#latestaidevelopment-crew-português-brasileiro)

---

# LatestAiDevelopment Crew (English)

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

Bem-vindo ao projeto LatestAiDevelopment Crew, desenvolvido com [crewAI](https://crewai.com). Este projeto agora inclui capacidades avançadas de busca com operadores do Google.

## Instalação

Certifique-se de ter o Python >=3.11 <3.13 instalado em seu sistema. Este projeto utiliza [UV](https://docs.astral.sh/uv/) para gerenciamento de dependências.

Primeiro, se você ainda não instalou, instale o uv:
```bash
pip install uv
```

Em seguida, instale as dependências necessárias:
```bash
pip install crewai crewai-tools
```

(Opcional) Bloqueie as dependências usando o comando CLI:
```bash
crewai install
```

## Configuração

Antes de executar o projeto, configure as chaves de API necessárias:
```bash
cp .env_example .env
```

Adicione suas chaves de API ao arquivo `.env`:
- `OPENAI_API_KEY`: Sua chave de API para acessar os modelos OpenAI
- `SERPER_API_KEY`: Sua chave de API para usar o SerperDevTool

## Recursos de Busca Avançada

O projeto inclui uma ferramenta de busca avançada com vários operadores do Google:

- 🔍 **Correspondência Exata de Frases**: Busca por frases exatas usando aspas
- 📄 **Filtro por Tipo de Arquivo**: Limita resultados a tipos específicos (PDF, DOC, etc.)
- 🌐 **Busca em Sites Específicos**: Pesquisa dentro de websites ou domínios específicos
- 📝 **Busca em Títulos**: Pesquisa por palavras-chave em títulos de páginas
- 🔗 **Busca em URLs**: Pesquisa por palavras-chave em URLs
- 📚 **Busca em Conteúdo**: Pesquisa por palavras-chave no conteúdo das páginas
- 📅 **Filtro por Data**: Filtra resultados por data

### Usando a Busca Avançada.

```python
from latest_ai_development.tools.enhanced_search_tool import EnhancedSearchTool

# Cria e configura a ferramenta de busca
search_tool = EnhancedSearchTool()
search_config = search_tool.builder("seu tópico de busca")
    .with_file_type("pdf")
    .with_site("example.com")
    .with_date_range(after="2024-01-01")
search_tool.configure(search_config)
```

### Opções de Configuração de Busca

| Método | Descrição | Exemplo |
|--------|-----------|---------|
| `with_file_type()` | Filtra por extensão de arquivo | `.with_file_type("pdf")` |
| `with_site()` | Busca em domínio específico | `.with_site("example.com")` |
| `with_title()` | Busca em títulos | `.with_title("guia")` |
| `with_url()` | Busca em URLs | `.with_url("docs")` |
| `with_text()` | Busca no conteúdo | `.with_text("python")` |
| `with_date_range()` | Filtra por data | `.with_date_range(before="2024-12-31")` |
| `with_exact_phrase()` | Ativa correspondência exata | `.with_exact_phrase(True)` |

## Personalização do Projeto

- Modifique `src/latest_ai_development/config/agents.yaml` para definir seus agentes
- Modifique `src/latest_ai_development/config/tasks.yaml` para definir suas tarefas
- Modifique `src/latest_ai_development/crew.py` para adicionar sua própria lógica
- Modifique `src/latest_ai_development/main.py` para definir a variável `default_topic`

## Executando o Projeto

Execute a partir da pasta raiz:
```bash
$ crewai run
```

Isso criará um arquivo markdown com os resultados da pesquisa sobre o tópico especificado.

## Entendendo Sua Crew

A LatestAiDevelopment Crew consiste em múltiplos agentes de IA colaborando em tarefas. Cada agente tem funções e ferramentas únicas, definidas em:
- `config/agents.yaml`: Capacidades e configurações dos agentes
- `config/tasks.yaml`: Definições e dependências das tarefas

## Melhores Práticas de Busca

1. **Comece Amplo, Depois Refine**:
   ```python
   config = search_tool.builder("ética em IA")
        .with_site("journals-academicos.com")
        .with_file_type("pdf")
   ```

2. **Use Intervalos de Data Efetivamente**:
   ```python
   config.with_date_range(after="2024-01-01", before="2024-12-31")
   ```

## Suporte

- Visite nossa [documentação](https://docs.crewai.com)
- Entre no nosso [Discord](https://discord.com/invite/X4JWnZnxPb)
- Confira nosso [repositório GitHub](https://github.com/joaomdmoura/crewai)

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar issues e pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.
