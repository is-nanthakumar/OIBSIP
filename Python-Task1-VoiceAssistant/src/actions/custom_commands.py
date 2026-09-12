import json
from pathlib import Path


class CustomCommands:
    """Loads and manages user-defined voice commands."""

    def __init__(self, config_path: str = "custom_commands.json"):
        self.config_path = Path(config_path)
        self.commands = {}
        self.load()

    def load(self) -> None:
        """Load custom commands from the JSON configuration file."""

        if not self.config_path.exists():
            self.commands = {}
            return

        try:
            with self.config_path.open(
                "r",
                encoding="utf-8",
            ) as file:
                data = json.load(file)

            if isinstance(data, dict):
                self.commands = data
            else:
                self.commands = {}

        except (json.JSONDecodeError, OSError):
            self.commands = {}

    def get(self, command: str) -> dict | None:
        """Return a matching custom command."""

        normalized = " ".join(command.lower().strip().split())

        for trigger, config in self.commands.items():
            normalized_trigger = " ".join(
                trigger.lower().strip().split()
            )

            if normalized == normalized_trigger:
                return config

        return None

    def execute(self, command: str) -> str | None:
        """Execute a configured custom command."""

        config = self.get(command)

        if not config:
            return None

        action = config.get("action", "response")
        value = str(config.get("value", "")).strip()

        if action == "response":
            return value

        return None