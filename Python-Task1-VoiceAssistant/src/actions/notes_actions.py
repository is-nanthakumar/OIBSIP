from pathlib import Path


class NotesActions:
    """Handles creating, reading, and managing voice notes."""

    def __init__(self, notes_file: str = "notes.txt"):
        self.notes_file = Path(notes_file)

    def add_note(self, note: str) -> str:
        """Add a new note to the notes file."""

        note = note.strip()

        if not note:
            return "Please tell me what note I should save."

        with self.notes_file.open(
            "a",
            encoding="utf-8",
        ) as file:
            file.write(note + "\n")

        return "Note saved."

    def get_notes(self) -> str:
        """Return all saved notes."""

        if not self.notes_file.exists():
            return "You don't have any saved notes."

        content = self.notes_file.read_text(
            encoding="utf-8"
        ).strip()

        if not content:
            return "You don't have any saved notes."

        return f"Your notes are:\n{content}"

    def clear_notes(self) -> str:
        """Delete all saved notes."""

        if not self.notes_file.exists():
            return "You don't have any saved notes."

        self.notes_file.write_text(
            "",
            encoding="utf-8",
        )

        return "All notes cleared."