# GEMINI-API Projects
![Last Commit](https://img.shields.io/github/last-commit/JPP-J/DL-2_GEMINI_project?style=flat-square)
![Python](https://img.shields.io/badge/Python-100%25-blue?style=flat-square)
![Languages](https://img.shields.io/github/languages/count/JPP-J/DL-2_GEMINI_project?style=flat-square)

 
## 📌 Overview

This project demonstrates the creation of a conversational chat interface using the **GEMINI-API**, Google's generative AI platform. The primary focus is on preserving chat history across sessions, enabling context-aware and coherent multi-turn conversations.

### 🧩 Problem Statement

Building chatbots that maintain meaningful conversations over multiple turns requires preserving context and chat history. Managing this efficiently while integrating with powerful large language models like GEMINI is essential for delivering smooth user experiences. This project addresses the challenge of implementing a lightweight yet effective stateful chat system using GEMINI-API.

### 🔍 Approach

- Utilize Google’s GEMINI-API (`gemini-2.0-flash` model) for generating conversational responses.
- Save and load chat history as JSON to preserve context between user interactions.
- Manage sensitive credentials securely via environment variables (`dotenv`).
- Provide simple, reusable Python code for easy integration and prototyping.

### 🎢 Processes

1. Setup environment variables for API access.
2. Load existing chat history or start a new session.
3. Send user input and chat history to GEMINI-API to generate context-aware replies.
4. Save updated chat history for future interactions.
5. Repeat to maintain an ongoing conversational state.

### 🎯 Results & Impact

- Enables developers to quickly prototype context-rich chat applications using GEMINI.
- Preserves conversational state to improve response relevance and user experience.
- Provides a foundation for more advanced stateful AI chatbots or virtual assistants.

### ⚙️ Development Challenges

- Efficiently managing and serializing chat history to keep context without excessive overhead.
- Handling environment configuration securely while maintaining ease of use.
- Ensuring API integration is robust and handles conversation continuity gracefully.
  

## **Key Features**:  
  - Maintains conversation history for context-aware responses  
  - Simple, reusable Python code with environment variable management  
  - Utilizes Google’s generative AI via the GEMINI-API for state-of-the-art conversational capabilities

## **Libraries Used**:  
  - Data Handling: `json` — for managing chat history and data serialization  
  - Environment Handling: `dotenv` — to securely manage API keys and environment variables  
  - Deep Learning / AI: `google-genai` — to interact with Google’s GEMINI API  
  - Model Used: `gemini-2.0-flash` — the underlying large language model powering chat responses

## **Provides**:  
  - [`main.py`](main.py) 
  - [`Example Result Demo`](chat_his.json)

## **Usage**:  
  - Load environment variables for your API credentials using `.env` file  
  - Run the Python scripts to start a chat session  
  - The code automatically saves and loads chat history to provide context-aware AI responses

## **Ideal for**:  
  - Developers looking to integrate GEMINI AI in conversational applications  
  - Learners experimenting with stateful chatbots and large language models  
  - Quick prototyping of AI chat features with historical context preservation


*For detailed instructions and code examples, please check the repository README and source files.*
---

