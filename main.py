import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Jas Do It", layout="wide")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.sidebar.image("images/JasDoIt.png", width=70)  

menu = st.sidebar.selectbox( 
    "",
    ["Home", "Add Task", "Dashboard", "Feedback", "About"]
)


if menu == "Home":
    st.image("images/JasDoIt.png", width=100)
    st.title("Jas Do It ✔")
    st.header("When You Type Tasks, We Organize")

    st.image("images/managingTask.png", width=300)

    st.write("""
    This application helps users manage, organize, 
    and track tasks in a simple dashboard.
    """)
    
elif menu == "Add Task":
    st.title("Add New Task")
    with st.form("task_form"):

        task_name = st.text_input("Task Name")

        priority = st.selectbox(
            "Priority Level",
            ["Low", "Medium", "High"]
        )

        category = st.selectbox(
            "Category",
            ["School", "Work", "Personal", "Other"]
        )

        deadline = st.date_input(
            "Deadline",
            datetime.date.today()
        )

        description = st.text_area("Task Description")

        reminder = st.time_input("Reminder Time", value=None)

        important = st.checkbox("Mark as Important")

        submitted = st.form_submit_button("Add Task")

    if submitted:
        task = {
            "Task": task_name,
            "Priority": priority,
            "Category": category,
            "Deadline": deadline,
            "Important": important
        }

        st.session_state.tasks.append(task)

        st.success("Task added successfully!")
 
elif menu == "Dashboard":

    st.title("Dashboard")

    if st.session_state.tasks:

        st.subheader("Your Tasks")

        col1, col2, col3, col4 = st.columns([4,2,2,1])
        with col1:
            st.markdown("**Task**")
        with col2:
            st.markdown("**Priority**")
        with col3:
            st.markdown("**Deadline**")
        with col4:
            st.markdown("**Status**")

        st.divider()

        for i, task in enumerate(st.session_state.tasks):

            col1, col2, col3, col4 = st.columns([4,2,2,1])

            with col1:
                completed = st.checkbox(
                    task["Task"],
                    key=f"task_{i}"
                )

            with col2:
                st.write(task["Priority"])

            with col3:
                st.write(task["Deadline"])

            with col4:
                if completed:
                    st.success("Done")

        df = pd.DataFrame(st.session_state.tasks)

        st.divider()

        st.subheader("Task Distribution by Category")
        st.bar_chart(df["Category"].value_counts())

        st.divider()

        st.subheader("Priority Distribution")
        st.area_chart(df["Priority"].value_counts())

        completed_count = sum(
            st.session_state.get(f"task_{i}", False)
            for i in range(len(st.session_state.tasks))
        )

        progress = completed_count / len(st.session_state.tasks)

        st.subheader("Completion Progress")
        st.progress(progress)

        st.metric("Tasks Completed Today", "5", "+1")

        st.info("Tip: Break large tasks into smaller tasks to stay productive.")

    else:
        st.warning("No tasks added yet.")

elif menu == "Feedback":
    st.title("Send us your Feedback")

    rating = st.slider("Rate the app (10 being the highest and 1 being the lowest.)", 1, 10)
    
    recommendation = st.radio(
        "Would you recommend this app?",
        ["Yes", "Maybe", "No"]
    )

    comments = st.text_area("Additional comments")

    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")


elif menu == "About":
    st.title("About This App")

    st.markdown("""
    ### What the App Does
    Jas Do It is a simple to-do application aims to help users organize 
    daily activities by creating, prioritizing, and tracking tasks.

   It allows users to add tasks, set deadlines, prioritize activities, 
   and monitor productivity through a dashboard.

    ### Target Users
    - Students
    - Professionals
    - Anyone who wants to manage their tasks effectively.

    ### Inputs Collected
    - Task name
    - Priority level
    - Category
    - Deadline
    - Task description
    - Reminder time
    - Importance flag
    - User feedback

    ### Outputs Displayed
    - Task tables
    - Category and priority charts
    - Progress indicators
    - Task completion messages
    - Feedback responses

    ### Created By
    Kent Mondero  
    ICS-01-401A  
    """)