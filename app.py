import streamlit as st
import base64

# Set a background image

# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: url('dolphin-image.jpg');
#         background-size: cover;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

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

# set_background('dolphin-image.png')

st.image('owlcast-image.png')


# Title and introduction
st.title("The OwlCast")
st.write("OwlCast makes summarizing podcasts a hoot. Scroll down to see more content.")