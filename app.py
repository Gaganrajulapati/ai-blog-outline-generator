import streamlit as st
import json
import time

from prompt import create_prompt
from model import generate_blog
from pdf_export import generate_pdf


# PAGE CONFIG
st.set_page_config(
    page_title="AI Blog Generator",
    page_icon="🧠",
    layout="wide"
)


# CUSTOM CSS
st.markdown("""

<style>

/* Main Background */
.stApp {
    background-color: #0E1117;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #1E1E2F;
}

/* Input boxes */
.stTextInput input {
    background-color: #262730;
    color: white;
    border-radius: 10px;
}

/* Buttons */
.stButton button {
    background: linear-gradient(90deg, #ff4b4b, #ff6b6b);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border: none;
}

/* Headers */
h1, h2, h3 {
    color: white;
}

/* Metric cards */
div[data-testid="metric-container"] {
    background-color: #1E1E2F;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #333;
}

</style>

""", unsafe_allow_html=True)


# TITLE
st.title("🧠 AI Blog Topic & Outline Generator")

st.markdown(
    "Generate professional SEO optimized blog titles and outlines using Generative AI"
)


# SIDEBAR
st.sidebar.header("⚙️ Blog Configuration")


# CATEGORY
category = st.sidebar.selectbox(

    "Select Blog Category",

    [
        "Technology",
        "Business",
        "Health",
        "Marketing",
        "Education",
        "Finance"
    ]
)


# TONE
tone = st.sidebar.selectbox(

    "Select Writing Tone",

    [
        "Professional",
        "Casual",
        "Technical",
        "Marketing",
        "Educational"
    ]
)


# LENGTH
length = st.sidebar.selectbox(

    "Select Blog Length",

    [
        "Short",
        "Medium",
        "Long"
    ]
)


# USER INPUT
topic = st.text_input("📌 Enter Blog Topic")

audience = st.text_input("🎯 Enter Target Audience")


# GENERATE BUTTON
if st.button("🚀 Generate Blog Outline"):

    if topic == "":

        st.warning("Please enter blog topic")

    else:

        with st.spinner("Generating AI Content..."):

            # PROGRESS BAR
            progress = st.progress(0)

            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)

            # CREATE PROMPT
            prompt = create_prompt(
                topic,
                audience,
                tone,
                length
            )

            # GENERATE OUTPUT
            result = generate_blog(prompt)

            # ERROR CHECK
            if "error" in result:

                st.error(result["error"])

            else:

                st.success("✅ Blog Generated Successfully!")

                # METRICS
                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "Outline Sections",
                    len(result["outline_sections"])
                )

                col2.metric(
                    "SEO Keywords",
                    len(result["seo_keywords"])
                )

                col3.metric(
                    "Tone",
                    tone
                )

                st.divider()

                # BLOG TITLE
                st.subheader("📰 Blog Title")

                st.write(result["blog_title"])


                # BLOG INTRODUCTION
                if "blog_intro" in result:

                    st.subheader("📝 Blog Introduction")

                    st.write(result["blog_intro"])


                # OUTLINE
                st.subheader("📚 Blog Outline")

                for section in result["outline_sections"]:

                    # IF AI RETURNS DICTIONARY
                    if isinstance(section, dict):

                        title = section.get("title", "Untitled Section")

                        description = section.get(
                            "description",
                            "No description available."
                        )

                        with st.expander(f"✅ {title}"):

                            st.write(description)

                    # IF AI RETURNS STRING
                    else:

                        with st.expander(f"✅ {section}"):

                            st.write(
                                f"Detailed content planning for section: {section}"
                            )


                # AUDIENCE
                st.subheader("🎯 Target Audience")

                st.write(result["target_audience"])


                # WRITING GOAL
                st.subheader("✍️ Writing Goal")

                st.write(result["writing_goal"])


                # SEO KEYWORDS
                st.subheader("🔍 SEO Keywords")

                for keyword in result["seo_keywords"]:

                    st.markdown(
                        f"""
                        <span style="
                        background-color:#ff4b4b;
                        padding:8px;
                        border-radius:10px;
                        margin:5px;
                        display:inline-block;
                        color:white;
                        ">
                        {keyword}
                        </span>
                        """,
                        unsafe_allow_html=True
                    )


                st.divider()


                # GENERATE PDF
                generate_pdf(result)


                # DOWNLOAD BUTTON
                with open("blog_outline.pdf", "rb") as file:

                    st.download_button(

                        label="📥 Download PDF",

                        data=file,

                        file_name="blog_outline.pdf",

                        mime="application/pdf"
                    )