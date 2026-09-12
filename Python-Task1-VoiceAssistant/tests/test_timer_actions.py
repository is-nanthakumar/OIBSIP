from unittest.mock import patch

from src.actions.timer_actions import TimerActions


def test_set_timer():
    actions = TimerActions()

    with patch("src.actions.timer_actions.threading.Timer") as mock_timer:
        mock_instance = mock_timer.return_value

        result = actions.set_timer(60)

    mock_timer.assert_called_once()
    mock_instance.start.assert_called_once()

    assert result == "Timer set for 60 seconds."


def test_set_timer_rejects_zero():
    actions = TimerActions()

    with patch("src.actions.timer_actions.threading.Timer") as mock_timer:
        result = actions.set_timer(0)

    mock_timer.assert_not_called()

    assert result == "Timer duration must be greater than zero."


def test_set_timer_rejects_negative_value():
    actions = TimerActions()

    with patch("src.actions.timer_actions.threading.Timer") as mock_timer:
        result = actions.set_timer(-10)

    mock_timer.assert_not_called()

    assert result == "Timer duration must be greater than zero."


def test_timer_completion_callback():
    callback = patch(
        "src.actions.timer_actions.print"
    )

    actions = TimerActions()

    with callback:
        actions._trigger_timer()

    assert True


def test_cancel_timer():
    actions = TimerActions()

    with patch("src.actions.timer_actions.threading.Timer") as mock_timer:
        mock_instance = mock_timer.return_value
        mock_instance.is_alive.return_value = True

        actions.set_timer(60)
        result = actions.cancel_timer()

    mock_instance.cancel.assert_called_once()

    assert result == "Timer cancelled."


def test_cancel_timer_when_none_active():
    actions = TimerActions()

    result = actions.cancel_timer()

    assert result == "No active timer to cancel."