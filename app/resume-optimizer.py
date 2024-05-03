import streamlit as st

# Resume Sections
sections = ["Education", "Experience", "Projects", "Skills"]

# Function to display section content
def display_section(section):
    st.header(section)
    if section == "Education":
        st.subheader("Add your education details here:")
        # Education input fields
        with st.form(key="education_form"):
            degree = st.text_input("Degree", "")
            major = st.text_input("Major", "")
            university = st.text_input("University", "")
            graduation_year = st.number_input("Graduation Year", min_value=1900, max_value=2100)
            st.form_submit_button("Add Education")
        # Display education details
        if degree and major and university and graduation_year:
            st.write(f"- {degree} in {major}, {university}, {graduation_year}")

    elif section == "Experience":
        st.subheader("Add your work experience here:")
        # Experience input fields
        with st.form(key="experience_form"):
            company = st.text_input("Company", "")
            position = st.text_input("Position", "")
            start_year = st.number_input("Start Year", min_value=1900, max_value=2100)
            end_year = st.number_input("End Year", min_value=1900, max_value=2100)
            st.form_submit_button("Add Experience")
        # Display experience details
        if company and position and start_year and end_year:
            st.write(f"- {position} at {company} ({start_year}-{end_year})")

    elif section == "Projects":
        st.subheader("Add your projects here:")
        # Projects input fields
        with st.form(key="projects_form"):
            project_name = st.text_input("Project Name", "")
            project_description = st.text_area("Project Description", "")
            st.form_submit_button("Add Project")
        # Display project details
        if project_name and project_description:
            st.write(f"- {project_name}: {project_description}")

    elif section == "Skills":
        st.subheader("Add your skills here:")
        # Skills input field
        with st.form(key="skills_form"):
            skills = st.text_area("Skills (comma-separated)", "")
            st.form_submit_button("Add Skills")
        # Display skills
        if skills:
            skills_list = [skill.strip() for skill in skills.split(",")]
            st.write(", ".join(skills_list))

# Sidebar - User Profile
st.sidebar.title("User Profile")
name = st.sidebar.text_input("Name", "")
email = st.sidebar.text_input("Email", "")
phone = st.sidebar.text_input("Phone", "")

# Display resume sections
if name and email and phone:
    st.title("Resume")
    st.write(f"Name: {name}")
    st.write(f"Email: {email}")
    st.write(f"Phone: {phone}")
    
    for section in sections:
        display_section(section)
else:
    st.warning("Please fill in your name, email, and phone number in the sidebar.")
