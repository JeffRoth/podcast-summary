import streamlit as st
import base64

# Set a background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('dophin-image.jpg');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# def get_base64(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# def set_background(png_file):
#     bin_str = get_base64(png_file)
#     page_bg_img = '''
#     <style>
#     body {
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str
#     st.markdown(page_bg_img, unsafe_allow_html=True)

# set_background('dophin-image.png')


# Title and introduction
st.title("DolphinPod")
st.write("Dive into concise podcast summaries with DolphinPod. Scroll down to see more content.")