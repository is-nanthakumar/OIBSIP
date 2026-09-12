from datetime import datetime
from unittest.mock import patch

from src.actions.system_actions import SystemActions


def test_get_current_time():
    actions = SystemActions()

    with patch("src.actions.system_actions.datetime") as mock_datetime:
        mock_datetime.now.return_value.strftime.return_value = "02:30 PM"

        result = actions.get_current_time()

    assert result == "02:30 PM"


def test_get_current_date():
    actions = SystemActions()

    with patch("src.actions.system_actions.datetime") as mock_datetime:
        mock_datetime.now.return_value.strftime.return_value = (
            "Friday, 14 August 2026"
        )

        result = actions.get_current_date()

    assert result == "Friday, 14 August 2026"

def test_open_calculator():
    actions = SystemActions()

    with patch("src.actions.system_actions.subprocess.Popen") as mock_popen:
        result = actions.open_application("calculator")

    mock_popen.assert_called_once_with(["calc.exe"])

    assert result == "Opening calculator."


def test_open_notepad():
    actions = SystemActions()

    with patch("src.actions.system_actions.subprocess.Popen") as mock_popen:
        result = actions.open_application("notepad")

    mock_popen.assert_called_once_with(["notepad.exe"])

    assert result == "Opening notepad."


def test_open_file_explorer():
    actions = SystemActions()

    with patch("src.actions.system_actions.subprocess.Popen") as mock_popen:
        result = actions.open_application("file explorer")

    mock_popen.assert_called_once_with(["explorer.exe"])

    assert result == "Opening file explorer."


def test_open_unsupported_application():
    actions = SystemActions()

    with patch("src.actions.system_actions.subprocess.Popen") as mock_popen:
        result = actions.open_application("unknown application")

    mock_popen.assert_not_called()

    assert result == "I don't know how to open unknown application."    

def test_open_calculator_alias():
    actions = SystemActions()

    with patch("src.actions.system_actions.subprocess.Popen") as mock_popen:
        result = actions.open_application("calc")

    mock_popen.assert_called_once_with(["calc.exe"])

    assert result == "Opening calculator."


def test_open_explorer_alias():
    actions = SystemActions()

    with patch("src.actions.system_actions.subprocess.Popen") as mock_popen:
        result = actions.open_application("explorer")

    mock_popen.assert_called_once_with(["explorer.exe"])

    assert result == "Opening file explorer."    