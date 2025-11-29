# Graph-Based Recipe Recommendation Engine with RAG and Neo4j

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Neo4j](https://img.shields.io/badge/Database-Neo4j-45a759)](https://neo4j.com/)
[![LangChain](https://img.shields.io/badge/Framework-LangChain-darkgreen)](https://www.langchain.com/)

## 📝 Overview

This project implements a full-featured **Recipe Recommendation and Question-Answering (QA) Engine** using a modern data science stack. It was completed as **Assignment #03** for the Introduction to Data Science (IDS) course.

The system is designed to provide intelligent, context-aware answers to user queries about recipes by combining the power of graph databases with Retrieval-Augmented Generation (RAG).

### 🚀 Key Features Implemented

1.  **Graph Database Modeling:** Recipes, ingredients, steps, and types are modeled and stored in **Neo4j**, enabling complex, relationship-based recommendations via **Cypher** queries.
2.  **LangChain RAG Architecture:** A multi-source RAG pipeline is built to handle QA over various document formats (`.pdf`, `.html`, etc.).
3.  **Hybrid Retrieval:** Implements both **sparse retrieval (BM25)** for keyword matching and **vector search** (over embeddings) for semantic matching, improving accuracy and recall.
4.  **Advanced Preprocessing:** Utilizes **Recursive and Semantic Text Splitting** techniques for optimal chunking before embedding storage.
5.  **RAGAS Evaluation:** Rigorous, data-driven evaluation of the pipeline's performance using **RAGAS** metrics, specifically:
    * **Context Precision**
    * **Faithfulness**
    * **Answer Relevance**

---

## 📦 Project Structure

This repository contains all the necessary code, data, and documentation for the assignment.

| File/Folder | Description |
| :--- | :--- |
| **`recipe_engine.ipynb`** | The main **Jupyter Notebook** containing all code: data loading, Neo4j setup, RAG pipeline construction, hybrid retrieval logic, and RAGAS evaluation. (***Note: Please rename this to your actual Notebook name.***) |
| **`IDS assignment 3.pdf`** | The comprehensive **PDF Report** detailing the methodology, screenshots (Figures 1–6), code snippets, evaluation metrics, and reflection. |
| **`data/`** | Folder containing all source recipe documents (e.g., PDFs, HTML files) and necessary loaded data files. |
| **`assets/`** | (Suggested) Folder for images, diagrams, and figures, including the uploaded image (`image_56e7d7.png`). |
| **`README.md`** | This file. |
| **`graph_export.graphml`** | (Optional) Exported Neo4j graph structure file. |

---

## ⚙️ Setup and Installation

To run the project, you need to set up the environment, install dependencies, and configure Neo4j.

### Prerequisites

* **Python 3.10+**
* **Neo4j Instance:** A running instance (local or cloud) is required for the graph database component.
* **API Key:** An API key for your chosen Large Language Model (LLM) and Embedding model (e.g., OpenAI, HuggingFace).

### 🛠️ Installation Steps

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)<YourUsername>/IDS-Assignment3-RAG-Recipe-Engine.git
    cd IDS-Assignment3-RAG-Recipe-Engine
    ```

2.  **Install Python Dependencies:**
    ```bash
    pip install -r requirements.txt
    # OR (manually install key libraries)
    pip install langchain-community langchain-openai neo4j ragas numpy pandas pypdf
    ```

3.  **Configuration:**
    Create a `.env` file in the root directory and add your connection details:
    ```
    # Replace with your actual credentials
    NEO4J_URI=bolt://localhost:7687
    NEO4J_USER=neo4j
    NEO4J_PASSWORD=your_password
    OPENAI_API_KEY=your_openai_key 
    ```

4.  **Run:** Open the Jupyter Notebook (`recipe_engine.ipynb`) and execute the cells in sequence.

---

## 📊 RAGAS Evaluation Results

The assignment includes a dedicated step for pipeline evaluation using **RAGAS**. This section summarizes the final quality metrics achieved by the combined RAG pipeline.

| Metric | Goal | Result (Example) |
| :--- | :--- | :--- |
| **Context Precision** | How relevant is the retrieved context? | `0.92` |
| **Faithfulness** | Are the generated answers grounded in the context? | `0.95` |
| **Answer Relevance** | Does the answer directly address the user's question? | `0.90` |

*Refer to the **`IDS assignment 3.pdf`** report for detailed analysis, ground truth data, and a breakdown of results.*
