import streamlit as st

view = [100, 150, 30]
st.write('# Youtuve view')
st.write('## raw')
view
st.write('## bar chart')
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)

st.write('## pandas view')
sview