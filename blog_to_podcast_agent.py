import os
from uuid import uuid4

import streamlit as st
from dotenv import load_dotenv

from agno.agent import Agent, RunResponse
from agno.models.ollama import Ollama
from agno.tools.crawl4ai import Crawl4aiTools
from elevenlabs.client import ElevenLabs

load_dotenv()
ELEVENLABS_KEY = os.getenv("ELEVEN_LABS_API_KEY")

st.set_page_config(page_title="📰➔🎙️ Blog to Podcast", page_icon="🎙️")
st.title("📰 ➡️ 🎙️ Blog to Podcast Agent")

url = st.text_input("Enter the Blog URL:", "")
generate = st.button("🎙️ Generate Podcast")

if generate:
    if not url.strip():
        st.warning("✏️ Please enter a blog URL first.")
        st.stop()

    if not ELEVENLABS_KEY:
        st.error("🔑 Missing ELEVEN_LABS_API_KEY in your .env")
        st.stop()

    with st.spinner("⏳ Scraping, summarizing, and generating audio..."):
        try:
            # Step 1: Run Agent to summarize blog
            agent = Agent(
                name="Blog to Podcast Agent",
                agent_id="blog_to_podcast_agent",
                model=Ollama(id="llama3.1:8b"),
                tools=[Crawl4aiTools(max_length=None)],
                description="Scrape and summarize in a conversational tone.",
                instructions=[
                    "When given a blog URL:",
                    "1. Scrape the blog content with Crawl4aiTools.",
                    "2. Summarize it in an engaging, conversational tone.",
                    "3. Return *only* the final summary text (no audio).",
                ],
                markdown=True,
                debug_mode=True,
            )

            run: RunResponse = agent.run(f"Convert the blog content to a podcast: {url}")
            summary = run.content.strip()

            if not summary:
                st.error("⚠️ Agent returned no summary. Try another URL.")
                st.stop()

            # Step 2: Convert full summary to audio (join stream)
            client = ElevenLabs(api_key=ELEVENLABS_KEY)
            audio_stream = client.text_to_speech.convert(
                text=summary,
                voice_id="JBFqnCBsd6RMkjVDRZzb",
                model_id="eleven_multilingual_v2",
                output_format="mp3_44100_128"
            )
            audio_bytes = b"".join(audio_stream)  # Join the generator output

            # Step 3: Save and display
            os.makedirs("audio_generations", exist_ok=True)
            file_path = f"audio_generations/podcast_{uuid4().hex}.mp3"
            with open(file_path, "wb") as f:
                f.write(audio_bytes)

            st.success("✅ Podcast generated successfully!")
            st.audio(audio_bytes, format="audio/mp3")
            st.download_button("⬇️ Download Podcast", data=audio_bytes, file_name="blog_podcast.mp3", mime="audio/mp3")

        except Exception as e:
            st.error(f"❌ Error: {e}")
