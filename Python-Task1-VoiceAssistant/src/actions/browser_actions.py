import webbrowser
from urllib.parse import quote_plus


class BrowserActions:
    """Handles browser-based actions."""

    WEBSITES = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://github.com",
        "linkedin": "https://www.linkedin.com",
        "gmail": "https://mail.google.com",
        "whatsapp": "https://web.whatsapp.com",
        
    }

    def open_website(self, website: str) -> str:
        """Open a supported website in the default browser."""

        website = website.strip().lower()

        url = self.WEBSITES.get(website)

        if not url:
            return f"I don't know how to open {website}."

        webbrowser.open(url)

        return f"Opening {website}."

    def search_web(self, query: str) -> str:
        """Search the web using the default browser."""

        query = query.strip()

        if not query:
            return "Please tell me what you want me to search for."

        encoded_query = quote_plus(query)
        url = f"https://www.google.com/search?q={encoded_query}"

        webbrowser.open(url)

        return f"Searching the web for {query}."