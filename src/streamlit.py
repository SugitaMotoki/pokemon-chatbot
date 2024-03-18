import streamlit as st
import pandas as pd
from set_api_key import set_api_key


def main():
  df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
  })
  st.write()
  


if __name__ == "__main__":
    set_api_key()
    main()

