# LatestAiDevelopment Crew

Welcome to the LatestAiDevelopment Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.11 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Configuration

Before running the project, you need to set up the necessary API keys. Copy the `.env_example` file to `.env` and fill in the required values:

```bash
cp .env_example .env
```

Open the newly created `.env` file and add your API keys for the services used by the crew. The required keys are:

- `OPENAI_API_KEY`: Your API key for accessing OpenAI models.
- `SERPER_API_KEY`: Your API key for using the SerperDevTool for search.

### Customizing

- Modify `src/latest_ai_development/config/agents.yaml` to define your agents
- Modify `src/latest_ai_development/config/tasks.yaml` to define your tasks
- Modify `src/latest_ai_development/crew.py` to add your own logic, tools and specific args
- Modify `src/latest_ai_development/main.py` to set the `default_topic` variable with your desired search term.

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the latest-ai-development Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run and create a markdown file in the root folder with the output of a research on the topic defined by the `default_topic` variable in `src/latest_ai_development/main.py`. The filename will be based on the topic.

## Understanding Your Crew

The latest-ai-development Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the LatestAiDevelopment Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.

---

# LatestAiDevelopment Crew (Português Brasileiro)

Bem-vindo ao projeto LatestAiDevelopment Crew, desenvolvido com [crewAI](https://crewai.com). Este template foi projetado para ajudá-lo a configurar um sistema de IA multiagente com facilidade, aproveitando o framework poderoso e flexível fornecido pelo crewAI. Nosso objetivo é permitir que seus agentes colaborem efetivamente em tarefas complexas, maximizando sua inteligência e capacidades coletivas.

## Instalação

Certifique-se de ter o Python >=3.11 <3.13 instalado em seu sistema. Este projeto utiliza [UV](https://docs.astral.sh/uv/) para gerenciamento de dependências e pacotes, oferecendo uma experiência de configuração e execução perfeita.

Primeiro, se você ainda não o fez, instale o uv:

```bash
pip install uv
```

Em seguida, navegue até o diretório do seu projeto e instale as dependências:

(Opcional) Bloqueie as dependências e instale-as usando o comando CLI:
```bash
crewai install
```
### Configuração

Antes de executar o projeto, você precisa configurar as chaves de API necessárias. Copie o arquivo `.env_example` para `.env` e preencha os valores necessários:

```bash
cp .env_example .env
```

Abra o arquivo `.env` recém-criado e adicione suas chaves de API para os serviços utilizados pela crew. As chaves necessárias são:

- `OPENAI_API_KEY`: Sua chave de API para acessar os modelos da OpenAI.
- `SERPER_API_KEY`: Sua chave de API para usar a SerperDevTool para pesquisa.

### Customização

- Modifique `src/latest_ai_development/config/agents.yaml` para definir seus agentes
- Modifique `src/latest_ai_development/config/tasks.yaml` para definir suas tarefas
- Modifique `src/latest_ai_development/crew.py` para adicionar sua própria lógica, ferramentas e argumentos específicos
- Modifique `src/latest_ai_development/main.py` para definir a variável `default_topic` com o termo de pesquisa desejado.

## Executando o Projeto

Para iniciar sua crew de agentes de IA e começar a execução das tarefas, execute este comando a partir da pasta raiz do seu projeto:

```bash
$ crewai run
```

Este comando inicializa a LatestAiDevelopment Crew, reunindo os agentes e atribuindo-lhes tarefas conforme definido em sua configuração.

Este exemplo, sem modificações, será executado e criará um arquivo markdown na pasta raiz com o resultado de uma pesquisa sobre o tópico definido pela variável `default_topic` em `src/latest_ai_development/main.py`. O nome do arquivo será baseado no tópico.

## Entendendo Sua Crew

A LatestAiDevelopment Crew é composta por múltiplos agentes de IA, cada um com papéis, objetivos e ferramentas únicas. Esses agentes colaboram em uma série de tarefas, definidas em `config/tasks.yaml`, aproveitando suas habilidades coletivas para alcançar objetivos complexos. O arquivo `config/agents.yaml` descreve as capacidades e configurações de cada agente em sua crew.

## Suporte

Para suporte, perguntas ou feedback sobre a LatestAiDevelopment Crew ou crewAI.
- Visite nossa [documentação](https://docs.crewai.com)
- Entre em contato conosco através do nosso [repositório GitHub](https://github.com/joaomdmoura/crewai)
- [Junte-se ao nosso Discord](https://discord.com/invite/X4JWnZnxPb)
- [Converse com nossa documentação](https://chatg.pt/DWjSBZn)

Vamos criar maravilhas juntos com o poder e a simplicidade do crewAI.
