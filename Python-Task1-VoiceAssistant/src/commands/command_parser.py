from dataclasses import dataclass


@dataclass
class ParsedCommand:
    """Represents a parsed voice command."""

    action: str
    argument: str = ""


class CommandParser:
    """Converts natural command variations into structured commands."""

    OPEN_PREFIXES = (
        "i want you to open ",
        "i need you to open ",
        "would you mind opening ",
        "would you please open ",
        "could you please open ",
        "please open ",
        "can you open ",
        "can you please open ",
        "could you open ",
        "would you open ",
        "please start ",
        "could you launch ",
        "can you launch ",
        "launch ",
        "start ",
        "open ",
    )

    SEARCH_PREFIXES = (
        "please search the web for ",
        "would you mind searching for ",
        "i need you to search for ",
        "i want you to search for ",

        "could you search the web for ",
        "can you search the web for ",
        "please search google for ",
        "could you search google for ",
        "can you search google for ",
        "can you please search for ",
        "please search for ",
        "can you search for ",
        "could you search for ",
        "could you please search for ",
        "i want to search for ",
        "search for ",
        "please search ",
        "can you search ",
        "could you search ",
        "search ",
        "can you find information about ",
        "could you find information about ",
        "please find information about ",
        "find information about ",
        "can you find information on ",
        "could you find information on ",
        "please find information on ",
        "find information on ",
        "could you find ",
        "please look up ",
        "can you look up ",
        "could you look up ",
        "look up ",
    )

    EMAIL_PREFIXES = (
        "please send an email to ",
        "could you send an email to ",
        "can you send an email to ",
        "would you send an email to ",
        "send an email to ",
        "please send email to ",
        "could you send email to ",
        "can you send email to ",
        "send email to ",
    )

    WEATHER_PREFIXES = (
        "what is the weather like in ",
        "what's the weather like in ",
        "what is the weather in ",
        "what's the weather in ",
        "what is the weather for ",
        "what's the weather for ",
        "would you mind checking the weather in ",
        "tell me the weather in ",
        "tell me the weather for ",
        "can you tell me the weather like in ",
        "can you tell me the weather in ",
        "can you tell me the weather for ",
        "can you please check the weather in ",
        "could you tell me the weather like in ",
        "could you tell me the weather in ",
        "could you tell me the weather for ",
        "could you please check the weather in ",
        "please tell me the weather in ",
        "please tell me the weather for ",
        "please check the weather in ",
        "please check the weather for ",
        "can you check the weather in ",
        "can you check the weather for ",
        "could you check the weather in ",
        "could you check the weather for ",
        "i want to know the weather in ",
        "i would like to know the weather in ",
        "check the weather in ",
        "check the weather for ",
        "weather in ",
        "weather for ",
    )

    APPLICATIONS = {
        "calculator",
        "calc",
        "notepad",
        "file explorer",
        "explorer",
    }

    KNOWLEDGE_PREFIXES = (
        "what is ",
        "what are ",
        "who is ",
        "who was ",
        "who created ",
        "where is ",
        "when was ",
        "why is ",
        "why are ",
        "how does ",
        "how do ",
        "how many ",
        "tell me about ",
        "can you explain ",
        "please explain ",
        "explain ",
    )

    def parse(self, command: str) -> ParsedCommand:
        """Parse a voice command into an action and argument."""

        command = " ".join(command.strip().lower().split())

        if not command:
            return ParsedCommand(action="empty")

        # ---------------------------------------------------------
        # EXIT
        # ---------------------------------------------------------

        if command in {
            "exit",
            "quit",
            "quite",
            "stop",
            "bye",
            "goodbye",
            "good bye",
            "shutdown",
        }:
            return ParsedCommand(action="exit")

        # ---------------------------------------------------------
        # EMAIL
        # ---------------------------------------------------------

        for prefix in self.EMAIL_PREFIXES:
            if command.startswith(prefix):
                argument = command[len(prefix):].strip()

                if argument.endswith(" for me"):
                    argument = argument[:-7].strip()

                return ParsedCommand(
                    action="email",
                    argument=argument,
                )

        # ---------------------------------------------------------
        # WEATHER
        # ---------------------------------------------------------

        for prefix in self.WEATHER_PREFIXES:
            if command.startswith(prefix):
                argument = command[len(prefix):].strip()

                if argument.startswith("like in "):
                    argument = argument[8:].strip()

                if argument.startswith("in "):
                    argument = argument[3:].strip()

                if argument.startswith("for "):
                    argument = argument[4:].strip()

                return ParsedCommand(
                    action="weather",
                    argument=argument.capitalize(),
                )

        if command in {
            "what is the weather",
            "what's the weather",
            "tell me the weather",
            "can you tell me the weather",
            "could you tell me the weather",
            "please tell me the weather",
            "check the weather",
            "please check the weather",
            "can you check the weather",
            "could you check the weather",
        }:
            return ParsedCommand(
                action="weather",
                argument="",
            )

        # ---------------------------------------------------------
        # TIMER
        # ---------------------------------------------------------

        timer_prefixes = (
            "could you set a timer for ",
            "can you set a timer for ",
            "would you set a timer for ",
            "please set a timer for ",
            "set a timer for ",
            "set a timer ",
            "set timer for ",
            "set timer ",
            "start a timer for ",
            "start a timer ",
            "start timer for ",
            "start timer ",
            "timer for ",
            "timer ",
        )

        for prefix in timer_prefixes:
            if command.startswith(prefix):
                time_part = command[len(prefix):].strip()
                time_words = time_part.split()

                if len(time_words) != 2:
                    continue

                try:
                    amount = int(time_words[0])
                except ValueError:
                    continue

                unit = time_words[1].lower()

                multipliers = {
                    "second": 1,
                    "seconds": 1,
                    "minute": 60,
                    "minutes": 60,
                    "hour": 3600,
                    "hours": 3600,
                }

                multiplier = multipliers.get(unit)

                if multiplier is None:
                    continue

                seconds = amount * multiplier

                return ParsedCommand(
                    action="timer",
                    argument=str(seconds),
                )

        if command in {
            "cancel timer",
            "cancel the timer",
            "stop timer",
            "stop the timer",
        }:
            return ParsedCommand(
                action="cancel_timer",
                argument="",
            )

        # ---------------------------------------------------------
        # REMINDER
        # ---------------------------------------------------------

        reminder_patterns = (
            "remind me to ",
            "reminder me to ",
            "please remind me to ",
            "set a reminder to ",
            "could you remaind me to ",
            "can you remaind me to ",
            "would you remaind to ",
            "i want you to remaind me to ",
        )

        for prefix in reminder_patterns:
            if not command.startswith(prefix):
                continue

            if " in " not in command:
                continue

            remainder = command[len(prefix):].strip()

            message, time_part = remainder.rsplit(" in ", 1)

            message = message.strip()
            time_words = time_part.strip().split()

            if len(time_words) != 2:
                continue

            try:
                amount = int(time_words[0])
            except ValueError:
                continue

            unit = time_words[1].lower()

            multipliers = {
                "second": 1,
                "seconds": 1,
                "minute": 60,
                "minutes": 60,
                "hour": 3600,
                "hours": 3600,
            }

            multiplier = multipliers.get(unit)

            if multiplier is None or not message:
                continue

            seconds = amount * multiplier

            return ParsedCommand(
                action="reminder",
                argument=f"{message}|{seconds}",
            )

        # ---------------------------------------------------------
        # LIST REMINDERS
        # ---------------------------------------------------------

        if command in {
            "show my reminders",
            "show reminders",
            "list my reminders",
            "list reminders",
        }:
            return ParsedCommand(
                action="list_reminders",
                argument="",
            )

        # ---------------------------------------------------------
        # CANCEL REMINDERS
        # ---------------------------------------------------------

        if command in {
            "cancel reminder",
            "cancel the reminder",
            "cancel reminders",
            "cancel all reminders",
            "delete reminder",
            "delete reminders",
        }:
            return ParsedCommand(
                action="cancel_reminder",
                argument="",
            )

        if command.startswith("cancel reminder "):
            reminder_id = command[len("cancel reminder "):].strip()

            if reminder_id.isdigit():
                return ParsedCommand(
                    action="cancel_reminder",
                    argument=reminder_id,
                )

        if command.startswith("cancel the reminder "):
            reminder_id = command[len("cancel the reminder "):].strip()

            if reminder_id.isdigit():
                return ParsedCommand(
                    action="cancel_reminder",
                    argument=reminder_id,
                )

        if command.startswith("delete reminder "):
            reminder_id = command[len("delete reminder "):].strip()

            if reminder_id.isdigit():
                return ParsedCommand(
                    action="cancel_reminder",
                    argument=reminder_id,
                )

        if command.startswith("delete the reminder "):
            reminder_id = command[len("delete the reminder "):].strip()

            if reminder_id.isdigit():
                return ParsedCommand(
                    action="cancel_reminder",
                    argument=reminder_id,
                )
        # ---------------------------------------------------------
        # NOTES
        # ---------------------------------------------------------

        note_prefixes = (
            "take a note ",
            "take note ",
            "make a note ",
            "make note ",
            "save a note ",
            "save note ",
            "write a note ",
            "write note ",
            "note ",
        )

        for prefix in note_prefixes:
            if command.startswith(prefix):
                argument = command[len(prefix):].strip()

                return ParsedCommand(
                    action="note",
                    argument=argument,
                )

        if command in {
            "take a note",
            "take note",
            "make a note",
            "make note",
            "save a note",
            "save note",
            "write a note",
            "write note",
        }:
            return ParsedCommand(
                action="note",
                argument="",
            )

        # ---------------------------------------------------------
        # LIST NOTES
        # ---------------------------------------------------------

        if command in {
            "show my notes",
            "show notes",
            "read my notes",
            "read notes",
            "list my notes",
            "list notes",
        }:
            return ParsedCommand(
                action="list_notes",
                argument="",
            )

        # ---------------------------------------------------------
        # CLEAR NOTES
        # ---------------------------------------------------------

        if command in {
            "clear my notes",
            "clear notes",
            "delete my notes",
            "delete notes",
            "remove my notes",
            "remove notes",
        }:
            return ParsedCommand(
                action="clear_notes",
                argument="",
            )

        # ---------------------------------------------------------
        # OPEN / START / LAUNCH
        # ---------------------------------------------------------

        for prefix in self.OPEN_PREFIXES:
            if command.startswith(prefix):
                argument = command[len(prefix):].strip()

                if argument.endswith(" for me"):
                    argument = argument[:-7].strip()

                if argument.startswith("the "):
                    argument = argument[4:].strip()

                if argument in self.APPLICATIONS:
                    return ParsedCommand(
                        action="open_application",
                        argument=argument,
                    )

                return ParsedCommand(
                    action="open",
                    argument=argument,
                )

        # ---------------------------------------------------------
        # SEARCH
        # ---------------------------------------------------------

        for prefix in self.SEARCH_PREFIXES:
            if command.startswith(prefix):
                argument = command[len(prefix):].strip()

                if prefix == "could you find ":
                    if argument.endswith(" online"):
                        argument = argument[:-7].strip()

                elif prefix in {
                    "can you find information about ",
                    "could you find information about ",
                    "please find information about ",
                    "find information about ",
                }:
                    argument = "information about " + argument

                elif prefix in {
                    "can you find information on ",
                    "could you find information on ",
                    "please find information on ",
                    "find information on ",
                }:
                    argument = "information on " + argument

                return ParsedCommand(
                    action="search",
                    argument=argument,
                )
        

        # ---------------------------------------------------------
        # GENERAL KNOWLEDGE
        # ---------------------------------------------------------

        for prefix in self.KNOWLEDGE_PREFIXES:
            if command.startswith(prefix):
                argument = command[len(prefix):].strip()

                if argument:
                    return ParsedCommand(
                        action="knowledge",
                        argument=command,
                    )



        # ---------------------------------------------------------
        # UNKNOWN
        # ---------------------------------------------------------

        return ParsedCommand(
            action="unknown",
            argument=command,
        )