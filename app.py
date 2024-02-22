from PIL import Image
import streamlit as st


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":winking_face: :smiling_face_with_hearts:", layout="wide")

#==================================================================
# LOAD ASSETS
gif_image_url = "/workspaces/Alastor/ezgif.com-animated-gif-maker.gif"
audio_file_url = "/workspaces/Alastor/spotifydown.com - Smile Like You Mean It (Alastor's Offer).mp3"
image_url = "/workspaces/Alastor/FEcj82VXMAQfwzl.png"


#==================================================================
# - HEADER SECTION
with st.container():
    st.subheader("Alastor’s Offer :wave:")
    # Option to toggle audio
    enable_audio = st.checkbox("Enable Audio", value=True)

# Display audio file as background music
    if enable_audio:
        st.audio(audio_file_url, format='audio/mp3', start_time=0)
st.title("Smile Like You Mean It")
st.write("Everything's better with a song, don't you agree?")

# Script
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Splendid, ha-ha-ho!\n
            I see big things coming your way, yes, indeedy!\n
            Now, onto business\n
            Everything's better with a song, don't you agree?
            """
        )
    with right_column:
        st.image(image_url, use_column_width=True)
        st.image(gif_image_url, use_column_width=True)
