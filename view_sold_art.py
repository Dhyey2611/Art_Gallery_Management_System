import streamlit as st
import pandas as pd
from artist.database import view_sold_art_db

def view_sold_art(id):
    result = view_sold_art_db(id)
    df = pd.DataFrame(result, columns=["ID", "Description", "Price", "Available?"])
    st.dataframe(df)