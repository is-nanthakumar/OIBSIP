from unittest.mock import patch

from src.speech.text_to_speech import TextToSpeech


def test_speak_text():
    tts = TextToSpeech()

    with patch(
        "src.speech.text_to_speech.subprocess.run"
    ) as mock_run:

        tts.speak("Hello world")

        mock_run.assert_called_once()

        args = mock_run.call_args.args[0]

        assert args[0] == "powershell"
        assert args[1] == "-NoProfile"
        assert args[2] == "-NonInteractive"
        assert args[3] == "-Command"

        command = args[4]

        assert "System.Speech.Synthesis.SpeechSynthesizer" in command
        assert "$synth.Speak('Hello world')" in command
        assert "$synth.Dispose()" in command


def test_speak_empty_text():
    tts = TextToSpeech()

    with patch(
        "src.speech.text_to_speech.subprocess.run"
    ) as mock_run:

        tts.speak("")

        mock_run.assert_not_called()


def test_stop():
    tts = TextToSpeech()

    tts.stop()