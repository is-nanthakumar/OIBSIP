import os
import smtplib
from email.message import EmailMessage


class EmailActions:
    """Handles sending emails through SMTP."""

    def __init__(self):
        self.smtp_server = os.getenv(
            "EMAIL_SMTP_SERVER",
            "smtp.gmail.com",
        )
        self.smtp_port = int(
            os.getenv(
                "EMAIL_SMTP_PORT",
                "587",
            )
        )
        self.sender_email = os.getenv("EMAIL_SENDER")
        self.sender_password = os.getenv("EMAIL_PASSWORD")

    def send_email(
        self,
        recipient: str,
        subject: str,
        body: str,
    ) -> str:
        """Send an email using configured SMTP credentials."""

        if not self.sender_email or not self.sender_password:
            return (
                "Email is not configured. "
                "Please configure the email credentials first."
            )

        if not recipient:
            return "Please tell me the recipient email address."

        if not subject:
            return "Please tell me the email subject."

        if not body:
            return "Please tell me what you want me to say in the email."

        message = EmailMessage()
        message["From"] = self.sender_email
        message["To"] = recipient
        message["Subject"] = subject
        message.set_content(body)

        try:
            with smtplib.SMTP(
                self.smtp_server,
                self.smtp_port,
                timeout=10,
            ) as server:
                server.starttls()
                server.login(
                    self.sender_email,
                    self.sender_password,
                )
                server.send_message(message)

            return f"Email sent successfully to {recipient}."

        except (smtplib.SMTPException, OSError) as error:
            return f"Unable to send email: {error}"