from unittest.mock import patch
from src.commands.command_processor import CommandProcessor


def test_greeting():
    processor = CommandProcessor()

    response, should_exit = processor.process("hello")

    assert "Hello" in response
    assert should_exit is False


def test_identity():
    processor = CommandProcessor()

    response, should_exit = processor.process("what is your name")

    assert "voice assistant" in response.lower()
    assert should_exit is False


def test_exit_command():
    processor = CommandProcessor()

    response, should_exit = processor.process("exit")

    assert should_exit is True
    assert "goodbye" in response.lower()


def test_empty_command():
    processor = CommandProcessor()

    response, should_exit = processor.process("")

    assert response == "I didn't hear a command."
    assert should_exit is False

def test_quite_as_exit_command():
    processor = CommandProcessor()

    response, should_exit = processor.process("quite")

    assert should_exit is True
    assert "goodbye" in response.lower() 


def test_open_youtube():
    processor = CommandProcessor()

    with patch(
        "src.commands.command_processor.BrowserActions.open_website"
    ) as mock_open:
        mock_open.return_value = "Opening youtube."

        response, should_exit = processor.process("open youtube")

        mock_open.assert_called_once_with("youtube")

    assert response == "Opening youtube."
    assert should_exit is False


def test_search_web():
    processor = CommandProcessor()

    with patch(
        "src.commands.command_processor.BrowserActions.search_web"
    ) as mock_search:
        mock_search.return_value = "Searching the web for python tutorials."

        response, should_exit = processor.process(
            "search python tutorials"
        )

        mock_search.assert_called_once_with("python tutorials")

    assert response == "Searching the web for python tutorials."
    assert should_exit is False       


def test_current_time_command():
    processor = CommandProcessor()

    with patch(
        "src.commands.command_processor.SystemActions.get_current_time"
    ) as mock_time:
        mock_time.return_value = "02:30 PM"

        response, should_exit = processor.process("what is the time")

        mock_time.assert_called_once()

    assert response == "The current time is 02:30 PM."
    assert should_exit is False


def test_current_date_command():
    processor = CommandProcessor()

    with patch(
        "src.commands.command_processor.SystemActions.get_current_date"
    ) as mock_date:
        mock_date.return_value = "Friday, 14 August 2026"

        response, should_exit = processor.process("what is today's date")

        mock_date.assert_called_once()

    assert response == "Today's date is Friday, 14 August 2026."
    assert should_exit is False    

def test_machine_learning_search_is_not_greeting():
    processor = CommandProcessor()

    with patch(
        "src.commands.command_processor.BrowserActions.search_web"
    ) as mock_search:
        mock_search.return_value = (
            "Searching the web for machine learning."
        )

        response, should_exit = processor.process(
            "please search for machine learning"
        )

        mock_search.assert_called_once_with(
            "machine learning"
        )

    assert response == "Searching the web for machine learning."
    assert should_exit is False    


def test_help_command():
    processor = CommandProcessor()

    response, should_exit = processor.process("help")

    assert "open websites" in response.lower()
    assert "search the web" in response.lower()
    assert "time" in response.lower()
    assert "date" in response.lower()
    assert "calculator" in response.lower()
    assert should_exit is False


def test_what_can_you_do_command():
    processor = CommandProcessor()

    response, should_exit = processor.process("what can you do")

    assert "open websites" in response.lower()
    assert "search the web" in response.lower()
    assert "calculator" in response.lower()
    assert should_exit is False

def test_bye_command():
    processor = CommandProcessor()

    response, should_exit = processor.process("bye")

    assert should_exit is True
    assert "goodbye" in response.lower()


def test_goodbye_command():
    processor = CommandProcessor()

    response, should_exit = processor.process("goodbye")

    assert should_exit is True
    assert "goodbye" in response.lower()


def test_stop_command():
    processor = CommandProcessor()

    response, should_exit = processor.process("stop")

    assert should_exit is True
    assert "goodbye" in response.lower()    

def test_open_gmail():
    processor = CommandProcessor()

    with patch(
        "src.commands.command_processor.BrowserActions.open_website"
    ) as mock_open:
        mock_open.return_value = "Opening gmail."

        response, should_exit = processor.process(
            "please open gmail"
        )

        mock_open.assert_called_once_with("gmail")

    assert response == "Opening gmail."
    assert should_exit is False


def test_open_whatsapp():
    processor = CommandProcessor()

    with patch(
        "src.commands.command_processor.BrowserActions.open_website"
    ) as mock_open:
        mock_open.return_value = "Opening whatsapp."

        response, should_exit = processor.process(
            "please open whatsapp"
        )

        mock_open.assert_called_once_with("whatsapp")

    assert response == "Opening whatsapp."
    assert should_exit is False    

def test_open_unsupported_website():
    processor = CommandProcessor()

    with patch(
        "src.commands.command_processor.BrowserActions.open_website"
    ) as mock_open:
        mock_open.return_value = (
            "I don't know how to open instagram."
        )

        response, should_exit = processor.process(
            "open instagram"
        )

        mock_open.assert_called_once_with("instagram")

    assert response == "I don't know how to open instagram."
    assert should_exit is False    

def test_unknown_command():
    processor = CommandProcessor()

    response, should_exit = processor.process(
        "tell me something completely unknown"
    )

    assert response == (
        "I heard you say: tell me something completely unknown. "
        "I don't have an action for that command yet."
    )
    assert should_exit is False   

def test_hi_greeting():
    processor = CommandProcessor()

    response, should_exit = processor.process("hi")

    assert response == "Hello! How can I help you?"
    assert should_exit is False


def test_hey_greeting():
    processor = CommandProcessor()

    response, should_exit = processor.process("hey")

    assert response == "Hello! How can I help you?"
    assert should_exit is False


def test_good_morning_greeting():
    processor = CommandProcessor()

    response, should_exit = processor.process("good morning")

    assert response == "Good morning! How can I help you?"
    assert should_exit is False


def test_good_afternoon_greeting():
    processor = CommandProcessor()

    response, should_exit = processor.process("good afternoon")

    assert response == "Good afternoon! How can I help you?"
    assert should_exit is False


def test_good_evening_greeting():
    processor = CommandProcessor()

    response, should_exit = processor.process("good evening")

    assert response == "Good evening! How can I help you?"
    assert should_exit is False


def test_hi_inside_unknown_sentence_is_not_greeting():
    processor = CommandProcessor()

    response, should_exit = processor.process(
        "tell me something about hi"
    )

    assert response == (
        "I heard you say: tell me something about hi. "
        "I don't have an action for that command yet."
    )
    assert should_exit is False     


def test_tell_me_the_time_command():
    processor = CommandProcessor()

    with patch(
        "src.commands.command_processor.SystemActions.get_current_time"
    ) as mock_time:
        mock_time.return_value = "02:30 PM"

        response, should_exit = processor.process("tell me the time")

        mock_time.assert_called_once()

    assert response == "The current time is 02:30 PM."
    assert should_exit is False


def test_current_time_command():
    processor = CommandProcessor()

    with patch(
        "src.commands.command_processor.SystemActions.get_current_time"
    ) as mock_time:
        mock_time.return_value = "02:30 PM"

        response, should_exit = processor.process("current time")

        mock_time.assert_called_once()

    assert response == "The current time is 02:30 PM."
    assert should_exit is False


def test_what_is_the_date_command():
    processor = CommandProcessor()

    with patch(
        "src.commands.command_processor.SystemActions.get_current_date"
    ) as mock_date:
        mock_date.return_value = "Friday, 14 August 2026"

        response, should_exit = processor.process("what is the date")

        mock_date.assert_called_once()

    assert response == "Today's date is Friday, 14 August 2026."
    assert should_exit is False


def test_tell_me_todays_date_command():
    processor = CommandProcessor()

    with patch(
        "src.commands.command_processor.SystemActions.get_current_date"
    ) as mock_date:
        mock_date.return_value = "Friday, 14 August 2026"

        response, should_exit = processor.process(
            "tell me today's date"
        )

        mock_date.assert_called_once()

    assert response == "Today's date is Friday, 14 August 2026."
    assert should_exit is False    

def test_time_word_inside_unknown_sentence_is_not_time_command():
    processor = CommandProcessor()

    with patch(
        "src.commands.command_processor.SystemActions.get_current_time"
    ) as mock_time:
        response, should_exit = processor.process(
            "tell me something about time management"
        )

        mock_time.assert_not_called()

    assert response == (
        "I heard you say: tell me something about time management. "
        "I don't have an action for that command yet."
    )
    assert should_exit is False    

def test_please_help_me_command():
    processor = CommandProcessor()

    response, should_exit = processor.process("please help me")

    assert "open websites" in response.lower()
    assert "search the web" in response.lower()
    assert "calculator" in response.lower()
    assert should_exit is False


def test_can_you_help_me_command():
    processor = CommandProcessor()

    response, should_exit = processor.process("can you help me")

    assert "open websites" in response.lower()
    assert "search the web" in response.lower()
    assert "calculator" in response.lower()
    assert should_exit is False


def test_what_can_you_help_me_with_command():
    processor = CommandProcessor()

    response, should_exit = processor.process(
        "what can you help me with"
    )

    assert "open websites" in response.lower()
    assert "search the web" in response.lower()
    assert "calculator" in response.lower()
    assert should_exit is False



def test_weather_command():
    processor = CommandProcessor()

    with patch(
        "src.commands.command_processor.WeatherActions.get_weather"
    ) as mock_weather:
        mock_weather.return_value = (
            "The current weather in Chennai is "
            "32.5 degrees Celsius, mainly clear, with "
            "65% humidity."
        )

        response, should_exit = processor.process(
            "what is the weather in Chennai"
        )

        mock_weather.assert_called_once_with("Chennai")

    assert response == (
        "The current weather in Chennai is "
        "32.5 degrees Celsius, mainly clear, with "
        "65% humidity."
    )
    assert should_exit is False


def test_weather_command_with_natural_phrase():
    processor = CommandProcessor()

    with patch(
        "src.commands.command_processor.WeatherActions.get_weather"
    ) as mock_weather:
        mock_weather.return_value = (
            "The current weather in Bangalore is "
            "30 degrees Celsius, partly cloudy, with "
            "70% humidity."
        )

        response, should_exit = processor.process(
            "could you tell me the weather in Bangalore"
        )

        mock_weather.assert_called_once_with("Bangalore")

    assert "Bangalore" in response
    assert should_exit is False


def test_weather_command_without_location():
    processor = CommandProcessor()

    response, should_exit = processor.process(
        "what is the weather"
    )

    assert response == (
        "Please tell me which location you want the weather for."
    )
    assert should_exit is False



def test_email_command_requires_recipient_details():
    processor = CommandProcessor()

    response, should_exit = processor.process(
        "send an email to test@example.com"
    )

    assert response == (
        "I have the recipient address. "
        "Please provide the email subject and message."
    )
    assert should_exit is False

def test_email_conversation_collects_subject():
    processor = CommandProcessor()

    response, should_exit = processor.process(
        "send an email to test@example.com"
    )

    assert response == (
        "I have the recipient address. "
        "Please provide the email subject and message."
    )
    assert should_exit is False

    response, should_exit = processor.process(
        "Project update"
    )

    assert response == (
        "Got it. What should I say in the email?"
    )
    assert should_exit is False


def test_email_conversation_sends_message():
    processor = CommandProcessor()

    processor.process(
        "send an email to test@example.com"
    )

    processor.process(
        "Project update"
    )

    with patch.object(
        processor.email_actions,
        "send_email",
        return_value=(
            "Email sent successfully to test@example.com."
        ),
    ) as mock_send:
        response, should_exit = processor.process(
            "The project has been completed."
        )

    mock_send.assert_called_once_with(
        "test@example.com",
        "Project update",
        "The project has been completed.",
    )

    assert response == (
        "Email sent successfully to test@example.com."
    )
    assert should_exit is False


def test_email_conversation_can_be_cancelled():
    processor = CommandProcessor()

    processor.process(
        "send an email to test@example.com"
    )

    response, should_exit = processor.process(
        "cancel"
    )

    assert response == "Email cancelled."
    assert should_exit is False



def test_note_command_saves_note():
    processor = CommandProcessor()

    with patch.object(
        processor.notes_actions,
        "add_note",
        return_value="Note saved.",
    ) as mock_add_note:
        response, should_exit = processor.process(
            "take a note buy milk"
        )

    mock_add_note.assert_called_once_with("buy milk")

    assert response == "Note saved."
    assert should_exit is False


def test_show_notes_command():
    processor = CommandProcessor()

    with patch.object(
        processor.notes_actions,
        "get_notes",
        return_value="Your notes are:\nBuy milk",
    ) as mock_get_notes:
        response, should_exit = processor.process(
            "show my notes"
        )

    mock_get_notes.assert_called_once_with()

    assert response == "Your notes are:\nBuy milk"
    assert should_exit is False


def test_clear_notes_command():
    processor = CommandProcessor()

    with patch.object(
        processor.notes_actions,
        "clear_notes",
        return_value="All notes cleared.",
    ) as mock_clear_notes:
        response, should_exit = processor.process(
            "clear my notes"
        )

    mock_clear_notes.assert_called_once_with()

    assert response == "All notes cleared."
    assert should_exit is False 


def test_general_knowledge_python():
    processor = CommandProcessor()

    with patch.object(
        processor.knowledge_actions,
        "answer",
        return_value="Python is a programming language.",
    ) as mock_answer:
        response, should_exit = processor.process(
            "what is python"
        )

    mock_answer.assert_called_once_with("what is python")

    assert response == "Python is a programming language."
    assert should_exit is False


def test_general_knowledge_who_created_python():
    processor = CommandProcessor()

    with patch.object(
        processor.knowledge_actions,
        "answer",
        return_value="Python was created by Guido van Rossum.",
    ) as mock_answer:
        response, should_exit = processor.process(
            "who created python"
        )

    mock_answer.assert_called_once_with("who created python")

    assert "Guido van Rossum" in response
    assert should_exit is False


def test_custom_command():
    processor = CommandProcessor()

    processor.custom_commands.commands = {
        "study mode": {
            "action": "response",
            "value": "Study mode activated.",
        }
    }

    response, should_exit = processor.process(
        "study mode"
    )

    assert response == "Study mode activated."
    assert should_exit is False


def test_custom_command_is_case_insensitive():
    processor = CommandProcessor()

    processor.custom_commands.commands = {
        "study mode": {
            "action": "response",
            "value": "Study mode activated.",
        }
    }

    response, should_exit = processor.process(
        "STUDY MODE"
    )

    assert response == "Study mode activated."
    assert should_exit is False


def test_unknown_custom_command():
    processor = CommandProcessor()

    processor.custom_commands.commands = {
        "study mode": {
            "action": "response",
            "value": "Study mode activated.",
        }
    }

    response, should_exit = processor.process(
        "something completely different"
    )

    assert "I heard you say" in response
    assert should_exit is False       



