import re


TOKEN_PATTERN = re.compile(r"[a-zA-Z']+")


def normalize_text(text):
    """Convert input text to a normalized lowercase string."""
    return str(text or "").strip().lower()


def tokenize(text):
    """Tokenize text into lowercase word tokens."""
    return TOKEN_PATTERN.findall(normalize_text(text))
