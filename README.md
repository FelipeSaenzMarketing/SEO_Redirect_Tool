# 🔁 Generador Automático de Redirecciones 301

Aplicación web creada con **Streamlit** para generar redirecciones entre URLs antiguas y nuevas según su similitud textual.

## 🚀 Cómo usarla

1. Sube un archivo con las **URLs antiguas** (`urls_old.csv` o `.txt`).
2. Sube un archivo con las **URLs nuevas** (`urls_new.csv` o `.txt`).
3. Ajusta el **umbral de similitud** (por ejemplo, 0.6 o 0.7).
4. Descarga el archivo CSV con las redirecciones sugeridas.

## 📦 Despliegue en Streamlit Cloud

1. Sube este repositorio a tu cuenta de GitHub.
2. Ve a [https://share.streamlit.io](https://share.streamlit.io).
3. Conecta tu cuenta de GitHub y selecciona este proyecto.
4. En la configuración:
   - Archivo principal: `app.py`
   - Rama: `main`
5. ¡Listo! La app se ejecutará directamente en tu navegador.

## 🧰 Requisitos

- Python 3.8 o superior
- Streamlit (`pip install streamlit`)

## 📄 Ejemplo de entrada

**urls_old.csv**
```
/blog/python-basics
/blog/ai-introduction
```

**urls_new.csv**
```
/articulos/python-basicos
/articulos/introduccion-a-la-ia
```

**Salida (`redirects.csv`)**
```
old_url,new_url,similarity
/blog/python-basics,/articulos/python-basicos,0.92
/blog/ai-introduction,/articulos/introduccion-a-la-ia,0.88
```
