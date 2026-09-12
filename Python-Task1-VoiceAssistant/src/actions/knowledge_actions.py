import requests


class KnowledgeActions:
    """Provides general-knowledge answers using a local knowledge base
    with an optional Wikipedia fallback.
    """

    LOCAL_KNOWLEDGE = {
        "what is python": (
            "Python is a high-level programming language known for its "
            "simple syntax and wide use in web development, automation, "
            "data science, artificial intelligence, and software development."
        ),
        "who created python": (
            "Python was created by Guido van Rossum and was first released "
            "in 1991."
        ),
        "what is artificial intelligence": (
            "Artificial intelligence, or AI, is the field of creating "
            "computer systems that can perform tasks that normally require "
            "human intelligence, such as understanding language, learning, "
            "and making decisions."
        ),
        "what is ai": (
            "AI stands for artificial intelligence. It is technology that "
            "allows computers to perform tasks that normally require human "
            "intelligence."
        ),
        "what is machine learning": (
            "Machine learning is a branch of artificial intelligence where "
            "computers learn patterns from data and use those patterns to "
            "make predictions or decisions."
        ),
        "what is cpu": (
            "CPU stands for Central Processing Unit. It is the main "
            "processor of a computer and executes instructions from programs."
        ),
        "what is ram": (
            "RAM stands for Random Access Memory. It temporarily stores data "
            "that programs are actively using so the computer can access it quickly."
        ),
        "what is an operating system": (
            "An operating system is system software that manages computer "
            "hardware and provides services for applications. Examples include "
            "Windows, Linux, macOS, Android, and iOS."
        ),
        "what is github": (
            "GitHub is a platform for hosting Git repositories and "
            "collaborating on software projects."
        ),
        "what is git": (
            "Git is a distributed version control system used to track "
            "changes in source code and collaborate with other developers."
        ),
        "what is html": (
            "HTML stands for HyperText Markup Language. It is used to "
            "structure content on web pages."
        ),
        "what is css": (
            "CSS stands for Cascading Style Sheets. It is used to control "
            "the appearance and layout of web pages."
        ),
        "what is api": (
            "API stands for Application Programming Interface. It allows "
            "different software applications or services to communicate "
            "with each other."
        ),
        "what is database": (
            "A database is an organized collection of data that can be "
            "stored, managed, and retrieved efficiently."
        ),
        "what is python programming": (
            "Python programming means writing software using the Python "
            "programming language."
        ),
        "capital of india": "The capital of India is New Delhi.",
        "capital of tamil nadu": "The capital of Tamil Nadu is Chennai.",
        "largest planet": "Jupiter is the largest planet in our solar system.",
        "smallest planet": "Mercury is the smallest planet in our solar system.",
        "how many continents are there": (
            "There are seven continents: Asia, Africa, North America, "
            "South America, Antarctica, Europe, and Australia."
        ),
        "how many planets are there": (
            "There are eight recognized planets in our solar system."
        ),
    }

    def answer(self, question: str) -> str:
        """Return an answer for a general-knowledge question."""

        normalized = " ".join(question.lower().strip().split())

        if normalized in self.LOCAL_KNOWLEDGE:
            return self.LOCAL_KNOWLEDGE[normalized]

        return self._wikipedia_fallback(question)

    def _wikipedia_fallback(self, question: str) -> str:
        """Try to answer unknown questions using Wikipedia."""

        try:
            response = requests.get(
                "https://en.wikipedia.org/api/rest_v1/page/summary/"
                + requests.utils.quote(question),
                timeout=5,
            )

            if response.status_code != 200:
                return (
                    "I don't have enough information to answer that "
                    "question."
                )

            data = response.json()
            extract = data.get("extract", "").strip()

            if not extract:
                return (
                    "I don't have enough information to answer that "
                    "question."
                )

            return extract

        except requests.RequestException:
            return (
                "I couldn't find an answer right now. "
                "Please try the question again."
            )