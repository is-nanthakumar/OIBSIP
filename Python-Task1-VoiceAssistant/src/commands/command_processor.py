from src.actions.knowledge_actions import KnowledgeActions
from src.actions.custom_commands import CustomCommands
from src.actions.browser_actions import BrowserActions
from src.actions.system_actions import SystemActions
from src.actions.weather_actions import WeatherActions
from src.actions.email_actions import EmailActions
from src.actions.reminder_actions import ReminderActions
from src.actions.notes_actions import NotesActions
from src.actions.timer_actions import TimerActions
from typing import Callable
from src.commands.command_parser import CommandParser


class CommandProcessor:
    """Processes parsed voice commands and executes actions."""

    def __init__(
        self,
        on_reminder: Callable[[str], None] | None = None,
    ):
        self.browser_actions = BrowserActions()
        self.system_actions = SystemActions()
        self.weather_actions = WeatherActions()
        self.email_actions = EmailActions()
        self.command_parser = CommandParser()

        self.email_recipient = ""
        self.email_subject = ""
        self.email_conversation_active = False
        self.reminder_actions = ReminderActions(on_reminder=on_reminder)
        self.notes_actions = NotesActions()
        self.timer_actions = TimerActions()
        self.timer_actions = TimerActions()
        self.knowledge_actions = KnowledgeActions()
        self.custom_commands = CustomCommands()


    def process(self, command: str) -> tuple[str, bool]:
        """Process a voice command and return response and exit status."""

        command = command.strip()
        normalized_command = command.lower()

        if not command:
            return "I didn't hear a command.", False

        greetings = {
            "hello": "Hello! How can I help you?",
            "hi": "Hello! How can I help you?",
            "hey": "Hello! How can I help you?",
            "good morning": "Good morning! How can I help you?",
            "good afternoon": "Good afternoon! How can I help you?",
            "good evening": "Good evening! How can I help you?",
        }

        if command in greetings:
            return greetings[command], False

        if "your name" in command or "who are you" in command:
            return "I am your voice assistant.", False

        help_commands = {
            "help",
            "what can you do",
            "please help me",
            "can you help me",
            "what can you help me with",
        }

        if command in help_commands:
            return (
                "I can open websites, search the web, tell you the time and "
                "date, check the weather, and open applications like Calculator, "
                "Notepad, and File Explorer. I can also send emails, set reminders "
                "and timers, save notes, answer general-knowledge questions, "
                "and respond to your custom commands."
            ), False

        time_commands = {
            "what is the time",
            "what's the time",
            "tell me the time",
            "current time",
        }

        if command in time_commands:
            current_time = self.system_actions.get_current_time()
            return f"The current time is {current_time}.", False

        date_commands = {
            "what is today's date",
            "what's today's date",
            "what is the date",
            "tell me today's date",
            "current date",
        }

        if command in date_commands:
            current_date = self.system_actions.get_current_date()
            return f"Today's date is {current_date}.", False 


        if self.email_conversation_active:

            if normalized_command in {
                "cancel",
                "cancel email",
                "stop email",
            }:
                self.email_recipient = ""
                self.email_subject = ""
                self.email_conversation_active = False

                return "Email cancelled.", False

            if not self.email_subject:
                self.email_subject = command

                return (
                    "Got it. What should I say in the email?"
                ), False

            response = self.email_actions.send_email(
                self.email_recipient,
                self.email_subject,
                command,
            )

            self.email_recipient = ""
            self.email_subject = ""
            self.email_conversation_active = False

            return response, False

        

        # ---------------------------------------------------------
        # CUSTOM COMMANDS
        # ---------------------------------------------------------

        custom_response = self.custom_commands.execute(command)

        if custom_response is not None:
            return custom_response, False



        parsed_command = self.command_parser.parse(command) 

        if parsed_command.action == "exit":  
            return "Goodbye. Shutting down the voice assistant.", True


        
        # ---------------------------------------------------------
        # GENERAL KNOWLEDGE
        # ---------------------------------------------------------

        if parsed_command.action == "knowledge":
            response = self.knowledge_actions.answer(
                parsed_command.argument
            )

            return response, False



        if parsed_command.action == "email":
            if not parsed_command.argument:
                return (
                    "Please tell me the recipient email address."
                ), False

            self.email_recipient = parsed_command.argument
            self.email_subject = ""
            self.email_conversation_active = True

            return (
                 "I have the recipient address. "
                 "Please provide the email subject and message."
            ), False
     
                
          
                # ---------------------------------------------------------
        # TIMER
        # ---------------------------------------------------------

        if parsed_command.action == "timer":
            seconds = int(parsed_command.argument)

            response = self.timer_actions.set_timer(seconds)

            return response, False

        if parsed_command.action == "cancel_timer":
            response = self.timer_actions.cancel_timer()

            return response, False




        # ---------------------------------------------------------
        # REMINDERS
        # ---------------------------------------------------------

        # Cancel all reminders
        if command in {
            "cancel",
            "cancel reminder",
            "cancel the reminder",
            "please cancel",
            "please cancel the reminder",
        }:
            response = self.reminder_actions.cancel_reminder()
            return response, False

        # Set a reminder
        if parsed_command.action == "reminder":
            message, seconds_text = parsed_command.argument.rsplit("|", 1)

            seconds = int(seconds_text)

            response = self.reminder_actions.set_reminder(
                message,
                seconds,
            )

            return response, False


        # ---------------------------------------------------------
        # NOTES
        # ---------------------------------------------------------

        if parsed_command.action == "note":
            response = self.notes_actions.add_note(
                parsed_command.argument
            )

            return response, False

        if parsed_command.action == "list_notes":
            response = self.notes_actions.get_notes()

            return response, False

        if parsed_command.action == "clear_notes":
            response = self.notes_actions.clear_notes()

            return response, False



        # List active reminders
        if parsed_command.action == "list_reminders":
            response = self.reminder_actions.list_reminders()
            return response, False

        # Cancel a specific reminder by ID
        if parsed_command.action == "cancel_reminder":
            reminder_id = int(parsed_command.argument)

            response = self.reminder_actions.cancel_reminder_by_id(
                reminder_id
            )

            return response, False

        if parsed_command.action == "list_reminders":
            response = self.reminder_actions.list_reminders()
            return response, False

        if parsed_command.action == "cancel_reminder":
            reminder_id = int(parsed_command.argument)

            response = self.reminder_actions.cancel_reminder_by_id(
                reminder_id
            )

            return response, False



        if parsed_command.action == "weather":
            if not parsed_command.argument:
                return (
                    "Please tell me which location you want "
                    "the weather for."
                ), False

            response = self.weather_actions.get_weather(
                parsed_command.argument
            )

            return response, False

        if parsed_command.action == "open_application":
            if not parsed_command.argument:
                return (
                    "Please tell me which application you want me to open."
                ), False

            response = self.system_actions.open_application(
                parsed_command.argument
            )

            return response, False

        if parsed_command.action == "open":
            if not parsed_command.argument:
                return "Please tell me what you want me to open.", False

            response = self.browser_actions.open_website(
                parsed_command.argument
            )

            return response, False

        if parsed_command.action == "search":
            if not parsed_command.argument:
                return (
                    "Please tell me what you want me to search for."
                ), False

            response = self.browser_actions.search_web(
                parsed_command.argument
            )

            return response, False

        return (
            f"I heard you say: {command}. "
            "I don't have an action for that command yet."
        ), False