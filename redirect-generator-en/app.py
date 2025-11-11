import streamlit as st
import csv
from difflib import SequenceMatcher
import io

# --- Function to calculate similarity between two URLs ---
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

# --- Main function adapted for Streamlit ---
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
            results.append((old, "❌ No sufficient match", round(best_score, 3)))

    return results

# --- Streamlit Interface ---
st.set_page_config(page_title="Redirect Generator", page_icon="🔁", layout="centered")

st.title("🔁 Redirect Generator Tool - Similarity Score")
st.write("Upload your **old** and **new** URL files to generate redirect suggestions based on textual similarity.")
st.write("Redirect Tool by Felipe Saenz.")

file_old = st.file_uploader("📂 Upload old URLs file (.csv or .txt with one column for better visualization)", type=["csv", "txt"])
file_new = st.file_uploader("📂 Upload new URLs file (.csv or .txt with one column for better visualization)", type=["csv", "txt"])

threshold = st.slider("Minimum accepted similarity level", 0.0, 1.0, 0.5, 0.05)

if file_old and file_new:
    st.success("Files successfully uploaded ✅")
    results = generate_redirects(file_old, file_new, threshold)
    st.write("### Suggested Redirect Results:")
    st.dataframe(results, use_container_width=True)

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["old_url", "new_url", "similarity"])
    writer.writerows(results)

    st.download_button(
        label="⬇️ Download Redirects CSV",
        data=output.getvalue(),
        file_name="redirects.csv",
        mime="text/csv"
    )
    st.info("💡 Tip: Review low-similarity matches before applying them as final redirects.")
    st.info("   Redirect Tool by Felipe Saenz.")
else:
    st.warning("Please upload both files to begin.")
