import streamlit as st
import pandas as pd

from customer.database import view_purchased_art_db 

def view_purchased_art(id):
    result = view_purchased_art_db(id)
    df = pd.DataFrame(result, columns=["Art ID", "Art Description", "Price", "Artist Name"])
    st.dataframe(df)
    
    