from cgitb import text
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

import streamlit as st
from streamlit_option_menu import option_menu

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Ilyas God", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_87edm6kj.json")
img_contact_form = Image.open("images/cont.jpg")
img_lottie_animation = Image.open("images/hack.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Ilyas :wave:")
    st.title("A Highschool Student From SMK Galileo Indonesia")
    st.write("I am very passionate about learning Programming and Hacking, and always find out about many things on the internet.")
    st.write("[Subscribe my Youtube Channel >](https://www.youtube.com/c/Ilyassamz15)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On My Daily Life I Spent My Time For:
            - I spent my time for Playing a Game with My Online Friends, and we talk so much on Discord if we playing a Game together.
            - And I spent my time for watching Anime and Movie, but up to my mood sometimes if my mood is good, i can watching Anime full day (24 hours).
            - I like self-taught, even though I'm a game maniac and watch anime but I also like to learn a lot of things myself on the Internet, especially IT related.
            - The maybe I spent my time just for.. hmm i don't know because there is nothing interesting in my daily life lol, I just always repeat the activities of the previous activities.
            If u want add My Social Media just click the link bellow:
            """
        )

        st.write("[Tiktok >](https://www.tiktok.com/@kidskids1515/)")
        st.write("[Facebook >](https://www.facebook.com/ilyas.cwan.yasboy/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("THE PROJECT STILL UNDER PROGRESS")
        st.write(
            """
            COMING SOON COMING SOON COMING SOON COMING SOON COMING SOON
            COMING SOON COMING SOON COMING SOON COMING SOON COMING SOON
            COMING SOON COMING SOON COMING SOON COMING SOON COMING SOON
            """
        )
        st.markdown("[COMING SOON...]")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("THE PROJECT STILL UNDER PROGRESS")
        st.write(
            """
            COMING SOON COMING SOON COMING SOON COMING SOON COMING SOON
            COMING SOON COMING SOON COMING SOON COMING SOON COMING SOON
            COMING SOON COMING SOON COMING SOON COMING SOON COMING SOON
            """
        )
        st.markdown("[COMING SOON...]")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/yzvoldigoad27@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()