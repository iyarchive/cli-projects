import pandas as pd
import re
import html

bookreviews = pd.read_csv("bookreviews.csv")

print(bookreviews.columns)

def clean_text(text):
    text = str(text)

    # fix broken encoding
    text = text.encode("latin1", errors="ignore").decode("utf-8", errors="ignore")

    # unescape html entities
    text = html.unescape(text)

    # remove html tags
    text = re.sub(r"<[^>]+>", " ", text)

    # fix weird characters
    text = text.replace("â€™", "'")
    text = text.replace("â€œ", '"')
    text = text.replace("â€", '"')
    text = text.replace("â€”", "-")
    text = text.replace("â€“", "-")
    text = text.replace("â€¦", "...")
    text = text.replace("Â", "")

    # remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # lowercase
    text = text.lower()

    return text.strip()

bookreviews["review"] = bookreviews["review"].apply(clean_text)

bookreviews.to_csv(
    "cleaned_data.csv",
    index=False,
    encoding="utf-8-sig"
)
