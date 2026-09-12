from unittest.mock import patch

from src.actions.reminder_actions import ReminderActions


def test_set_reminder():
    actions = ReminderActions()

    with patch(
        "src.actions.reminder_actions.threading.Timer"
    ) as mock_timer:
        result = actions.set_reminder(
            "call John",
            60,
        )

    mock_timer.assert_called_once_with(
        60,
        actions._trigger_reminder,
        args=("call John",),
    )

    mock_timer.return_value.start.assert_called_once()

    assert result == "Reminder set for 60 seconds."


def test_empty_reminder_message():
    actions = ReminderActions()

    result = actions.set_reminder("", 60)

    assert result == (
        "Please tell me what I should remind you about."
    )


def test_invalid_reminder_time():
    actions = ReminderActions()

    result = actions.set_reminder("call John", 0)

    assert result == "Reminder time must be greater than zero."


def test_trigger_reminder():
    actions = ReminderActions()

    with patch("builtins.print") as mock_print:
        actions._trigger_reminder("call John")

    mock_print.assert_called_once_with(
        "\nReminder: call John"
    )


def test_cancel_reminder():
    actions = ReminderActions()

    actions.set_reminder("call John", 60)

    result = actions.cancel_reminder()

    assert result == "Reminder cancelled."


def test_cancel_reminder_when_none_exists():
    actions = ReminderActions()

    result = actions.cancel_reminder()

    assert result == "No active reminder to cancel."


def test_list_reminders():
    actions = ReminderActions()

    actions.set_reminder("call John", 60)
    actions.set_reminder("drink water", 120)

    result = actions.list_reminders()

    assert "call John" in result
    assert "drink water" in result


def test_list_reminders_when_empty():
    actions = ReminderActions()

    result = actions.list_reminders()

    assert result == "No active reminders."


def test_cancel_reminder_by_id():
    actions = ReminderActions()

    actions.set_reminder("call John", 60)
    actions.set_reminder("drink water", 120)

    result = actions.cancel_reminder_by_id(1)

    assert result == "Reminder 1 cancelled."

    remaining = actions.list_reminders()

    assert "call John" not in remaining
    assert "drink water" in remaining


def test_cancel_unknown_reminder_id():
    actions = ReminderActions()

    result = actions.cancel_reminder_by_id(99)

    assert result == "Reminder 99 not found."    
