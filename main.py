# main.py
# entry point

import streamlit as st

def main():
    from pycaret.utils import version
    msg = str(version()) + ' succesfully loaded.' 
    st.success(msg)

if __name__ == '__main__':
    main()
