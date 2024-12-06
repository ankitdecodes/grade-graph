import streamlit as st

st.set_page_config(page_title="GradeGraph", page_icon="📊")

# Add a larger emoji above and below the name in the sidebar using HTML and CSS
st.sidebar.markdown('<div style="text-align: center;"><span style="font-size: 10.5rem;">📊</span></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div style="text-align: center;"><span style="font-size: 2.5rem;">GradeGraph</span></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div style="text-align: center;"><span style="font-size: 1.5rem;">"Developed by Data Science Students"</span></div>', unsafe_allow_html=True)
st.title("🤝About Us")


st.write(
        "GradeGraph is an academic performance visualization platform designed to empower students, educators, and institutions by providing a data-driven approach to education."
    )

st.write(
        "We offer a user-friendly interface that allows you to analyze and visualize student academic performance data, offering valuable insights into trends, progress, and areas for improvement."
    )

st.write(
        "With GradeGraph, you can make informed decisions to enhance your academic journey."
    )


# Footer
st.markdown('<div style="text-align: center;">© 2023 GradeGraph</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;">For more information Follow us on <a href="https://github.com/ankitdecodes/grade-graph">GitHub</a></div>', unsafe_allow_html=True)
