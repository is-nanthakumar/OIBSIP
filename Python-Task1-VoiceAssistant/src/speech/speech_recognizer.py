import speech_recognition as sr


class SpeechRecognizer:
    """Handles converting microphone audio into text."""

    def __init__(self, timeout: int = 5, phrase_time_limit: int = 8):
        self.recognizer = sr.Recognizer()
        self.timeout = timeout
        self.phrase_time_limit = phrase_time_limit
        self._calibrated = False

    def listen(self) -> str:
        """Listen through the microphone and return recognized text."""

        with sr.Microphone() as source:
            print("Listening...")

            if not self._calibrated:
                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )
                self._calibrated = True

            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=self.timeout,
                    phrase_time_limit=self.phrase_time_limit
                )
            except sr.WaitTimeoutError:
                print("No speech detected.")
                return ""

        try:
            print("Recognizing...")

            text = self.recognizer.recognize_google(audio)

            print(f"You said: {text}")
            return text.lower().strip()

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
            return ""

        except sr.RequestError as error:
            print(f"Speech recognition service error: {error}")
            return ""