import streamlit as st
import csv
from difflib import SequenceMatcher
import io

# --- Función para calcular similitud entre dos URLs ---
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

# --- Función principal adaptada ---
def generar_redirecciones(file_old, file_new, umbral):
    urls_old = [line.strip() for line in file_old.read().decode("utf-8").splitlines() if line.strip()]
    urls_new = [line.strip() for line in file_new.read().decode("utf-8").splitlines() if line.strip()]
    resultados = []

    for old in urls_old:
        mejor_match = None
        mejor_score = 0
        for new in urls_new:
            score = similarity(old, new)
            if score > mejor_score:
                mejor_match = new
                mejor_score = score

        if mejor_score >= umbral:
            resultados.append((old, mejor_match, round(mejor_score, 3)))
        else:
            resultados.append((old, "❌ Sin coincidencia suficiente", round(mejor_score, 3)))

    return resultados

# --- Interfaz de Streamlit ---
st.set_page_config(page_title="Generador de redirecciones", page_icon="🔁", layout="centered")

st.title("🔁 Generador automático de redirecciones 301")
st.write("Sube tus archivos de URLs **antiguas** y **nuevas** para generar coincidencias basadas en similitud textual.")

file_old = st.file_uploader("📂 Subir archivo de URLs antiguas (.csv o .txt)", type=["csv", "txt"])
file_new = st.file_uploader("📂 Subir archivo de URLs nuevas (.csv o .txt)", type=["csv", "txt"])

umbral = st.slider("Nivel mínimo de similitud aceptado", 0.0, 1.0, 0.5, 0.05)

if file_old and file_new:
    st.success("Archivos cargados correctamente ✅")
    resultados = generar_redirecciones(file_old, file_new, umbral)
    st.write("### Resultados de redirección sugeridos:")
    st.dataframe(resultados, use_container_width=True)

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["old_url", "new_url", "similarity"])
    writer.writerows(resultados)

    st.download_button(
        label="⬇️ Descargar CSV de redirecciones",
        data=output.getvalue(),
        file_name="redirects.csv",
        mime="text/csv"
    )
    st.info("💡 Consejo: revisa las coincidencias con baja similitud antes de aplicarlas como redirecciones definitivas.")
else:
    st.warning("Por favor, sube ambos archivos para comenzar.")
