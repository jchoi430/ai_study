## What is AI

Artificial Intelligence refers to computer systems designed to simulate intelligent human behavior and cognitive functions such as learning, reasoning, and problem-solving.

**Examples:**
- Virtual assistants (Siri, Alexa)
- Game-playing AI (Chess, Go engines)
- Recommendation systems (Netflix, Spotify)

## What is Machine Learning

Machine Learning is a subset of AI that enables systems to learn and improve from experience and data without being explicitly programmed for each task.

**Examples:**
- Email spam detection
- Credit score prediction
- Customer segmentation

## What is Deep Learning

Deep Learning uses artificial neural networks with multiple layers to process complex patterns in large datasets, powering many modern AI applications.

**Examples:**
- Facial recognition systems
- Large language models (GPT, BERT)
- Medical image analysis

## What is Natural Language Processing

Natural Language Processing enables computers to understand, interpret, and generate human language in a meaningful and useful way.

**Examples:**
- Chatbots and conversational AI
- Machine translation (Google Translate)
- Sentiment analysis

## What is Computer Vision

Computer Vision is an AI field that enables machines to interpret and understand visual information from images and videos.

**Examples:**
- Object detection in images
- Autonomous vehicle navigation
- Medical image diagnosis

## What is Usage Case of AI

Usage cases are real-world applications of AI technologies, such as recommendation systems, autonomous vehicles, medical diagnosis, and natural language chatbots.

**Examples:**
- E-commerce product recommendations
- Self-driving cars and autonomous delivery
- Healthcare diagnostics and drug discovery

## What is Generative AI

Generative AI refers to algorithms and models that can create new content, such as text, images, audio, or code, based on the patterns they learned from their training data.

**Examples:**
- Generating synthetic images (Midjourney, DALL-E)
- Writing articles, emails, or code (GitHub Copilot)
- Composing original music tracks

## What is LLM

A Large Language Model (LLM) is a type of Generative AI specifically designed to understand and generate human language by predicting the next word based on vast amounts of text data.

**Examples:**
- Text summarization and completion
- Language translation
- Question answering applications

## What is Token

Tokens are the fundamental units of data handled by large language models, representing chunks of text like words, parts of words, or single characters.

**Examples:**
- The word "apple" might be one token
- A rare word might be split into multiple sub-word tokens
- Special tokens representing the start or end of a sequence

## What is Claude, Gemini, ChatGPT

These are state-of-the-art conversational AI chatbots powered by large language models developed by different tech companies to interact with users through natural language.

**Examples:**
- ChatGPT (developed by OpenAI)
- Gemini (developed by Google)
- Claude (developed by Anthropic)

## What is Agent

An AI Agent is an autonomous system that uses an LLM to perceive its environment, make decisions, and take actions to achieve a specific goal over a sequence of steps.

**Examples:**
- Autonomous coding assistants
- Customer support bots that can issue refunds
- Automated research tools

## What is RAG

Retrieval-Augmented Generation (RAG) is a technique that improves an LLM's responses by fetching relevant, up-to-date facts from an external knowledge base before generating an answer.

**Examples:**
- Corporate chatbots querying internal policies
- Customer support referencing specific product manuals
- Legal assistants searching through past cases

## What is Prompt Engineering

Prompt Engineering is the practice of designing and refining the input instructions (prompts) given to an AI model to achieve the most accurate and desired output.

**Examples:**
- Providing "few-shot" examples in a prompt
- Assigning a persona ("Act as a senior software engineer")
- Structuring inputs to elicit step-by-step reasoning

## What is Fine-tuning

Fine-tuning is the process of taking a pre-trained AI model and further training it on a smaller, domain-specific dataset to adapt it to specialized tasks and improve performance.

**Examples:**
- Adapting a general LLM to understand medical jargon
- Training a model to strictly adhere to a company's brand voice
- Improving an image generator's ability to draw specific objects

## What is Embedding

Embeddings are dense numerical representations (vectors) of data, such as words or images, that capture semantic meaning, allowing algorithms to measure the similarity between different pieces of data.

**Examples:**
- Word embeddings in text analysis
- Image embeddings for visual search
- Used extensively behind the scenes in recommendation systems

## What is Vector DB

A Vector Database is specialized database designed to efficiently store and search high-dimensional vector embeddings, making it ideal for retrieving similar concepts within AI applications.

**Examples:**
- Finding documents similar to a user's query
- Visual search engines matching related images
- The primary storage backend for RAG architectures

## What is Skills of AI

AI "skills" refer to specialized capabilities or tool-use instructions modularly added to an AI system, allowing it to interact with specific APIs or perform complex tasks beyond simple text generation.

**Examples:**
- A skill for searching the web
- A skill for executing Python code natively
- A skill for reading local files

## What is Agentic AI

Agentic AI refers to a shift in AI systems from passive responders to proactive actors capable of planning, goal-setting, adapting, and using external tools with minimal human intervention.

**Examples:**
- A system deciding the best multi-step strategy to complete a ticket
- Autonomous workflows making database edits
- AI agents evaluating their own output to self-correct

## What is Multi-Agent AI

Multi-Agent AI involves multiple autonomous AI agents interacting, collaborating, or competing with each other within an environment to solve complex problems more effectively than a single agent could alone.

**Examples:**
- Simulated economies with AI buyers and sellers
- A collaborative team of a 'coder agent' and a 'reviewer agent'
- Multi-robot coordination in physical environments


## What is skills.md

A `skills.md` file (or similar) is a configuration or documentation file commonly used in agentic frameworks to explicitly define the instructions, capabilities, and tools an AI agent can access.

**Examples:**
- Defining how an agent should read/write to a specific database
- Providing exact instructions on how to use a custom API or SDK
- Containing guidelines on coding style or project conventions

## What is projects.md

A `projects.md` file serves as a high-level roadmap or master document within an AI-assisted workspace, outlining the current goals, architecture decisions, and task lists.

**Examples:**
- Tracking open and completed tasks for an AI agent
- Listing the core technology stack and architecture of a project
- Storing notes and context about features currently under development

## What is best design pattern for AI agent

The best design pattern for an AI agent usually involves a "ReAct" (Reasoning and Acting) loop, augmented by modular tools, structured memory, and clear boundaries of execution.

**Examples:**
- **ReAct Pattern:** The agent loops through thinking, acting, and observing the result
- **Planner-Executor Pattern:** One agent creates a high-level plan, and specialized sub-agents execute individual steps
- **Evaluator-Optimizer:** An agent iteratively reviews and refines its own output before presenting the final result

## What is best practice for skills.md

Best practices for writing a skills document involve making instructions deterministic, highly specific, and offering clear examples of inputs and desired outputs, treating it like programming rather than casual conversation.

**Examples:**
- Using precise, unambiguous language and imperative commands
- Providing concrete "good" and "bad" examples of tool use
- Keeping the scope of each skill narrow and focused on a single responsibility

## What is agent plugin for Gemini, ChatGPT, or Claude

An agent plugin is an extension or modular capability that allows foundation models to interact with third-party services, execute code, or fetch real-time data beyond their static training data.

**Examples:**
- Custom enterprise plugins that let models query internal systems like Jira or GitHub
- ChatGPT's Code Interpreter or Web Browsing plugins
- Gemini's extensions for fetching data from Google Workspace (Docs, Drive, Mail)
