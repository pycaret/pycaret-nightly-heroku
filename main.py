# main.py
# entry point

import streamlit as st

def main():
    from pycaret.utils import version
    ver = version()
    st.sidebar.success(ver + ' succesfully loaded.')

if __name__ == '__main__':
    main()