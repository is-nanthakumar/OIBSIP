from unittest.mock import MagicMock, patch

from src.assistant import VoiceAssistant


def test_assistant_processes_command_and_speaks_response():
    with patch("src.assistant.SpeechRecognizer"), \
         patch("src.assistant.TextToSpeech"), \
         patch("src.assistant.CommandProcessor"):

        assistant = VoiceAssistant()

        assistant.speech_recognizer.listen.side_effect = [
            "hello",
            "exit",
        ]

        assistant.command_processor.process.side_effect = [
            ("Hello! How can I help you?", False),
            ("Goodbye. Shutting down the voice assistant.", True),
        ]

        assistant.run()

        assert assistant.command_processor.process.call_count == 2

        assistant.text_to_speech.speak.assert_any_call(
            "Hello! How can I help you?"
        )

        assistant.text_to_speech.speak.assert_any_call(
            "Goodbye. Shutting down the voice assistant."
        )


def test_assistant_retries_after_empty_commands():
    with patch("src.assistant.SpeechRecognizer"), \
         patch("src.assistant.TextToSpeech"), \
         patch("src.assistant.CommandProcessor"):

        assistant = VoiceAssistant()

        assistant.speech_recognizer.listen.side_effect = [
            "",
            "hello",
            "exit",
        ]

        assistant.command_processor.process.side_effect = [
            ("Hello! How can I help you?", False),
            ("Goodbye. Shutting down the voice assistant.", True),
        ]

        assistant.run()

        assert assistant.command_processor.process.call_count == 2


def test_assistant_reports_after_three_failed_attempts():
    with patch("src.assistant.SpeechRecognizer"), \
         patch("src.assistant.TextToSpeech"), \
         patch("src.assistant.CommandProcessor"):

        assistant = VoiceAssistant()

        assistant.speech_recognizer.listen.side_effect = [
            "",
            "",
            "",
            "exit",
        ]

        assistant.command_processor.process.return_value = (
            "Goodbye. Shutting down the voice assistant.",
            True,
        )

        assistant.run()

        assistant.text_to_speech.speak.assert_any_call(
            "I am having trouble understanding you. "
            "Please try again."
        )


def test_assistant_stops_when_processor_requests_exit():
    with patch("src.assistant.SpeechRecognizer"), \
         patch("src.assistant.TextToSpeech"), \
         patch("src.assistant.CommandProcessor"):

        assistant = VoiceAssistant()

        assistant.speech_recognizer.listen.return_value = "exit"

        assistant.command_processor.process.return_value = (
            "Goodbye. Shutting down the voice assistant.",
            True,
        )

        assistant.run()

        assistant.command_processor.process.assert_called_once_with(
            "exit"
        )