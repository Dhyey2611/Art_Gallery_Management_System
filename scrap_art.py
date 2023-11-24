import streamlit as st

from customer.database import resell_art
from customer.database import view_purchased_art_db

def scrap_art(id):
    result = view_purchased_art_db(id)
    ids = [item[0] for item in result]
    print(ids)
    st.subheader("Re-Sell Art")
    art_id = st.selectbox("Art ID:", ids)
    if st.button("Re-Sell"):
        resell_art(id, art_id)
        st.success("Art Returned to Gallery")