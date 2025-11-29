# Recipe Recommendation Engine with Graph RAG

A comprehensive recipe recommendation and question-answering system built with Neo4j graph database and Retrieval-Augmented Generation (RAG) architecture.

## Features

- **Multi-format document loading** (PDF, HTML, TXT, Python)
- **Advanced text splitting** (Recursive, Token-based, Semantic)
- **Hybrid retrieval system** (BM25 + FAISS vector search)
- **Graph database integration** with Neo4j
- **Natural language to Cypher query conversion**
- **RAG pipeline with GPT-4 integration**
- **Comprehensive evaluation metrics**

## Project Structure

```
recipe-recommendation-engine/
├── data/
│   ├── recipes.pdf
│   ├── recipes.html
│   ├── recipes.txt
│   └── recipe_utils.py
├── images/
│   ├── recursive_splitting.png
│   ├── token_splitting.png
│   ├── semantic_splitting.png
│   ├── vector_store.png
│   ├── neo4j_schema.png
│   └── evaluation_results.png
├── notebooks/
│   └── recipe_recommendation_engine.ipynb
├── reports/
│   └── assignment_report.pdf
├── requirements.txt
└── README.md
```

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/recipe-recommendation-engine.git
cd recipe-recommendation-engine
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file:
```bash
OPENAI_API_KEY=your_api_key_here
NEO4J_URI=your_neo4j_uri
NEO4J_USERNAME=your_username
NEO4J_PASSWORD=your_password
```

## Usage

1. **Start Jupyter Notebook**
```bash
jupyter notebook notebooks/recipe_recommendation_engine.ipynb
```

2. **Run the notebook cells in sequence**
   - Data loading and preprocessing
   - Text splitting implementations
   - Embedding generation and storage
   - Neo4j graph setup
   - RAG pipeline construction
   - Evaluation and testing

## Text Splitting Methods

### Recursive Character Splitting
- Fixed size chunks (200 characters)
- 50 character overlap
- Produced: 9 chunks

### Token-based Splitting
- 100 tokens per chunk
- 20 token overlap
- Produced: 6 chunks

### Semantic Splitting
- AI-powered meaning-based chunks
- Variable chunk sizes (23-340 characters)
- Produced: 7 chunks

## Evaluation Results

| Metric | Score |
|--------|-------|
| Context Precision | 0.95 |
| Faithfulness | 0.94 |
| String Similarity | 0.92 |

## Sample Queries

- "Find recipes without eggs"
- "Show vegetarian recipes"
- "Find recipes containing chocolate"
- "How do I make gluten-free banana bread?"
- "What's the process for roasting vegetables?"

## Technologies Used

- **Python** - Core programming language
- **Neo4j** - Graph database
- **LangChain** - RAG framework
- **FAISS** - Vector storage and similarity search
- **Sentence Transformers** - Embedding generation
- **BM25** - Sparse retrieval algorithm
- **OpenAI GPT-4** - Language model
- **Jupyter** - Development environment

## Key Insights

- Graph database modeling required careful schema design
- Hybrid retrieval (BM25 + FAISS) provided best results
- Semantic splitting created more meaningful chunks
- Evaluation metrics helped quantify system performance

## Author

**Natasha Fatima**
- Enrollment: 03-134231-055
- Department of Computer Sciences
- Bahria University, Lahore Campus

## License

This project is for academic purposes as part of the Introduction to Data Science course.
