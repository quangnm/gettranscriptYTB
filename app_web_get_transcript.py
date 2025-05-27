import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    return match.group(1) if match else None

st.title("🎬 YouTube Transcript Downloader")

url = st.text_input("Paste YouTube Link Here:")
if st.button("Get Transcript"):
    video_id = extract_video_id(url)
    if not video_id:
        st.error("Invalid URL.")
    else:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            output = "\n".join([f"{e['start']:.2f}s ({e['duration']:.2f}s): {e['text']}" for e in transcript])
            st.download_button("📄 Download Transcript", output, file_name="transcript.txt")
        except Exception as e:
            st.error(f"Error: {e}")
