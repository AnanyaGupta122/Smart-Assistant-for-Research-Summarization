# 📄 Smart Assistant for Research Summarization

An AI-powered assistant that understands, summarizes, and reasons through large documents like research papers, legal files, or technical manuals. Built using Streamlit and NLP models, this tool enables contextual question answering and logic-based interaction from uploaded PDF or TXT documents.

--------------------------------------------------------------------------------

## 🎯 Task Objective

As part of EZ's GenAI assessment, the goal is to develop a document-aware assistant that goes beyond simple summarization or keyword search and demonstrates:

- Contextual understanding  
- Logical reasoning  
- AI-powered interaction  

-------------------------------------------------------------------------------

##  What the Assistant Must Do

-  **Accept document uploads** in PDF or TXT format  
-  **Auto-generate a summary** (≤ 150 words) upon upload  
-  **Ask Anything Mode**  
  - Users can ask free-form questions  
  - Assistant answers based on document context  
  - Every answer must include justification from the source  
-  **Challenge Me Mode**  
  - System generates 3 logic-based or comprehension questions  
  - Users answer and receive AI-evaluated feedback with justification  

-------------------------------------------------------------------------------


## Setup Instructions

1. Clone the Repository
```bash
git clone https://github.com/AnanyaGupta122/Smart-Assistant-for-Research-Summarization.git
cd Smart-Assistant-for-Research-Summarization

2. Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install Requirements
pip install -r requirements.txt

4. Run the App Locally
 streamlit run app.py
-------------------------------------------------------------------------------



### Architecture & Reasoning Flow
## High-Level Flow

[User Uploads Document (.pdf/.txt)]
              ↓
[Document Text Extraction]
              ↓
[Auto Summary Generated (≤ 150 words)]
              ↓
  ┌───────────────────────┬────────────────────────┐
  │     Ask Anything      │      Challenge Me      │
  │ (Freeform QA Mode)    │ (Logic Q Gen & Eval)   │
  └───────────────────────┴────────────────────────┘
------------------------------------------------------------------------------------


# Reasoning Workflow
Ask Anything Mode
1. User inputs question.
2. Assistant embeds the question and all sentences in the doc.
3. Uses cosine similarity to find the most relevant answer.
4. Returns:
   (i)Best matched sentence
   (ii)Answer justification based on document content

# Challenge Me Mode
1. Assistant generates 3 logic-based questions from document.
2. User attempts to answer each.
3. Assistant compares user answer with expected sentence using embeddings.
4. Returns:
   Feedback: ✅ Correct or ❌ Incorrect
   Justification with source snippet
