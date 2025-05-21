import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

# Sample data
data1 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Doe', 'Mary', 'Kate'],
    'Age': [28, 22, 30, 25, 33],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
})

data2 = pd.DataFrame({
    'Name': ['Mike', 'Emily', 'Tom', 'Ben', 'Alice'],
    'Age': [29, 27, 26, 31, 24],
    'City': ['Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
})

data3 = pd.DataFrame({
    'Name': ['Mark', 'Emma', 'Kumar', 'Dinesh', 'Liam'],
    'Age': [32, 23, 28, 29, 27],
    'City': ['Seattle', 'Boston', 'Atlanta', 'Denver', 'Miami']
})

# Initialize SessionState for managing state across re-runs
class SessionState:
    def __init__(self):
        self.selected_row_index = None

state = SessionState()

# Streamlit app
st.title('AgGrid with Sequential Display on Row Selection')

# Display AgGrid instances with row selection and sequential display
selected_row_index = AgGrid(data1,
                            theme='streamlit',
                            pagination=True,
                            editable=True,  # Enable row selection
                            height=250,
                            fit_columns_on_grid_load=True,
                            key='grid1')

if selected_row_index is not None:
    state.selected_row_index = selected_row_index

if state.selected_row_index is not None:
    if state.selected_row_index == 0:
        AgGrid(data1,
               theme='streamlit',
               pagination=True,
               editable=True,  # Enable row selection
               height=250,
               fit_columns_on_grid_load=True,
               key='grid1')
    elif state.selected_row_index == 1:
        AgGrid(data2,
               theme='streamlit',
               pagination=True,
               editable=True,  # Enable row selection
               height=250,
               fit_columns_on_grid_load=True,
               key='grid2')
    elif state.selected_row_index == 2:
        AgGrid(data3,
               theme='streamlit',
               pagination=True,
               editable=True,  # Enable row selection
               height=250,
               fit_columns_on_grid_load=True,
               key='grid3')
