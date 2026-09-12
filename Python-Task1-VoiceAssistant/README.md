# Voice Assistant

A Python-based voice assistant that listens to spoken commands, converts speech into text, understands natural language variations, performs useful actions, and responds using spoken audio.

This project was developed as part of the **OASIS Infobyte Python Programming Internship — Task 1: Voice Assistant**.

## Features

* Voice input through the microphone
* Speech-to-text using `SpeechRecognition`
* Natural language command handling
* Multiple variations for common commands
* Greetings and identity responses
* Current time and date
* Live weather information
* Web search
* Website opening
* Windows application launching

  * Calculator
  * Notepad
  * File Explorer
* Conversational email sending
* Timed reminders
* Timers
* Personal notes
* General-knowledge question answering
* Local knowledge base with Wikipedia fallback
* Custom voice commands through JSON configuration
* Help commands
* Exit commands
* Local Windows text-to-speech
* Speech recognition error handling
* Retry handling for repeated failed inputs
* Unit and integration testing with `pytest`

## How It Works

```text
Microphone
    ↓
Speech Recognition
    ↓
Command Processor
    ↓
Custom Commands
    ↓
Command Parser
    ↓
Intent / Command
    ↓
Action Layer
    ↓
Response
    ↓
Windows Text-to-Speech
    ↓
Speaker
```

## Main Components

### `SpeechRecognizer`

Captures spoken input through the microphone and converts speech into text using Google's speech recognition service.

The assistant also calibrates the microphone for ambient noise and handles speech-recognition failures gracefully.

### `CommandParser`

Converts natural voice commands into structured commands.

Example:

```text
User:
Could you please search for Python tutorials?

Parsed command:
action = "search"
argument = "python tutorials"
```

The parser supports multiple natural variations of the same command instead of relying on a single exact phrase.

### `CommandProcessor`

Acts as the central command-routing layer.

It determines which action should be executed and manages conversational flows such as email composition.

It also coordinates:

* Built-in commands
* Custom commands
* General-knowledge questions
* Weather requests
* Reminders
* Timers
* Notes
* Email conversations

### `BrowserActions`

Handles:

* Opening websites
* Performing web searches

### `SystemActions`

Handles:

* Current time
* Current date
* Opening supported Windows applications

Supported applications include:

* Calculator
* Notepad
* File Explorer

### `WeatherActions`

Handles weather-related commands and retrieves current weather information for a requested location.

### `EmailActions`

Handles conversational email composition and sending.

Example flow:

```text
User:
Send an email to test@example.com

Assistant:
I have the recipient address. Please provide the email subject and message.

User:
Project update

Assistant:
Got it. What should I say in the email?

User:
The project has been completed.

Assistant:
Email sent successfully.
```

Email conversations can also be cancelled.

### `ReminderActions`

Provides timed reminder functionality.

Supports:

* Creating reminders
* Listing active reminders
* Cancelling reminders
* Cancelling reminders by ID
* Triggering reminder callbacks

### `TimerActions`

Provides timer functionality for timed tasks and notifications.

### `NotesActions`

Provides simple personal note functionality.

Supports:

* Creating notes
* Viewing notes
* Clearing notes

Notes are stored locally in:

```text
notes.txt
```

### `KnowledgeActions`

Provides general-knowledge question answering.

The assistant includes a lightweight local knowledge base for common questions and can use Wikipedia as a fallback for questions that are not available locally.

Example:

```text
User:
What is Python?

Assistant:
Python is a high-level programming language known for its
simple syntax and wide use in web development, automation,
data science, artificial intelligence, and software development.
```

Other examples include:

```text
Who created Python?
What is artificial intelligence?
What is machine learning?
What is CPU?
What is RAM?
What is GitHub?
What is an API?
What is the capital of India?
How many planets are there?
```

### `CustomCommands`

Allows users to define their own voice commands through:

```text
custom_commands.json
```

Example:

```json
{
    "study mode": {
        "action": "response",
        "value": "Study mode activated. Focus and do your best."
    },
    "motivate me": {
        "action": "response",
        "value": "Keep going. Small progress every day leads to big results."
    }
}
```

The user can then say:

```text
study mode
```

and the assistant responds with the configured message.

Custom commands are intentionally limited to safe predefined actions rather than arbitrary system command execution.

### `TextToSpeech`

Converts assistant responses into spoken audio using the Windows native:

```text
System.Speech.Synthesis.SpeechSynthesizer
```

Text-to-speech runs locally on Windows and does not require a separate cloud TTS service.

### `VoiceAssistant`

Coordinates the complete voice-assistant loop:

```text
Listen → Process → Respond → Continue
```

It also handles repeated failed speech-recognition attempts.

## Supported Commands

### Greetings

```text
hello
hi
hey
good morning
good afternoon
good evening
```

### Identity

```text
what is your name
who are you
```

### Time

```text
what is the time
what's the time
tell me the time
current time
```

### Date

```text
what is the date
what is today's date
what's today's date
tell me today's date
current date
```

### Weather

```text
what is the weather in Chennai
what's the weather like in Chennai
tell me the weather in Chennai
check the weather in Chennai
weather in Chennai
could you tell me the weather in Bangalore
```

### Web Search

```text
search python tutorials
search for machine learning
please search for Python tutorials
please search the web for Python tutorials
can you search Google for Python
can you find python tutorials online
can you find information about Python
look up Python programming
could you please search for Python tutorials
```

### Open Websites

```text
open youtube
please open gmail
please open whatsapp
could you please open youtube
would you mind opening youtube
```

### Open Applications

```text
open calculator
open calc
open notepad
open file explorer
open explorer
open the calculator
please open the notepad
can you open the file explorer
please start the calculator
could you launch notepad
```

### Email

Start an email conversation with:

```text
send an email to test@example.com
```

The assistant collects the subject and message conversationally.

Cancel an email conversation with:

```text
cancel
cancel email
stop email
```

### Reminders

```text
remind me to call John in 60 seconds
please remind me to check the project in 5 minutes
set a reminder to take a break in 1 hour
```

Supported time units:

```text
seconds
minutes
hours
```

Reminder management:

```text
show my reminders
list reminders
cancel reminder
cancel reminder 1
```

### Timers

```text
set a timer for 10 seconds
start a timer for 5 minutes
set timer for 1 hour
```

Cancel a timer:

```text
cancel timer
stop timer
```

### Notes

Create a note:

```text
take a note buy milk
make a note call John
save note finish project
write a note complete the assignment
```

View notes:

```text
show my notes
show notes
read my notes
read notes
list my notes
```

Clear notes:

```text
clear my notes
clear notes
delete my notes
remove my notes
```

### General Knowledge

```text
what is Python
who created Python
what is artificial intelligence
what is machine learning
what is CPU
what is RAM
what is GitHub
what is an API
what is the capital of India
how many planets are there
can you explain machine learning
tell me about databases
```

### Custom Commands

Example configured commands:

```text
study mode
start coding
motivate me
good night
```

Custom commands can be changed by editing:

```text
custom_commands.json
```

### Help

```text
help
what can you do
please help me
can you help me
what can you help me with
```

### Exit

```text
exit
quit
bye
goodbye
stop
shutdown
```

## Project Structure

```text
Python-Task1-VoiceAssistant/
│
├── src/
│   ├── __init__.py
│   ├── assistant.py
│   │
│   ├── actions/
│   │   ├── __init__.py
│   │   ├── browser_actions.py
│   │   ├── custom_commands.py
│   │   ├── email_actions.py
│   │   ├── knowledge_actions.py
│   │   ├── notes_actions.py
│   │   ├── reminder_actions.py
│   │   ├── system_actions.py
│   │   ├── timer_actions.py
│   │   └── weather_actions.py
│   │
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── command_parser.py
│   │   └── command_processor.py
│   │
│   └── speech/
│       ├── __init__.py
│       ├── speech_recognizer.py
│       └── text_to_speech.py
│
├── tests/
│   ├── test_assistant.py
│   ├── test_browser_actions.py
│   ├── test_command_parser.py
│   ├── test_command_processor.py
│   ├── test_email_actions.py
│   ├── test_notes_actions.py
│   ├── test_reminder_actions.py
│   ├── test_speech_recognizer.py
│   ├── test_system_actions.py
│   ├── test_text_to_speech.py
│   ├── test_timer_actions.py
│   └── test_weather_actions.py
│
├── custom_commands.json
├── .gitignore
├── README.md
├── requirements.txt
└── requirements-dev.txt
```

## Requirements

* Python 3.11+
* Windows operating system
* Working microphone
* Speakers or headphones
* Internet connection for Google speech recognition
* Internet connection for web search and weather services
* Email configuration for email functionality

## Installation

Create a virtual environment:

```powershell
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

Install runtime dependencies:

```powershell
pip install -r requirements.txt
```

Install development and testing dependencies:

```powershell
pip install -r requirements-dev.txt
```

## Run the Assistant

Start the voice assistant with:

```powershell
python -m src.assistant
```

The assistant will start listening through the microphone and respond using spoken audio.

## Testing

Run the complete automated test suite:

```powershell
python -m pytest -q
```

Current test status:

```text
180 passed
```

The automated test suite covers:

* Command parsing
* Natural language command variations
* Command processing
* General-knowledge routing
* Custom commands
* Browser actions
* System actions
* Weather actions
* Email actions
* Reminder actions
* Timer actions
* Notes actions
* Speech recognition
* Text-to-speech
* Voice assistant integration
* Error handling

## Error Handling

The assistant handles:

* No speech detected
* Unrecognized speech
* Speech recognition service errors
* Empty commands
* Unknown commands
* Repeated failed recognition attempts
* Unsupported applications
* Invalid reminder durations
* Empty notes
* Cancelled email conversations

After repeated failed speech-recognition attempts, the assistant informs the user and continues listening.

## Speech Recognition

Speech-to-text currently uses:

```python
recognize_google()
```

Therefore, speech recognition requires an internet connection and is not fully offline.

## Text-to-Speech

Text-to-speech is handled locally using Windows Speech Synthesis:

```text
System.Speech.Synthesis.SpeechSynthesizer
```

No external cloud TTS service is required.

## Dependencies

### Runtime

```text
SpeechRecognition==3.17.0
PyAudio==0.2.14
requests==2.34.2
```

### Development

```text
pytest==9.1.1
```

## Testing Approach

The project uses automated unit and integration tests to verify individual components and their interactions.

The complete test suite currently passes:

```text
180 passed
```

This provides automated coverage across the main assistant components and command flows.

## Privacy

The assistant is designed to keep text-to-speech processing local through Windows Speech Synthesis.

However, speech recognition currently uses Google's speech recognition service through `SpeechRecognition`, so spoken input is sent to the external speech-recognition service for transcription.

Web search and weather functionality also require internet access.

Email functionality requires the user's configured email service and credentials.

Users should avoid speaking or storing sensitive information through commands unless they understand the external services involved.

## OASIS Infobyte Task 1

This project implements the main requirements of the OASIS Infobyte Python Programming Internship Task 1: Voice Assistant, including:

* Microphone-based voice input
* Speech-to-text conversion
* Command processing
* Natural language command variations
* Greeting responses
* Time and date information
* Weather information
* Web search
* Website opening
* Application launching
* Text-to-speech responses
* Error handling
* Automated testing

Additional functionality implemented:

* Conversational email sending
* Timed reminders
* Timers
* Personal notes
* General-knowledge question answering
* Custom voice commands
* Improved natural language command handling

## Project Status

```text
Voice input / speech recognition     Complete
Command parsing                      Complete
Natural language handling            Complete
Command processing                   Complete
Browser actions                      Complete
System actions                       Complete
Weather support                      Complete
Email support                        Complete
Reminder support                     Complete
Timer support                        Complete
Notes support                        Complete
General knowledge                    Complete
Custom commands                      Complete
Text-to-speech                       Complete
Error handling                       Complete
Automated testing                    180/180 passed
Documentation                        Complete
```

## Current Status

The project is fully implemented with the current automated test suite passing successfully.

```text
180 passed
```

The assistant is ready for final demonstration, GitHub submission, and project presentation.
