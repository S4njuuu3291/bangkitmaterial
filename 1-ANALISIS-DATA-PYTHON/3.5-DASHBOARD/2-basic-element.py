import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Belajar Analisis Data dengan Python")

st.header("Pengembangan Dashboard")
st.subheader('Pengembangan Dashboard')

st.markdown("""
  #### My first app
  Hello, para calon praktisi data masa depan!
  """)

st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))

st.caption("Ini adalah caption")

code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

st.text('Ini adalah teks biasa, dan dibawah saya adalah latex.')

st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

st.dataframe(df,width=500,height = 150)
st.caption("Di atas adalah st.dataframe()")

st.table(data=df)
st.caption("Di atas adalah st.table() static table")

st.metric(label="Temperature", value="28 °C",delta="1.2 °C")
st.caption("Di atas adalah st.metric() metric")

st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.caption("Di atas adalah json")

x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)
st.caption("Di atas adalah chart")
