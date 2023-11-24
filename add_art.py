import streamlit as st
from artist.database import add_art_db

def add_art(id):
    art_desc = st.text_input("Enter Description:")
    art_price = st.number_input("Enter Price:", min_value=0, step=1)
    if st.button("Add Art"):
        add_art_db(id, art_desc, art_price)
        st.success("Successfully added Art")