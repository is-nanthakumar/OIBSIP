from datetime import datetime
import subprocess


class SystemActions:
    """Handles system-level utility actions."""

    def get_current_time(self) -> str:
        """Return the current local time."""

        return datetime.now().strftime("%I:%M %p")

    def get_current_date(self) -> str:
        """Return the current local date."""

        return datetime.now().strftime("%A, %d %B %Y")

    def open_application(self, application: str) -> str:
        """Open a supported Windows application."""

        application = application.strip().lower()

        applications = {
            "calculator": ["calc.exe"],
            "calc": ["calc.exe"],
            "notepad": ["notepad.exe"],
            "file explorer": ["explorer.exe"],
            "explorer": ["explorer.exe"],
        }

        display_names = {
            "calculator": "calculator",
            "calc": "calculator",
            "notepad": "notepad",
            "file explorer": "file explorer",
            "explorer": "file explorer",
        }

        command = applications.get(application)

        if command is None:
            return f"I don't know how to open {application}."

        subprocess.Popen(command)

        return f"Opening {display_names[application]}."