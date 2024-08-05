import streamlit as st
import streamlit.components.v1 as components
import os
from supabase import create_client
import pandas as pd
import requests
import docker
import subprocess
import platform
import distro
import uuid
from datetime import datetime

# Supabase setup
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
supabase = create_client(supabase_url, supabase_key)

#r = requests.get(f'https://docs.google.com/spreadsheets/d/1UZRV_O-E21TwKWXlD_7aFralTYvJvK2Gvcp2nxopq9A&output=csv')
#open('dataset.csv', 'wb').write(r.content)
#feedback_df = pd.read_csv('dataset.csv')

def show_login_signup_forms():
    col1, col2 = st.columns(2)
    with col1:
        with st.expander('Login 🔒'):
            email = st.text_input('Email', key='login_email')
            password = st.text_input('Password', type='password', key='login_password')
            login_btn = st.button('Login', on_click=login, args=(email, password))
    with col2:
        with st.expander('Sign Up 📝'):
            new_email = st.text_input('Email', key='signup_email')
            new_password = st.text_input('Password', type='password', key='signup_password')
            signup_btn = st.button('Sign Up', on_click=signup, args=(new_email, new_password))


def show_user_info(user):
    with st.expander('User Information'):
        st.success(f'🎉 Logged in as: {user["email"]}')
        if 'full_name' in user.get("user_metadata", {}):
            st.write(f'Username: {user["user_metadata"]["full_name"]}')


def main():
     show_login_signup_forms()
    st.title('Streamlit Supabase 🔒')

if __name__ == '__main__':
    main()
