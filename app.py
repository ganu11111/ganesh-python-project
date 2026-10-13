import streamlit as st

st.title("My Python Automation Project 🤖")

st.write("Welcome! This is my first AI project website.")

st.header("Client Report Generator")

client_name = st.text_input("Enter Client Name")
project_name = st.text_input("Enter Project Name")
status = st.selectbox(
    "Select Project Status",
    ["Pending", "In Progress", "Completed"]
)

if st.button("Generate Report"):
    report = f"""
    CLIENT PROJECT REPORT
    ---------------------
    Client Name: {client_name}
    Project Name: {project_name}
    Status: {status}
    """

    st.text(report)

    st.download_button(
        label="Download Report",
        data=report,
        file_name="client_report.txt",
        mime="text/plain"
    )
    