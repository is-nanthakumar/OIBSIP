from unittest.mock import MagicMock, patch

import speech_recognition as sr

from src.speech.speech_recognizer import SpeechRecognizer


def test_listen_returns_recognized_text():
    recognizer = SpeechRecognizer()

    fake_audio = MagicMock()

    with patch(
        "src.speech.speech_recognizer.sr.Microphone"
    ) as mock_microphone:
        mock_source = mock_microphone.return_value.__enter__.return_value

        with patch.object(
            recognizer.recognizer,
            "listen",
            return_value=fake_audio,
        ), patch.object(
            recognizer.recognizer,
            "adjust_for_ambient_noise"
        ), patch.object(
            recognizer.recognizer,
            "recognize_google",
            return_value="Open Calculator",
        ):
            result = recognizer.listen()

    assert result == "open calculator"


def test_listen_returns_empty_on_timeout():
    recognizer = SpeechRecognizer()

    with patch(
        "src.speech.speech_recognizer.sr.Microphone"
    ) as mock_microphone:
        mock_microphone.return_value.__enter__.return_value = MagicMock()

        with patch.object(
            recognizer.recognizer,
            "adjust_for_ambient_noise"
        ), patch.object(
            recognizer.recognizer,
            "listen",
            side_effect=sr.WaitTimeoutError(),
        ):
            result = recognizer.listen()

    assert result == ""


def test_listen_returns_empty_on_unknown_value():
    recognizer = SpeechRecognizer()

    fake_audio = MagicMock()

    with patch(
        "src.speech.speech_recognizer.sr.Microphone"
    ) as mock_microphone:
        mock_microphone.return_value.__enter__.return_value = MagicMock()

        with patch.object(
            recognizer.recognizer,
            "adjust_for_ambient_noise"
        ), patch.object(
            recognizer.recognizer,
            "listen",
            return_value=fake_audio,
        ), patch.object(
            recognizer.recognizer,
            "recognize_google",
            side_effect=sr.UnknownValueError(),
        ):
            result = recognizer.listen()

    assert result == ""


def test_listen_returns_empty_on_request_error():
    recognizer = SpeechRecognizer()

    fake_audio = MagicMock()

    with patch(
        "src.speech.speech_recognizer.sr.Microphone"
    ) as mock_microphone:
        mock_microphone.return_value._enter_.return_value = MagicMock()

        with patch.object(
            recognizer.recognizer,
            "adjust_for_ambient_noise"
        ), patch.object(
            recognizer.recognizer,
            "listen",
            return_value=fake_audio,
        ), patch.object(
            recognizer.recognizer,
            "recognize_google",
            side_effect=sr.RequestError("network error"),
        ):
            result = recognizer.listen()

    assert result == ""