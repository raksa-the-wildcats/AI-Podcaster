# 🎙️ AI Podcaster

A powerful text-to-speech application that converts text into natural-sounding audio with optional AI-powered summarization. Built with Python, featuring support for multiple languages and voices.

## ✨ Features

- **Multi-language TTS**: Support for 9 languages including English, Spanish, French, Hindi, Japanese, and more
- **AI Summarization**: Automatically summarize long texts before converting to speech
- **High-Quality Audio**: 24kHz audio output using Kokoro TTS engine
- **User-Friendly Interface**: Available in both Streamlit and Gradio versions
- **Local Processing**: Runs entirely on your machine for privacy

## 🌍 Supported Languages

- 🇺🇸 American English
- 🇬🇧 British English  
- 🇪🇸 Spanish
- 🇫🇷 French
- 🇮🇳 Hindi
- 🇮🇹 Italian
- 🇯🇵 Japanese
- 🇧🇷 Brazilian Portuguese
- 🇨🇳 Mandarin Chinese

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+** installed on your system
2. **Ollama** installed and running ([Download here](https://ollama.ai))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-podcaster.git
   cd ai-podcaster
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install and setup Ollama model**
   ```bash
   # Install Ollama if you haven't already
   # Then pull the required model
   ollama pull qwen2.5:8b
   ```

4. **Create audio output directory**
   ```bash
   mkdir audios
   ```

### Running the Application

#### Streamlit Version
```bash
streamlit run app.py
```

#### Gradio Version  
```bash
python app_gradio.py
```

The application will open in your default web browser.

## 📖 Usage

1. **Select Language**: Choose your preferred language from the dropdown
2. **Enter Text**: Paste or type the text you want to convert to speech
3. **Optional Summarization**: Check the "Summarize text" option to automatically summarize long content
4. **Generate Audio**: Click the generate button and wait for processing
5. **Listen**: Play the generated audio directly in the browser

## 🛠️ Technical Details

### Architecture
- **Frontend**: Streamlit or Gradio web interface
- **TTS Engine**: Kokoro for high-quality speech synthesis
- **AI Model**: Qwen 2.5 (8B) via Ollama for text summarization
- **Audio Processing**: NumPy and SoundFile for audio manipulation

### File Structure
```
ai-podcaster/
├── app.py                 # Streamlit version
├── app_gradio.py          # Gradio version
├── requirements.txt       # Python dependencies
├── audios/               # Generated audio files
└── README.md             # This file
```

## 🔧 Configuration

### Changing the Voice
Modify the `voice` parameter in the `generate_audio` function:
```python
generator = pipeline(text, voice='af_heart')  # Change 'af_heart' to desired voice
```

### Switching AI Models
Update the model name in the initialization:
```python
model = ChatOllama(model="qwen2.5:8b")  # Try different Ollama models
```

### Audio Settings
Adjust sample rate and audio quality:
```python
sf.write(file_path, full_audio, 24000)  # Change 24000 to desired sample rate
```

## 🐛 Troubleshooting

### Common Issues

**Ollama Connection Error**
- Ensure Ollama is installed and running
- Verify the model is downloaded: `ollama list`
- Check if Ollama service is running: `ollama serve`

**Audio Generation Failed**
- Verify all dependencies are installed
- Check if the `audios/` directory exists and has write permissions
- Ensure sufficient disk space for audio files

**Model Loading Issues**
- Try pulling the model again: `ollama pull qwen2.5:8b`
- Check available models: `ollama list`
- Restart Ollama service

### Performance Tips

- Use shorter texts for faster processing
- Enable summarization for very long content
- Close other resource-intensive applications
- Consider using a smaller Ollama model for faster summarization

## 📦 Dependencies

- `streamlit` - Web interface framework
- `gradio` - Alternative web interface
- `langchain_core` - LLM orchestration
- `langchain_ollama` - Ollama integration
- `kokoro` - Text-to-speech engine
- `soundfile` - Audio file handling
- `numpy` - Numerical computations

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Kokoro TTS](https://github.com/hexgrad/kokoro) for the excellent text-to-speech engine
- [Ollama](https://ollama.ai) for making local LLM deployment simple
- [LangChain](https://langchain.com) for LLM orchestration tools

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/ai-podcaster/issues) page
2. Create a new issue with detailed information
3. Join our community discussions

---

⭐ **If you found this project helpful, please give it a star!** ⭐