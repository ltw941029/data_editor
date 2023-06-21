import pandas as pd
import streamlit as st

df = pd.DataFrame(
    [
       {"명령어": "st.selectbox", "평점": 4, "is_widget": True},
       {"명령어": "st.balloons", "평점": 5, "is_widget": False},
       {"명령어": "st.time_input", "평점": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(
    df,
    column_config={
        "command": "Streamlit 명령어",
        "rating": st.column_config.NumberColumn(
            "당신이 주는 평점",
            help="이 명령어에 몇점이나 주시겠습니까 (1-5)?",
            min_value=1,
            max_value=5,
            step=1,
            format="%d ⭐",
        ),
        "is_widget": "위젯인가 ?",
    },
    disabled=["명령어", "is_widget"],
    hide_index=True,
)

favorite_command = edited_df.loc[edited_df["평점"].idxmax()]["명령어"]
st.markdown(f"최애 명령어는 **{favorite_command}** 🎈")
