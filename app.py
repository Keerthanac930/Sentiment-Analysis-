import pandas as pd
import streamlit as st

from src.absa.analyzer import AspectSentimentAnalyzer


st.set_page_config(page_title="Aspect-Based Sentiment Analysis", page_icon="ABSA")

st.title("Aspect-Based Sentiment Analysis")
st.write("Analyze review sentiment for specific aspects such as food, service, price, delivery, and quality.")

analyzer = AspectSentimentAnalyzer()

review_text = st.text_area(
    "Enter a review",
    value="The food was delicious and affordable, but the delivery was late.",
    height=140,
)

if st.button("Analyze Review"):
    results = analyzer.analyze(review_text)

    st.subheader("Sentiment Result")
    st.dataframe(pd.DataFrame(results), use_container_width=True)

uploaded_file = st.file_uploader("Upload CSV with a review column", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    if "review" not in data.columns:
        st.error("The uploaded CSV must contain a review column.")
    else:
        batch_results = analyzer.analyze_dataframe(data)
        st.subheader("Batch Results")
        st.dataframe(batch_results, use_container_width=True)
