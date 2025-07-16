import streamlit as st

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #a53860;
        color: #450920;
    }

    [data-testid="stSidebar"] {
        background-color: #450920;
    }

    h1, h2, h3 {
        color: #450920;
    }

    section[data-testid="stFileUploader"] {
        background-color: #450920;
        border: 1px solid #450920;
        border-radius: 10px;
        padding: 1.5em;
    }

    section[data-testid="stFileUploader"] > div {
        background-color: #6a1540 !important;
        border: 2px dashed #ffa5ab !important;
        border-radius: 12px;
        padding: 1.5em;
        color: white !important;
        text-align: center;
    }

    div[data-testid="uploadedFileName"] {
        color: #ffffff !important;
        font-weight: bold;
    }

    div[data-testid="stAlert-success"] {
        background-color: #6a1540 !important;
        color: white !important;
        border: 1px solid #ffa5ab;
        border-radius: 8px;
    }

    .stAlert {
        border-radius: 8px;
        font-size: 1em;
    }

    div[data-testid="stMarkdownContainer"] p {
        background-color: #ffc2d1;
        padding: 1em;
        border-radius: 8px;
        color: #450920;
        font-weight: 500;
    }

    input[type="text"], textarea {
        background-color: #450920 !important;
        color: white !important;
        border: 1px solid #ffa5ab !important;
        border-radius: 6px;
    }

    .stButton>button {
        background-color: #450920;
        color: white;
        border-radius: 6px;
        padding: 0.4em 1em;
        border: none;
    }

    .stButton>button:hover {
        background-color: #450920;
    }

    div[role="radiogroup"] > label {
        background-color: #450920;
        color: white;
        border-radius: 5px;
        padding: 0.5em;
        margin-bottom: 0.5em;
        display: block;
    }
    </style>
""", unsafe_allow_html=True)



st.set_page_config(page_title="📚 GenAI Research Assistant", layout="wide")
st.title("Smart Research Assistant")

st.subheader("Upload Document")
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    st.success(" File uploaded successfully!")

    raw_text = "[Extracted text goes here]"
    
    st.subheader("Auto Summary")
    summary = "[Auto summary of the document will be shown here]"
    st.info(summary)

    st.subheader("Choose Interaction Mode")
    mode = st.radio("Select mode:", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        st.subheader("Ask a question about the document")
        question = st.text_input("Type your question:")
        if question:
            st.markdown("**Answer:** Lorem ipsum dolor sit amet.")
            st.markdown("**Justification:** Based on paragraph 3 of section 1.")

    elif mode == "Challenge Me":
        st.subheader("🧠 Answer these logic-based questions")

        for i in range(1, 4):
            st.markdown(f"**Q{i}:** [Generated logic question here]")
            user_answer = st.text_input(f"Your answer to Q{i}:", key=f"q{i}")
            if user_answer:
                st.success(f"Feedback: [Evaluated response to Q{i}]")

