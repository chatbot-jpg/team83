# EchoVerse Audiobook Creation System

import sys
from audio.generator import AudioGenerator
from voices.options import VoiceOptions
from tones.customizer import ToneCustomizer
from utils.helpers import read_text_file, validate_input

def main():
    print("Welcome to EchoVerse: Your Generative AI Audiobook Creator!")
    
    # Get user input for text or file upload
    user_input = input("Please enter the text you want to convert to audio or provide the file path: ")
    
    # Check if input is a file path
    if user_input.endswith('.txt'):
        text = read_text_file(user_input)
    else:
        text = user_input
    
    # Validate the input text
    if not validate_input(text):
        print("Invalid input. Please provide a valid text.")
        sys.exit(1)
    
    # Choose voice options
    voice_options = VoiceOptions()
    available_voices = voice_options.get_available_voices()
    print("Available voices:", available_voices)
    selected_voice = input("Select a voice from the above options: ")
    voice_options.set_voice(selected_voice)
    
    # Choose tone options
    tone_customizer = ToneCustomizer()
    tone = input("Enter the desired tone for the audiobook (e.g., happy, serious): ")
    
    # Customize the tone of the text
    customized_text = tone_customizer.customize_tone(text, tone)
    
    # Generate audio
    audio_generator = AudioGenerator()
    audio_generator.generate_audio(customized_text, tone)
    
    # Save the audio file
    output_file = input("Enter the output file path to save the audio (e.g., output.mp3): ")
    audio_generator.save_audio(output_file)
    
    print("Audiobook created successfully!")

if __name__ == "__main__":
    main()