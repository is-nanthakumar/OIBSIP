import threading
from typing import Callable


class TimerActions:
    """Handles countdown timers."""

    def __init__(self, on_timer_complete: Callable[[str], None] | None = None):
        self._timers = []
        self._on_timer_complete = on_timer_complete

    def set_timer(self, seconds: int) -> str:
        """Start a countdown timer."""

        if seconds <= 0:
            return "Timer duration must be greater than zero."

        timer = threading.Timer(
            seconds,
            self._trigger_timer,
        )

        timer.daemon = True
        timer.start()

        self._timers.append(timer)

        return f"Timer set for {seconds} seconds."

    def _trigger_timer(self) -> None:
        """Trigger timer completion."""

        message = "Timer finished."

        print(f"\n{message}")

        if self._on_timer_complete:
            self._on_timer_complete(message)

    def cancel_timer(self) -> str:
        """Cancel active timers."""

        active_timers = [
            timer
            for timer in self._timers
            if timer.is_alive()
        ]

        if not active_timers:
            self._timers = []
            return "No active timer to cancel."

        for timer in active_timers:
            timer.cancel()

        self._timers = []

        return "Timer cancelled."