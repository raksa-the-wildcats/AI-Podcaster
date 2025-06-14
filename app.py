import os
import re
import numpy as np
import soundfile as sf
import gradio as gr
from kokoro import KPipeline
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

# Create audios directory if it doesn't exist
audios_directory = 'audios/'
os.makedirs(audios_directory, exist_ok=True)

supported_languages = {
    '🇺🇸 American English': 'a',
    '🇬🇧 British English': 'b',
    '🇪🇸 Spanish': 'e',
    '🇫🇷 French': 'f',
    '🇮🇳 Hindi': 'h',
    '🇮🇹 Italian': 'i',
    '🇯🇵 Japanese': 'j',
    '🇧🇷 Brazilian Portuguese': 'p',
    '🇨🇳 Mandarin Chinese': 'z'
}

summary_template = """
Summarize the following text by highlighting the key points. 
Maintain a conversational tone and keep the summary easy to follow for a general audience.
Text: {text}
"""

model = ChatOllama(model="qwen2.5:8b")

def generate_audio(pipeline, text):
    # Clean up old files
    for file in os.listdir(audios_directory):
        if file.endswith('.wav'):
            os.remove(os.path.join(audios_directory, file))

    generator = pipeline(text, voice='af_heart')
    chunks = []

    for i, (gs, ps, audio) in enumerate(generator):
        chunks.append(audio)

    file_name = 'audio.wav'
    full_audio = np.concatenate(chunks, axis=0)
    file_path = os.path.join(audios_directory, file_name)
    sf.write(file_path, full_audio, 24000)

    return file_path

def summarize_text(text):
    prompt = ChatPromptTemplate.from_template(summary_template)
    chain = prompt | model

    summary = chain.invoke({"text": text})
    return clean_text(summary.content)

def clean_text(text):
    # Fixed the syntax error in the original code
    clean_text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    return clean_text.strip()

def process_text_to_audio(language, text, should_summarize):
    if not text.strip():
        return None, "Please enter some text to generate audio."
    
    try:
        # Initialize pipeline with selected language
        pipeline = KPipeline(lang_code=supported_languages[language])
        
        # Summarize if requested
        processed_text = text
        if should_summarize:
            processed_text = summarize_text(text)
            
        # Generate audio
        audio_file = generate_audio(pipeline, processed_text)
        
        return audio_file, f"Audio generated successfully! {'(Summarized text used)' if should_summarize else ''}"
        
    except Exception as e:
        return None, f"Error: {str(e)}"

# Create Gradio interface
with gr.Blocks(title="AI Podcaster") as app:
    gr.Markdown("# 🎙️ AI Podcaster")
    gr.Markdown("Convert text to speech with optional AI summarization")
    
    with gr.Row():
        with gr.Column():
            language_dropdown = gr.Dropdown(
                choices=list(supported_languages.keys()),
                value=list(supported_languages.keys())[0],
                label="Select Language"
            )
            
            text_input = gr.Textbox(
                lines=10,
                placeholder="Enter your text here...",
                label="Text Input"
            )
            
            summarize_checkbox = gr.Checkbox(
                label="Summarize text before generating audio",
                value=False
            )
            
            generate_btn = gr.Button("🎵 Generate Audio", variant="primary")
        
        with gr.Column():
            audio_output = gr.Audio(label="Generated Audio", type="filepath")
            status_text = gr.Textbox(label="Status", interactive=False)
    
    generate_btn.click(
        fn=process_text_to_audio,
        inputs=[language_dropdown, text_input, summarize_checkbox],
        outputs=[audio_output, status_text]
    )

if __name__ == "__main__":
    app.launch(share=True, debug=True)