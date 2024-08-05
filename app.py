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

r = requests.get(f'https://docs.google.com/spreadsheets/d/1UZRV_O-E21TwKWXlD_7aFralTYvJvK2Gvcp2nxopq9A&output=csv')
open('dataset.csv', 'wb').write(r.content)
feedback_df = pd.read_csv('dataset.csv')

def show_user_info(user):
    with st.expander('User Information'):
        st.success(f'🎉 Logged in as: {user["email"]}')
        if 'full_name' in user.get("user_metadata", {}):
            st.write(f'Username: {user["user_metadata"]["full_name"]}')


def main():
    st.title('Streamlit Supabase 🔒')

if __name__ == '__main__':
    main()
