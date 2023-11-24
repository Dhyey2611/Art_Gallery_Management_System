import streamlit as st
import pandas as pd

from customer.database import show_costliest
from customer.database import buy_art_db

def buy_costliest(id):
    result = show_costliest()
    if len(result)==0:
        st.text("No art is currently available")
    df = pd.DataFrame(result, columns=["Art ID", "Description", "Price", "Artist Name"])
    st.dataframe(df)
    if st.button("Buy This Art"):
        art_id = result[0][0]
        buy_art_db(id, art_id)
        st.success("Successfully bought Art")