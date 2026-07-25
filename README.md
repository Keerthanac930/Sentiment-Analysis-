# Aspect-Based Sentiment Analysis

This repository contains a structured Python project for Aspect-Based Sentiment Analysis (ABSA). Instead of assigning only one sentiment label to an entire review, the project identifies specific product or service aspects, such as food, service, price, delivery, ambience, quality, and support, then estimates sentiment for each detected aspect.

## Features

- Detects predefined aspects from review text.
- Classifies aspect-level sentiment as positive, negative, or neutral.
- Supports single-review prediction from the command line.
- Supports batch analysis from CSV files.
- Includes an optional Streamlit interface for interactive use.
- Provides a small sample dataset for testing the workflow.
- Keeps the original academic report in `docs/`.

## Technologies

- Python 3
- pandas
- Streamlit
- unittest
- Rule-based NLP baseline using aspect keywords and sentiment lexicons

## Project Structure

```text
Aspect-Based-Sentiment-Analysis/
├── app.py
├── data/
│   └── sample_reviews.csv
├── docs/
│   └── AKSK REPORT.pdf
├── src/
│   └── absa/
│       ├── __init__.py
│       ├── analyzer.py
│       ├── cli.py
│       ├── lexicon.py
│       └── preprocessing.py
├── tests/
│   └── test_analyzer.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Keerthanac930/Sentiment-Analysis-.git
cd Sentiment-Analysis-
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Analyze one review:

```bash
python -m src.absa.cli --text "The food was delicious but the service was slow."
```

Analyze reviews from a CSV file:

```bash
python -m src.absa.cli --input data/sample_reviews.csv --output outputs/predictions.csv
```

Run the Streamlit app:

```bash
streamlit run app.py
```

Run tests:

```bash
python -m unittest
```

## Input Format

For batch analysis, use a CSV file with a `review` column:

```csv
review
"The food was excellent but delivery was late."
"The price is affordable and the quality is good."
```

## Example Output

```text
food: positive
delivery: negative
```

## Future Enhancements

- Train a machine learning model on labelled ABSA datasets.
- Add transformer-based models such as BERT for aspect extraction and sentiment classification.
- Support custom aspect dictionaries through configuration files.
- Add a REST API for integration with other applications.
- Add visual dashboards for aspect-wise sentiment trends.

## License

Add a license before distributing this project publicly.
