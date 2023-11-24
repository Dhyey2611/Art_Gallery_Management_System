import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

from artist.add_art import add_art
from artist.view_sold_art import view_sold_art

from customer.view_available_art import view_available_art
from customer.buy_art import buy_art
from customer.view_purchased_art import view_purchased_art
from customer.buy_costliest import buy_costliest
from customer.scrap_art import scrap_art

st.title("PES University")
st.header("Art Gallery Management")

is_login = False # Variable to check if the user has logged in
with open('users.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    with open('users.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    user_type = config['credentials']['usernames'].get(username, {}).get('type', None)
    is_login = True
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')


# User priviledges on frontend after login for Artist
if is_login and user_type=='Artist':
    id = config['credentials']['usernames'].get(username, {}).get('id', None)
    menu = ["Dashboard", "Add-Art","View Sold Art"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice=="Dashboard":
        st.subheader(f'Welcome *{name} ({user_type})*')
        authenticator.logout('Logout', 'main')
    elif choice == "Add-Art":
        st.subheader("Add-Art")
        add_art(id)
    elif choice == "View Sold Art":
        st.subheader("View Sold Art")
        view_sold_art(id)
    else:
        st.subheader("Select a valid option")

# User priviledges on frontend after login for Customer
if is_login and user_type=='Customer':
    id = config['credentials']['usernames'].get(username, {}).get('id', None)
    menu = ["Dashboard", "Buy-Art", "Buy Costliest","View Purchased Art"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice=="Dashboard":
        st.subheader(f'Welcome *{name} ({user_type})*')
        authenticator.logout('Logout', 'main')
    elif choice == "Buy-Art":
        st.subheader("Available Arts:")
        view_available_art()
        st.subheader("Buy Art:")
        buy_art(id)
    elif choice == "View Purchased Art":
        st.subheader("View Purchased Art")
        view_purchased_art(id)
        scrap_art(id)
    elif choice == "Buy Costliest":
        st.subheader("Buy Costliest Art")
        buy_costliest(id)
    else:
        st.subheader("Select a valid option")