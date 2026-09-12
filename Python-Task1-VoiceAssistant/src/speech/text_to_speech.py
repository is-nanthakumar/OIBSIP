import subprocess


class TextToSpeech:
    """Handles converting text responses into spoken audio on Windows."""

    def __init__(self, rate: int = 175, volume: float = 1.0):
        self.rate = rate
        self.volume = volume

    def speak(self, text: str) -> None:
        """Speak the given text using Windows native speech synthesis."""

        if not text:
            return

        windows_rate = max(
            -10,
            min(10, round((self.rate - 175) / 15))
        )

        windows_volume = max(
            0,
            min(100, round(self.volume * 100))
        )

        safe_text = text.replace("'", "''")

        powershell_command = (
            "Add-Type -AssemblyName System.Speech; "
            "$synth = New-Object "
            "System.Speech.Synthesis.SpeechSynthesizer; "
            f"$synth.Rate = {windows_rate}; "
            f"$synth.Volume = {windows_volume}; "
            f"$synth.Speak('{safe_text}'); "
            "$synth.Dispose()"
        )

        try:
            subprocess.run(
                [
                    "powershell",
                    "-NoProfile",
                    "-NonInteractive",
                    "-Command",
                    powershell_command,
                ],
                check=False,
                creationflags=subprocess.CREATE_NO_WINDOW,
            )
        except Exception as error:
            print(f"TTS error: {error}")

    def stop(self) -> None:
        """Stop the current speech process if possible."""

        pass