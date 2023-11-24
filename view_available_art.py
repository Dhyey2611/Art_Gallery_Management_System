import streamlit as st
import pandas as pd

from customer.database import view_available_art_db 

def view_available_art():
    result = view_available_art_db()
    df = pd.DataFrame(result, columns=["Art ID", "Description", "Price", "Artist Name"])
    st.dataframe(df)
