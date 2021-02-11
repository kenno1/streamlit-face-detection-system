import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Streamlit Face Detection app')

upload_file = st.file_uploader("choose an image ...", type='jpg')

if upload_file is not None:
    img = Image.open(upload_file)
    st.image(img, caption='Uploaded Image.', use_column_width=True)


"""
# this is explain.
blow function is test.
"""

st.write('DataFrame')
st.write(
    pd.DataFrame({
        '1st column': [1, 2, 3, 4],
        '2nd column': [10, 20, 30, 40]
    })
)

if st.checkbox('show DataFrame'):
    chart_df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.line_chart(chart_df)
