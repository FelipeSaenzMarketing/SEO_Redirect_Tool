import streamlit as st
import csv
from difflib import SequenceMatcher
import io

from branding import apply_branding, brand_header, project_panel, metric_guide, signature

NO_MATCH_LABEL = "No sufficient match"


# --- Calculate similarity between two URLs ---
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


# --- Core matching logic ---
def generate_redirects(file_old, file_new, threshold):
    urls_old = [line.strip() for line in file_old.read().decode("utf-8").splitlines() if line.strip()]
    urls_new = [line.strip() for line in file_new.read().decode("utf-8").splitlines() if line.strip()]
    results = []

    for old in urls_old:
        best_match = None
        best_score = 0
        for new in urls_new:
            score = similarity(old, new)
            if score > best_score:
                best_match = new
                best_score = score

        if best_score >= threshold:
            results.append((old, best_match, round(best_score, 3)))
        else:
            results.append((old, NO_MATCH_LABEL, round(best_score, 3)))

    return results


# --- Streamlit interface ---
st.set_page_config(page_title="301 Redirect Generator", layout="centered")

apply_branding()
brand_header(
    "301 Redirect Generator",
    "Map old URLs to their closest new counterparts automatically during a site migration.",
)
project_panel(
    "When you migrate a site or restructure its URLs, every old address needs a 301 redirect "
    "to the right new page to preserve SEO equity. This tool compares your old and new URL "
    "lists with a textual similarity algorithm and suggests the best match for each old URL, "
    "so you can build your redirect map in minutes instead of by hand.",
    points=[
        "Upload one old-URLs file and one new-URLs file (.csv or .txt, one URL per line).",
        "Set the minimum similarity you are willing to accept.",
        "Download a ready-to-use redirect map as CSV.",
    ],
)

metric_guide(
    "How to read the results",
    {
        "old_url": "A URL from your previous site structure that needs a redirect.",
        "new_url": "The most textually similar URL from your new list, suggested as the redirect target.",
        "similarity": "A 0-1 score of how close the two URLs are. Closer to 1 means a stronger, safer match.",
        "Minimum similarity": "The threshold below which no match is proposed. Raise it for stricter matching, lower it to catch more URLs.",
        f"'{NO_MATCH_LABEL}'": "No new URL cleared the threshold. Review these manually and map them by hand.",
    },
)

file_old = st.file_uploader(
    "Upload old URLs file (.csv or .txt, one URL per line)", type=["csv", "txt"]
)
file_new = st.file_uploader(
    "Upload new URLs file (.csv or .txt, one URL per line)", type=["csv", "txt"]
)

threshold = st.slider("Minimum accepted similarity level", 0.0, 1.0, 0.5, 0.05)

if file_old and file_new:
    st.success("Files successfully uploaded.")
    results = generate_redirects(file_old, file_new, threshold)
    st.write("### Suggested redirect results")
    st.dataframe(results, use_container_width=True)

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["old_url", "new_url", "similarity"])
    writer.writerows(results)

    st.download_button(
        label="Download redirects CSV",
        data=output.getvalue(),
        file_name="redirects.csv",
        mime="text/csv",
    )
    st.info("Tip: review low-similarity matches before applying them as final redirects.")
else:
    st.warning("Please upload both files to begin.")

signature()
