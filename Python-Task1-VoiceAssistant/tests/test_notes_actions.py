from pathlib import Path

from src.actions.notes_actions import NotesActions


def test_add_note(tmp_path: Path):
    notes_file = tmp_path / "notes.txt"

    actions = NotesActions(str(notes_file))

    result = actions.add_note("Buy milk")

    assert result == "Note saved."
    assert notes_file.read_text(encoding="utf-8") == "Buy milk\n"


def test_add_multiple_notes(tmp_path: Path):
    notes_file = tmp_path / "notes.txt"

    actions = NotesActions(str(notes_file))

    actions.add_note("Buy milk")
    actions.add_note("Call John")

    assert notes_file.read_text(encoding="utf-8") == (
        "Buy milk\n"
        "Call John\n"
    )


def test_add_empty_note(tmp_path: Path):
    notes_file = tmp_path / "notes.txt"

    actions = NotesActions(str(notes_file))

    result = actions.add_note("")

    assert result == "Please tell me what note I should save."


def test_get_notes_when_no_file(tmp_path: Path):
    notes_file = tmp_path / "notes.txt"

    actions = NotesActions(str(notes_file))

    result = actions.get_notes()

    assert result == "You don't have any saved notes."


def test_get_notes(tmp_path: Path):
    notes_file = tmp_path / "notes.txt"

    actions = NotesActions(str(notes_file))

    actions.add_note("Buy milk")
    actions.add_note("Call John")

    result = actions.get_notes()

    assert result == (
        "Your notes are:\n"
        "Buy milk\n"
        "Call John"
    )


def test_clear_notes(tmp_path: Path):
    notes_file = tmp_path / "notes.txt"

    actions = NotesActions(str(notes_file))

    actions.add_note("Buy milk")

    result = actions.clear_notes()

    assert result == "All notes cleared."
    assert notes_file.read_text(encoding="utf-8") == ""


def test_clear_notes_when_no_file(tmp_path: Path):
    notes_file = tmp_path / "notes.txt"

    actions = NotesActions(str(notes_file))

    result = actions.clear_notes()

    assert result == "You don't have any saved notes."