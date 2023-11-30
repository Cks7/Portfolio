# main.py

import streamlit as st
import pandas as pd

# Sample data for projects
projects_data = {
    "Project Name": ["1.Email Spam Classifier", "2.AI Based Trip Planner"],
    "Description": [
        "Description: In this project, I developed an advanced Email Spam Classifier using Natural Language Processing (NLP) techniques. The primary goal was to create a robust and efficient system capable of automatically analyzing incoming emails and accurately classifying them as either spam or ham (non-spam).",
        "Description: In creating an AI-based Tour Guide for Pune, we collected comprehensive data from Google Maps, Zomato, and MakeMyTrip APIs, conducted thorough data cleaning and exploratory data analysis (EDA), merged datasets using location coordinates, employed KNN for proximity analysis, and implemented collaborative and content-based filtering for effective recommendations. The results were integrated into a streamlined UI using Streamlit, offering users personalized suggestions for nearby place",
    ],
    "Link": ["https://github.com/Cks7/sms-spam-classifier", "https://github.com/Cks7/TripPlanner"],
    "Weblink":["No link","https://tripplanner-a8gz2txa6kzguqdajsmn7j.streamlit.app/"]
}

projects_df = pd.DataFrame(projects_data)

# Sample data for skills
skills_data = {
    "Skill": ["C and C++", "Team Work", "Python", "Good Listener", "Machine Learning", "Tableau", "MySQL","Data Analysis","Dart","Frontend"],

}

skills_df = pd.DataFrame(skills_data)
experience_data = {
    "Position": ["Software Intern"],
    "Company": ["HumInspAiRe"],
    "Duration": ["06/04/23 - Current"],
    "Description": [

        "Working on software development projects at HumInspAiRe.",
    ],
    "Acceptance Letter": [
        "https://drive.google.com/drive/u/2/my-drive",
    ],
}
experience_df = pd.DataFrame(experience_data)
# Sample education data
education_data = {
    "Degree": ["Secondary State Board", "Higher Secondary State Board", "BTECH - Artificial Intelligence and Data Science"],
    "Institution": ["Kamlabai Girl's High School, Dhule", "S.V.V.P.S College, Dhule", "Vishwakarma Institute of Information Technology, Pune"],
    "Percentage/GPA": ["95.20%, 2019", "89.8%, 2021", "GPA: 9.30 (Second Year Completed)"],
    "Year": ["2019", "2021", "2021-2025"],
}

education_df = pd.DataFrame(education_data)

# Sample profile information
profile_info = """
Passionate and motivated student pursuing a degree in Artificial Intelligence and Data Science.
With good logical thinking and technical skills, I want to grab a good internship and gain knowledge and experience by working on more projects.
"""

# Sample contact information
contact_info = "My mail I'D: chetanaks777@gmail.com  \nMy LinkedIn Profile: [LinkedIn](https://www.linkedin.com/in/chetana-shinde-382731229/)  \nGithub Profile: [GitHub](https://github.com/Cks7)"






# Sample certificates
certificates_info = {
    "Certificate Name": ["CISCO Computer Network", "Machine Learning Specialization", "Machine Learning Maths"],
    "Certificate Link": ["https://drive.google.com/file/d/1OfNR3Rj_tD1gV1tCCd5luP53SmxE_CvT/view?usp=sharing", "https://coursera.org/share/9a8f691fcb16cbb2f2ec866a346c71be", "https://coursera.org/share/ba8a25f24db02d10f89abd7e522f14d5"]
}

certificate_df = pd.DataFrame(certificates_info)
def main():
    # Set page config at the beginning
    st.set_page_config(
        page_title="Chetana's Portfolio",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
    )

    # Custom CSS styles
    st.markdown(
        """
        <style>
            body {
                margin: 0;
                font-family: 'Arial', sans-serif;
                background-color: #f8f8f8;
                color: #333333; /* Default text color */
            }
            .navbar {
                overflow: hidden;
                background-color: #0f1115;
                padding: 20px;
                position: fixed;
                width: 1380px;
                top: 30px;
                z-index: 1000;
                
            }
            .navbar a {
                float: left;
                
                display: block;
                color: #f2f2f2;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
            }
            .navbar a:hover {
                background-color: #ddd;
                color: black;
            }
             section {
            padding: 40px;
            margin: 80px 0 0;  /* Add margin to the top */
            border-radius: 10px;
        }
            section.projects {
                background-color: #0f1115; /* Projects section background color */
                color: #1f4b6e; /* Projects section text color */
            }
            section.skills {
                background-color: #0f1115; /* Skills section background color */
                color: #333333; /* Skills section text color */
            }
            section.welcome {
                background-color: #0f1115; /* Welcome section background color */
                color: #000000; /* Welcome section text color */
            }
            section.about {
                background-color: #0f1115; /* About Me section background color */
                color: #4f6128; /* About Me section text color */
            }
            section.contact {
                background-color: #0f1115; /* Contact section background color */
                color: #008080; /* Contact section text color */
            }
            section.experience {
                background-color: #0f1115; /* Contact section background color */
                color: #008080; /* Contact section text color */
            }
            section.education {
                background-color: #0f1115; /* Education section background color */
                color: #9f6000; /* Education section text color */
            }
            section.certificates {
                background-color: #0f1115; /* Certificates section background color */
                color: #6a1b9a; /* Certificates section text color */
            }
            h2 {
                color: #1f4b6e;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Navigation Bar
    st.markdown(
        """
        <div class="navbar">
            <a href="#projects">Projects</a>
            <a href="#experience">Experience</a>
            <a href="#skills">Skills</a>
            <a href="#education">Education</a>
            <a href="#certificates">Certificates</a>
            <a href="#contact">Contact</a>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # Welcome Section
    show_welcome()

    # Projects Section

    show_projects()

    show_experience()

    # Skills Section

    show_skills()


    show_education()

    # Certificates Section

    show_certificates()


    # Contact Section

    show_contact()

    # Education Section


def show_projects():
    st.markdown("<section class='projects' id='projects'><h2>Projects</h2></section>", unsafe_allow_html=True)
    # Define the columns
    col1, col2 = st.columns(2)

    # Column 1: Projects Data
    for index, row in projects_df.iterrows():
        col1.write(f"**Name:** {row['Project Name']}")
        col1.write(f"**Description:** {row['Description']}")
        col1.write(f"**Github Link:** {row['Link']}")
        col1.write(f"**Weblink:** {row['Weblink']}")

        # Add a separator between projects
        col1.markdown("---")


    # Column 2: Image or Gif
    gif_url = "https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif"  # Replace with your image or gif URL
    col2.image(gif_url, use_column_width=True)

def show_experience():
    st.markdown("<section class='experience' id='experience'><h2>Experience</h2></section>", unsafe_allow_html=True)

    for index, row in experience_df.iterrows():
        st.write(f"**Position:** {row['Position']}")
        st.write(f"**Company:** {row['Company']}")
        st.write(f"**Duration:** {row['Duration']}")
        st.write(f"**Description:** {row['Description']}")

        # If there is an acceptance letter link, display it
        if row['Acceptance Letter']:
            st.write(f"**Acceptance Letter:** [{row['Position']} Acceptance Letter]({row['Acceptance Letter']})")

        # Add a separator between experiences
        st.markdown("---")


def show_skills():
    st.markdown("<section class='skills' id='skills'><h2>Skills</h2></section>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])

    # Column 1: Image with custom spacing
    col1.markdown("""
        <div style="margin-right: 80px;">
            <img src="https://d1m75rqqgidzqn.cloudfront.net/wp-data/2019/09/11134058/What-is-data-science-2.jpg" width="100%" alt="Your Image Caption Here">
        </div>
    """, unsafe_allow_html=True)

    # Column 2: Text
    col2.dataframe(skills_df)




def show_education():
    st.markdown("<section class='education' id='education'><h2>Education</h2></section>", unsafe_allow_html=True)
    st.dataframe(education_df)

def show_certificates():
    st.markdown("<section class='certificates' id='certificates'><h2>Certificates</h2></section>", unsafe_allow_html=True)
    for index, row in certificate_df.iterrows():
        st.write(f"**Name:** {row['Certificate Name']}")
        st.write(f"**Link:** {row['Certificate Link']}")
        st.markdown("---")


def show_welcome():
    welcome_image = "https://img.freepik.com/free-vector/abstract-low-poly-connection-lines-digital-technology-background_1017-25550.jpg?w=1060&t=st=1701340700~exp=1701341300~hmac=57088c3c52e49beb4a143334b7bcc2374db86621f156072edc983acca3a8efc2"
    st.markdown(
        f"""
        <div style="position: relative;">
            <img src="{welcome_image}" style="width: 100%; border-radius: 10px;" alt="Welcome Image">
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; color: #ffffff;">
                <h3 >Hello! I am Chetana Shinde,<br> a passionate and motivated student pursuing a degree in Artificial Intelligence and Data Science.</h3>
                <p>With good logical thinking and technical skills, I aim to grab a good internship and gain knowledge and experience by working on more projects.</p>
                <p>Feel free to explore the sections below!</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def show_contact():
    st.markdown("<section class='contact' id='contact'><h2>Contact Me</h2></section>", unsafe_allow_html=True)
    st.write(contact_info)



if __name__ == "__main__":
    main()
