class VoiceOptions:
    def __init__(self):
        self.available_voices = ["Voice 1", "Voice 2", "Voice 3"]  # Example voices
        self.selected_voice = self.available_voices[0]  # Default voice

    def get_available_voices(self):
        return self.available_voices

    def set_voice(self, voice: str):
        if voice in self.available_voices:
            self.selected_voice = voice
        else:
            raise ValueError(f"Voice '{voice}' is not available.")