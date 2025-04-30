# 📰 ➡️ 🎙️ Blog to Podcast Agent

Convert any blog post into a narrated podcast using AI.

---

## 🔍 Overview
**Blog to Podcast Agent** is a Streamlit-based AI app that:
1. **Scrapes** blog content using Crawl4ai.
2. **Summarizes** it using a powerful Ollama LLM (LLaMA 3.1 8B).
3. **Generates natural-sounding audio** using the ElevenLabs API.
4. Streams the podcast directly in the browser and allows download as an MP3.

---

## 🚀 Features
- 🔗 Blog URL input
- 📄 Automatic scraping and summarization
- 🧠 LLaMA 3.1 summarization agent
- 🔊 High-quality speech via ElevenLabs
- 🎧 Stream and download podcast

---

## 🛠️ Setup

### 1. Clone this repo
```bash
git clone https://github.com/AkashR-16/Blog-To-Podast-Agent.git
cd Blog-To-Podast-Agent
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate   # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file:
```env
ELEVEN_LABS_API_KEY=your_elevenlabs_api_key_here
```

### 5. Run the app
```bash
streamlit run blog_to_podcast_agent.py
```

---

## 🧠 Tech Stack
- **Streamlit** – frontend UI
- **agno** – multi-agent orchestration
- **Ollama** – LLaMA 3.1 (8B) for summarization
- **Crawl4ai** – blog content scraper
- **ElevenLabs SDK** – realistic TTS (text-to-speech)

---

## 📁 Output
All generated podcasts are saved to:
```
audio_generations/
```
You can stream or download them directly via the app UI.

---

## 🗣️ Example Voices
- Voice ID used: `JBFqnCBsd6RMkjVDRZzb`
- Model: `eleven_multilingual_v2`

You can customize this in the code as needed.

---

## 📌 Notes
- Make sure you have a valid ElevenLabs API key with TTS access.
- Works cross-platform (tested on macOS).
- MP3 audio streamed using `st.audio()`.

---

## 📜 License
MIT License. Feel free to fork and enhance!


