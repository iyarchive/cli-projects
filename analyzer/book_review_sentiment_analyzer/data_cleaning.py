import pandas as pd
import re

bookreviews = pd.read_csv("bookreviews.csv")

print(bookreviews.columns)

def clean_text(text):
    text = str(text)

    # remove html tags
    text = re.sub(r"<.*?>", "", text)

    # remove weird encoding
    text = text.replace("â€™", "'")
    text = text.replace("Â", "")
    text = text.replace("&nbsp;", " ")

    # lowercase
    text = text.lower()

    return text

bookreviews["clean_review"] = bookreviews["review"].apply(clean_text)
bookreviews.to_csv("cleaned_data.csv", index=False)
