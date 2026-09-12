import threading
from typing import Callable


class ReminderActions:
    """Handles scheduling and triggering reminders."""

    def __init__(self, on_reminder: Callable[[str], None] | None = None):
        self._timers = []
        self._reminders = []
        self._on_reminder = on_reminder
        self._next_id = 1

    def set_reminder(self, message: str, seconds: int) -> str:
        """Schedule a reminder after the given number of seconds."""

        message = message.strip()

        if not message:
            return "Please tell me what I should remind you about."

        if seconds <= 0:
            return "Reminder time must be greater than zero."

        reminder_id = self._next_id
        self._next_id += 1

        timer = threading.Timer(
            seconds,
            self._trigger_reminder,
            args=(message,),
        )

        timer.daemon = True
        timer.start()

        reminder = {
            "id": reminder_id,
            "message": message,
            "seconds": seconds,
            "timer": timer,
        }

        self._timers.append(timer)
        self._reminders.append(reminder)

        return f"Reminder set for {seconds} seconds."

    def _trigger_reminder(self, message: str) -> None:
        """Trigger a scheduled reminder."""

        reminder_text = f"Reminder: {message}"

        print(f"\n{reminder_text}")

        self._reminders = [
            reminder
            for reminder in self._reminders
            if reminder["message"] != message
        ]  

        self._timers = [
            timer
            for timer in self._timers
            if timer.is_alive()
        ]

        if self._on_reminder:
            self._on_reminder(reminder_text) 



    def get_active_reminders(self) -> list[str]:
        """Return messages for currently active reminders."""

        active_reminders = [
            reminder
            for reminder in self._reminders
            if reminder["timer"].is_alive()
        ]

        self._reminders = active_reminders

        return [
            reminder["message"]
            for reminder in active_reminders
        ]



    def list_reminders(self) -> str:
        """Return all currently active reminders."""

        active_reminders = [
            reminder
            for reminder in self._reminders
            if reminder["timer"].is_alive()
        ]

        self._reminders = active_reminders

        if not active_reminders:
            return "No active reminders."

        lines = []

        for reminder in active_reminders:
            lines.append(
                f"{reminder['id']}. {reminder['message']} "
                f"({reminder['seconds']} seconds)"
            )

        return "Active reminders:\n" + "\n".join(lines)

    def cancel_reminder(self) -> str:
        """Cancel all currently active reminders."""

        active_reminders = [
            reminder
            for reminder in self._reminders
            if reminder["timer"].is_alive()
        ]

        if not active_reminders:
            self._timers = []
            self._reminders = []
            return "No active reminder to cancel."

        for reminder in active_reminders:
            reminder["timer"].cancel()

        self._timers = []
        self._reminders = []

        return "Reminder cancelled."

    def cancel_reminder_by_id(self, reminder_id: int) -> str:
        """Cancel one reminder by its ID."""

        for reminder in self._reminders:
            if reminder["id"] == reminder_id:
                reminder["timer"].cancel()

                self._reminders.remove(reminder)

                self._timers = [
                    timer
                    for timer in self._timers
                    if timer is not reminder["timer"]
                ]

                return f"Reminder {reminder_id} cancelled."

        return f"Reminder {reminder_id} not found."