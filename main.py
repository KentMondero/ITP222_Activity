import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Streamlit Elements Demo", layout="centered")

# Sidebar menu
menu = st.sidebar.selectbox(
    "Navigation",
    ["Home", "Text & Markdown", "Inputs", "Buttons", "Data Display", "Charts", "About"]
)

# ---------------- HOME ----------------
if menu == "Home":
    st.title("Streamlit Elements Demo App")
    st.write("Welcome! This app showcases different Streamlit elements using the Streamlit API Reference.")
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=200)
    st.success("Use the sidebar to explore different Streamlit components.")

# ---------------- TEXT & MARKDOWN ----------------
elif menu == "Text & Markdown":
    st.header("Text & Markdown")
    st.text("This is st.text()")
    st.write("This is st.write()")
    st.markdown("**This is bold text using Markdown**")
    st.markdown("*This is italic text*")
    st.markdown("### This is a subheading")
    st.code("print('Hello Streamlit')", language="python")

# ---------------- INPUTS ----------------
elif menu == "Inputs":
    st.header("Input Widgets")

    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0, max_value=120)
    agree = st.checkbox("I agree")
    gender = st.radio("Select gender:", ["Male", "Female", "Other"])
    hobby = st.selectbox("Choose a hobby:", ["Reading", "Sports", "Gaming", "Music"])
    level = st.slider("Select level:", 1, 10)

    if name:
        st.write(f"Hello, {name}!")
    st.write("Age:", age)
    st.write("Agreement:", agree)
    st.write("Gender:", gender)
    st.write("Hobby:", hobby)
    st.write("Level:", level)

# ---------------- BUTTONS ----------------
elif menu == "Buttons":
    st.header("Buttons & Status")

    if st.button("Click me"):
        st.success("Button clicked!")

    with st.spinner("Loading..."):
        time.sleep(1)

    st.progress(70)
    st.toast("This is a toast notification!")

# ---------------- DATA DISPLAY ----------------
elif menu == "Data Display":
    st.header("Data Display")

    df = pd.DataFrame({
        "Name": ["Ana", "Ben", "Cara", "Dan"],
        "Score": [85, 90, 78, 92]
    })

    st.write("DataFrame using st.dataframe():")
    st.dataframe(df)

    st.write("Table using st.table():")
    st.table(df)

    st.json({
        "name": "Kent",
        "course": "ICS",
        "year": 2
    })

# ---------------- CHARTS ----------------
elif menu == "Charts":
    st.header("Charts")

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["A", "B", "C"]
    )

    st.line_chart(chart_data)
    st.bar_chart(chart_data)
    st.area_chart(chart_data)

# ---------------- ABOUT ----------------
elif menu == "About":
    st.title("About")
    st.write("""
    This application demonstrates various Streamlit elements using:
    https://docs.streamlit.io/develop/api-reference

    Sidebar Panels:
    1. Home  
    2. Text & Markdown  
    3. Inputs  
    4. Buttons  
    5. Data Display  
    6. Charts  
    7. About  

    Created for learning Streamlit components.
    """)