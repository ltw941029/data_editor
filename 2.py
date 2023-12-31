import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
       {"명령어": "st.selectbox", "평점": 4, "is_widget": True},
       {"명령어": "st.balloons", "평점": 5, "is_widget": False},
       {"명령어": "st.time_input", "평점": 3, "is_widget": True},
   ]
)

edited_df = st.data_editor(df, num_rows="fixed",hide_index=False, column_order=('is_widget','명령어','평점'))
edited_df = st.data_editor(df, num_rows="fixed",hide_index=False, column_order=None)
