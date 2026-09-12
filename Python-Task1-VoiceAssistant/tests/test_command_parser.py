from src.commands.command_parser import CommandParser


def test_open_command():
    parser = CommandParser()

    result = parser.parse("open youtube")

    assert result.action == "open"
    assert result.argument == "youtube"


def test_please_open_command():
    parser = CommandParser()

    result = parser.parse("please open youtube")

    assert result.action == "open"
    assert result.argument == "youtube"


def test_can_you_open_command():
    parser = CommandParser()

    result = parser.parse("can you open google")

    assert result.action == "open"
    assert result.argument == "google"


def test_search_command():
    parser = CommandParser()

    result = parser.parse("search python tutorials")

    assert result.action == "search"
    assert result.argument == "python tutorials"


def test_search_for_command():
    parser = CommandParser()

    result = parser.parse("search for python tutorials")

    assert result.action == "search"
    assert result.argument == "python tutorials"


def test_please_search_for_command():
    parser = CommandParser()

    result = parser.parse("please search for machine learning")

    assert result.action == "search"
    assert result.argument == "machine learning"


def test_can_you_search_for_command():
    parser = CommandParser()

    result = parser.parse("can you search for Python tutorials")

    assert result.action == "search"
    assert result.argument == "python tutorials"


def test_exit_command():
    parser = CommandParser()

    result = parser.parse("quit")

    assert result.action == "exit"
    assert result.argument == ""


def test_empty_command():
    parser = CommandParser()

    result = parser.parse("")

    assert result.action == "empty"
    assert result.argument == ""


def test_unknown_command():
    parser = CommandParser()

    result = parser.parse("tell me a joke")

    assert result.action == "unknown"
    assert result.argument == "tell me a joke"

def test_open_calculator_command():
    parser = CommandParser()

    result = parser.parse("open calculator")

    assert result.action == "open_application"
    assert result.argument == "calculator"


def test_open_notepad_command():
    parser = CommandParser()

    result = parser.parse("please open notepad")

    assert result.action == "open_application"
    assert result.argument == "notepad"


def test_open_file_explorer_command():
    parser = CommandParser()

    result = parser.parse("can you open file explorer")

    assert result.action == "open_application"
    assert result.argument == "file explorer"    

def test_bye_command():
    parser = CommandParser()

    result = parser.parse("bye")

    assert result.action == "exit"
    assert result.argument == ""


def test_goodbye_command():
    parser = CommandParser()

    result = parser.parse("goodbye")

    assert result.action == "exit"
    assert result.argument == ""


def test_stop_command():
    parser = CommandParser()

    result = parser.parse("stop")

    assert result.action == "exit"
    assert result.argument == ""


def test_bye_command():
    parser = CommandParser()

    result = parser.parse("bye")

    assert result.action == "exit"
    assert result.argument == ""


def test_goodbye_command():
    parser = CommandParser()

    result = parser.parse("goodbye")

    assert result.action == "exit"
    assert result.argument == ""


def test_stop_command():
    parser = CommandParser()

    result = parser.parse("stop")

    assert result.action == "exit"
    assert result.argument == ""    

def test_open_calculator_alias_command():
    parser = CommandParser()

    result = parser.parse("open calc")

    assert result.action == "open_application"
    assert result.argument == "calc"


def test_open_explorer_alias_command():
    parser = CommandParser()

    result = parser.parse("open explorer")

    assert result.action == "open_application"
    assert result.argument == "explorer"           


def test_open_command_with_extra_spaces():
    parser = CommandParser()

    result = parser.parse("  open    youtube  ")

    assert result.action == "open"
    assert result.argument == "youtube"


def test_open_calculator_with_extra_spaces():
    parser = CommandParser()

    result = parser.parse("PLEASE   OPEN   CALC")

    assert result.action == "open_application"
    assert result.argument == "calc"


def test_search_command_with_extra_spaces():
    parser = CommandParser()

    result = parser.parse("  search    for    python tutorials  ")

    assert result.action == "search"
    assert result.argument == "python tutorials"


def test_exit_command_with_extra_spaces():
    parser = CommandParser()

    result = parser.parse("   GOODBYE   ")

    assert result.action == "exit"
    assert result.argument == "" 

def test_open_the_calculator_command():
    parser = CommandParser()

    result = parser.parse("open the calculator")

    assert result.action == "open_application"
    assert result.argument == "calculator"


def test_please_open_the_notepad_command():
    parser = CommandParser()

    result = parser.parse("please open the notepad")

    assert result.action == "open_application"
    assert result.argument == "notepad"


def test_can_you_open_the_file_explorer_command():
    parser = CommandParser()

    result = parser.parse("can you open the file explorer")

    assert result.action == "open_application"
    assert result.argument == "file explorer"


def test_could_you_please_open_calculator_command():
    parser = CommandParser()

    result = parser.parse("could you please open calculator")

    assert result.action == "open_application"
    assert result.argument == "calculator"  


def test_search_the_web_command():
    parser = CommandParser()

    result = parser.parse("please search the web for Python tutorials")

    assert result.action == "search"
    assert result.argument == "python tutorials"


def test_could_you_search_the_web_command():
    parser = CommandParser()

    result = parser.parse(
        "could you search the web for machine learning"
    )

    assert result.action == "search"
    assert result.argument == "machine learning"


def test_search_google_command():
    parser = CommandParser()

    result = parser.parse("can you search Google for Python")

    assert result.action == "search"
    assert result.argument == "python"   


def test_natural_open_youtube_command():
    parser = CommandParser()

    result = parser.parse(
        "would you please open youtube for me"
    )

    assert result.action == "open"
    assert result.argument == "youtube"


def test_natural_search_command():
    parser = CommandParser()

    result = parser.parse(
        "could you find python tutorials online"
    )

    assert result.action == "search"
    assert result.argument == "python tutorials"


def test_natural_search_for_command():
    parser = CommandParser()

    result = parser.parse(
        "i want to search for machine learning"
    )

    assert result.action == "search"
    assert result.argument == "machine learning"


def test_natural_open_calculator_command():
    parser = CommandParser()

    result = parser.parse(
        "can you launch the calculator"
    )

    assert result.action == "open_application"
    assert result.argument == "calculator"


def test_natural_open_notepad_command():
    parser = CommandParser()

    result = parser.parse(
        "would you open notepad for me"
    )

    assert result.action == "open_application"
    assert result.argument == "notepad"       


def test_start_calculator_natural_command():
    parser = CommandParser()

    result = parser.parse(
        "please start the calculator for me"
    )

    assert result.action == "open_application"
    assert result.argument == "calculator"


def test_launch_notepad_natural_command():
    parser = CommandParser()

    result = parser.parse(
        "could you launch notepad for me"
    )

    assert result.action == "open_application"
    assert result.argument == "notepad"


def test_find_information_natural_search_command():
    parser = CommandParser()

    result = parser.parse(
        "can you find information about python"
    )

    assert result.action == "search"
    assert result.argument == "information about python"


def test_look_up_natural_search_command():
    parser = CommandParser()

    result = parser.parse(
        "please look up machine learning tutorials"
    )

    assert result.action == "search"
    assert result.argument == "machine learning tutorials"


def test_unknown_sentence_does_not_become_search():
    parser = CommandParser()

    result = parser.parse(
        "tell me something about searching"
    )

    assert result.action == "unknown"
    assert result.argument == "tell me something about searching"       


def test_open_word_inside_normal_sentence_is_not_open_command():
    parser = CommandParser()

    result = parser.parse(
        "I was talking about opening a new account"
    )

    assert result.action == "unknown"


def test_search_word_inside_normal_sentence_is_not_search_command():
    parser = CommandParser()

    result = parser.parse(
        "I am searching for a better way to learn"
    )

    assert result.action == "unknown"


def test_launch_word_inside_normal_sentence_is_not_launch_command():
    parser = CommandParser()

    result = parser.parse(
        "the rocket launch was successful"
    )

    assert result.action == "unknown"


def test_find_word_inside_normal_sentence_is_not_search_command():
    parser = CommandParser()

    result = parser.parse(
        "I find Python interesting"
    )

    assert result.action == "unknown"


def test_weather_command_with_location():
    parser = CommandParser()

    result = parser.parse(
        "what is the weather in Chennai"
    )

    assert result.action == "weather"
    assert result.argument == "Chennai"


def test_weather_command_with_please():
    parser = CommandParser()

    result = parser.parse(
        "please check the weather in Chennai"
    )

    assert result.action == "weather"
    assert result.argument == "Chennai"


def test_weather_command_natural_phrase():
    parser = CommandParser()

    result = parser.parse(
        "could you tell me the weather in Bangalore"
    )

    assert result.action == "weather"
    assert result.argument == "Bangalore"


def test_weather_command_with_for():
    parser = CommandParser()

    result = parser.parse(
        "what is the weather like in Mumbai"
    )

    assert result.action == "weather"
    assert result.argument == "Mumbai"


def test_weather_word_inside_normal_sentence_is_not_weather_command():
    parser = CommandParser()

    result = parser.parse(
        "I was reading about weather patterns today"
    )

    assert result.action == "unknown"  



def test_send_email_command():
    parser = CommandParser()

    result = parser.parse(
        "send an email to test@example.com"
    )

    assert result.action == "email"
    assert result.argument == "test@example.com"


def test_please_send_email_command():
    parser = CommandParser()

    result = parser.parse(
        "please send an email to test@example.com"
    )

    assert result.action == "email"
    assert result.argument == "test@example.com"


def test_can_you_send_email_command():
    parser = CommandParser()

    result = parser.parse(
        "can you send email to test@example.com"
    )

    assert result.action == "email"
    assert result.argument == "test@example.com"


def test_email_command_with_for_me():
    parser = CommandParser()

    result = parser.parse(
        "please send an email to test@example.com for me"
    )

    assert result.action == "email"
    assert result.argument == "test@example.com"  



def test_reminder_command():
    parser = CommandParser()

    result = parser.parse(
        "remind me to call john in 10 minutes"
    )

    assert result.action == "reminder"
    assert result.argument == "call john|600"


def test_reminder_command_seconds():
    parser = CommandParser()

    result = parser.parse(
        "please remind me to drink water in 30 seconds"
    )

    assert result.action == "reminder"
    assert result.argument == "drink water|30"


def test_set_reminder_command():
    parser = CommandParser()

    result = parser.parse(
        "set a reminder to check the report in 5 minutes"
    )

    assert result.action == "reminder"
    assert result.argument == "check the report|300" 



def test_list_reminders_command():
    parser = CommandParser()

    result = parser.parse("list reminders")

    assert result.action == "list_reminders"
    assert result.argument == ""


def test_show_my_reminders_command():
    parser = CommandParser()

    result = parser.parse("show my reminders")

    assert result.action == "list_reminders"
    assert result.argument == ""


def test_cancel_reminder_command():
    parser = CommandParser()

    result = parser.parse("cancel reminder 2")

    assert result.action == "cancel_reminder"
    assert result.argument == "2"


def test_delete_reminder_command():
    parser = CommandParser()

    result = parser.parse("delete reminder 3")

    assert result.action == "cancel_reminder"
    assert result.argument == "3"  


def test_set_timer_command():
    parser = CommandParser()

    result = parser.parse("set a timer for 30 seconds")

    assert result.action == "timer"
    assert result.argument == "30"


def test_set_timer_minutes_command():
    parser = CommandParser()

    result = parser.parse("set timer for 5 minutes")

    assert result.action == "timer"
    assert result.argument == "300"


def test_start_timer_command():
    parser = CommandParser()

    result = parser.parse("start a timer for 1 hour")

    assert result.action == "timer"
    assert result.argument == "3600"


def test_cancel_timer_command():
    parser = CommandParser()

    result = parser.parse("cancel timer")

    assert result.action == "cancel_timer"
    assert result.argument == ""  



def test_take_a_note_command():
    parser = CommandParser()

    result = parser.parse(
        "take a note buy milk"
    )

    assert result.action == "note"
    assert result.argument == "buy milk"


def test_make_a_note_command():
    parser = CommandParser()

    result = parser.parse(
        "make a note call John"
    )

    assert result.action == "note"
    assert result.argument == "call john"


def test_save_note_command():
    parser = CommandParser()

    result = parser.parse(
        "save note finish project"
    )

    assert result.action == "note"
    assert result.argument == "finish project"


def test_show_notes_command():
    parser = CommandParser()

    result = parser.parse(
        "show my notes"
    )

    assert result.action == "list_notes"
    assert result.argument == ""


def test_read_notes_command():
    parser = CommandParser()

    result = parser.parse(
        "read notes"
    )

    assert result.action == "list_notes"
    assert result.argument == ""


def test_clear_notes_command():
    parser = CommandParser()

    result = parser.parse(
        "clear my notes"
    )

    assert result.action == "clear_notes"
    assert result.argument == ""


def test_general_knowledge_command():
    parser = CommandParser()

    result = parser.parse("what is python")

    assert result.action == "knowledge"
    assert result.argument == "what is python"


def test_general_knowledge_who_question():
    parser = CommandParser()

    result = parser.parse("who created python")

    assert result.action == "knowledge"
    assert result.argument == "who created python"


def test_general_knowledge_explain_question():
    parser = CommandParser()

    result = parser.parse(
        "can you explain machine learning"
    )

    assert result.action == "knowledge"
    assert result.argument == "can you explain machine learning"


def test_natural_open_command_phase_two():
    parser = CommandParser()

    result = parser.parse(
        "would you mind opening youtube"
    )

    assert result.action == "open"
    assert result.argument == "youtube"


def test_natural_search_command_phase_two():
    parser = CommandParser()

    result = parser.parse(
        "could you please search for python tutorials"
    )

    assert result.action == "search"
    assert result.argument == "python tutorials"


def test_natural_weather_command_phase_two():
    parser = CommandParser()

    result = parser.parse(
        "i want to know the weather in Chennai"
    )

    assert result.action == "weather"
    assert result.argument == "Chennai"