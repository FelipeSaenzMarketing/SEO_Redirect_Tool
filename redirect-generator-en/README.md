# 🔁 SEO Redirect Generator By Felipe Saenz

This App automatically generates redirect suggestions between old and new URLs based on textual similarity.

## 🚀 How to Use

1. Upload a file containing your **old URLs** (`urls_old.csv` or `.txt`).
2. Upload a file containing your **new URLs** (`urls_new.csv` or `.txt`).
3. Adjust the **similarity threshold** (for example, 0.6 or 0.7).
4. Download the generated CSV file with the suggested redirects.
5. Remember always to check manually the results of generated .csv file.


- Python 3.8 or higher  
- Streamlit (`pip install streamlit`)

## 📄 Example Input

**urls_old.csv**
```
/blog/python-basics
/blog/ai-introduction
```

**urls_new.csv**
```
/articles/python-basics
/articles/intro-to-ai
```

**Output (`redirects.csv`)**
```
old_url,new_url,similarity
/blog/python-basics,/articles/python-basics,0.92
/blog/ai-introduction,/articles/intro-to-ai,0.88
```

## 💡 Notes

- The app uses Python’s built-in `difflib` module to calculate text similarity between URLs.  
- You can fine-tune the **similarity threshold** to control match accuracy.  
- Perfect for **SEO migrations**, **content restructuring**, or **website redesigns**.

## 🧭 Example Use Case

Imagine you’re migrating your blog from `/blog/...` to `/articles/...`.  
Instead of manually matching hundreds of URLs, this app finds the best matches automatically and generates a redirect map for you.

### 🧑‍💻 Author Felipe Saenz
Created with ❤️ using **Python**, ***AI*** and **Streamlit**.
