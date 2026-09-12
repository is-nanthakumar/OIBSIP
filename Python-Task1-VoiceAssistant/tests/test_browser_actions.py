from unittest.mock import patch

from src.actions.browser_actions import BrowserActions


def test_open_supported_website():
    actions = BrowserActions()

    with patch("src.actions.browser_actions.webbrowser.open") as mock_open:
        response = actions.open_website("youtube")

        mock_open.assert_called_once_with(
            "https://www.youtube.com"
        )

    assert response == "Opening youtube."


def test_open_unsupported_website():
    actions = BrowserActions()

    with patch("src.actions.browser_actions.webbrowser.open") as mock_open:
        response = actions.open_website("facebook")

        mock_open.assert_not_called()

    assert response == "I don't know how to open facebook."


def test_search_web():
    actions = BrowserActions()

    with patch("src.actions.browser_actions.webbrowser.open") as mock_open:
        response = actions.search_web("python tutorials")

        mock_open.assert_called_once_with(
            "https://www.google.com/search?q=python+tutorials"
        )

    assert response == "Searching the web for python tutorials."


def test_empty_search():
    actions = BrowserActions()

    with patch("src.actions.browser_actions.webbrowser.open") as mock_open:
        response = actions.search_web("")

        mock_open.assert_not_called()

    assert response == "Please tell me what you want me to search for."

def test_open_gmail():
    actions = BrowserActions()

    with patch("src.actions.browser_actions.webbrowser.open") as mock_open:
        response = actions.open_website("gmail")

        mock_open.assert_called_once_with(
            "https://mail.google.com"
        )

    assert response == "Opening gmail."


def test_open_github():
    actions = BrowserActions()

    with patch("src.actions.browser_actions.webbrowser.open") as mock_open:
        response = actions.open_website("github")

        mock_open.assert_called_once_with(
            "https://github.com"
        )

    assert response == "Opening github."


def test_open_linkedin():
    actions = BrowserActions()

    with patch("src.actions.browser_actions.webbrowser.open") as mock_open:
        response = actions.open_website("linkedin")

        mock_open.assert_called_once_with(
            "https://www.linkedin.com"
        )

    assert response == "Opening linkedin."


def test_open_whatsapp():
    actions = BrowserActions()

    with patch("src.actions.browser_actions.webbrowser.open") as mock_open:
        response = actions.open_website("whatsapp")

        mock_open.assert_called_once_with(
            "https://web.whatsapp.com"
        )

    assert response == "Opening whatsapp."    