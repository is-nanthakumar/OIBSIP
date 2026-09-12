from src.commands.command_processor import CommandProcessor
from src.speech.speech_recognizer import SpeechRecognizer
from src.speech.text_to_speech import TextToSpeech


class VoiceAssistant:
    """Coordinates speech recognition, command processing, and speech output."""

    def __init__(self):
        self.speech_recognizer = SpeechRecognizer()
        self.text_to_speech = TextToSpeech()
        self.command_processor = CommandProcessor(on_reminder=self._handle_reminder)


    def _handle_reminder(self, message: str) -> None:
        """Speak a reminder when its timer triggers."""

        print(f"Assistant: {message}")
        self.text_to_speech.speak(message)    

    def run(self) -> None:
        """Start the voice assistant main loop."""

        self.text_to_speech.speak(
            "Hello. Voice assistant started. How can I help you?"
        )

        failed_attempts = 0
        max_failed_attempts = 3

        while True:
            command = self.speech_recognizer.listen()

            if not command:
                failed_attempts += 1

                if failed_attempts >= max_failed_attempts:
                    message = (
                        "I am having trouble understanding you. "
                        "Please try again."
                    )

                    print(f"Assistant: {message}")
                    self.text_to_speech.speak(message)

                    failed_attempts = 0

                continue

            failed_attempts = 0

            response, should_exit = self.command_processor.process(command)

            print(f"Assistant: {response}")
            print(f"TTS text length:{len(response)}")   
            print("TTS: Speaking response...")          
            self.text_to_speech.speak(response)
            print("TTS: Response completed")

            if should_exit:
                break


if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()