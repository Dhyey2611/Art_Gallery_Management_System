import streamlit as st
from customer.database import buy_art_db
from customer.database import avail_art_ids

def buy_art(id):
    avail_arts = avail_art_ids()
    avail_arts = [item[0] for item in avail_arts]
    art_id = st.selectbox("Enter Art ID to buy:", avail_arts)
    if st.button("Buy Art"):
        buy_art_db(id, art_id)
        st.success("Successfully bought Art")