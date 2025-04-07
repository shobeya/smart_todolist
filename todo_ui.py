import streamlit as st
from textblob import TextBlob

# Sample Task List
tasks = []

# Function to Assign Priority using NLP
def assign_priority(task):
    task_blob = TextBlob(task)
    if "urgent" in task.lower() or "today" in task.lower() or "important" in task.lower():
        return "High"
    elif "tomorrow" in task.lower() or "in 2 days" in task.lower():
        return "Medium"
    else:
        return "Low"

# UI Layout
st.title("AI-Powered Smart To-Do List")
st.write("Enter your task, and AI will assign priority!")

# Task Input
task_input = st.text_input("Enter your task:")

# When user enters a task, assign priority and add to list
if task_input:
    priority = assign_priority(task_input)
    tasks.append({"task": task_input, "priority": priority})

# Display Tasks
st.subheader("Your Prioritized Tasks:")
for task in sorted(tasks, key=lambda x: x["priority"], reverse=True):
    st.write(f"✅ {task['task']} | **Priority:** {task['priority']}")
