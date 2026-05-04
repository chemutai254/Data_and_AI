# GenAI and RAG Project

This folder contains an example of Retrieval-Augmented Generation (RAG) using a local PDF document and transformer-based language models.

## Contents

- `GenAI_and_RAG.ipynb` — Jupyter notebook demonstrating document ingestion, embedding creation, vector search, and generative question answering.
- `Roles.pdf` — source document used for building the retrieval corpus and answering user queries from context.

## Workflow Overview

1. Load the PDF document using `PyPDFLoader`.
2. Split the document into chunks with `RecursiveCharacterTextSplitter`.
3. Create sentence embeddings for each chunk using `HuggingFaceEmbeddings`.
4. Build a vector store with `FAISS` for fast semantic retrieval.
5. Create a retriever to find the most relevant document passages for a query.
6. Use a seq2seq generation pipeline based on `google/flan-t5-large` to generate answers from the retrieved context.

## Key Notebook Steps

- Installs required packages: `langchain`, `transformers`, `sentence-transformers`, `faiss-cpu`, and `pypdf`.
- Loads `Roles.pdf` and examines the document chunks.
- Builds the vector store and retriever from the PDF content.
- Defines a `query_rag()` function to:
  - retrieve relevant passages
  - construct a prompt with context
  - generate a response using the Flan-T5 model
- Demonstrates a sample RAG query to summarize the document.

## Usage

1. Open `GenAI_and_RAG.ipynb` in Jupyter Notebook or JupyterLab.
2. Run cells sequentially from top to bottom.
3. Ensure `Roles.pdf` is present in the same folder so the notebook can ingest it correctly.
4. Modify or extend the `query_rag` function to ask custom questions about the document.

## Requirements

The notebook uses the following Python libraries:

- langchain
- langchain-community
- transformers
- sentence-transformers
- faiss-cpu
- pypdf

Install dependencies with:

```bash
pip install langchain langchain-community transformers sentence-transformers faiss-cpu pypdf
```

## Notes

- `Roles.pdf` is the data source used for retrieval and generation.
- The notebook demonstrates a local RAG pipeline without requiring an external API.
- For best performance, run the notebook where the model download and indexing can complete successfully, i.e. Google Colab.
