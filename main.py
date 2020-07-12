# main.py
# entry point

import streamlit as st

def main():
    from pycaret.utils import __version__
    msg = str(__version__()) + ' succesfully loaded.' 
    st.success(msg)

if __name__ == '__main__':
    main()
