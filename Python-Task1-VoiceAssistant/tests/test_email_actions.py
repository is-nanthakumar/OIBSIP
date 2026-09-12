import smtplib
from unittest.mock import MagicMock, patch

from src.actions.email_actions import EmailActions


def test_send_email_success():
    with patch.dict(
        "os.environ",
        {
            "EMAIL_SMTP_SERVER": "smtp.gmail.com",
            "EMAIL_SMTP_PORT": "587",
            "EMAIL_SENDER": "sender@example.com",
            "EMAIL_PASSWORD": "test-password",
        },
    ):
        action = EmailActions()

        with patch(
            "src.actions.email_actions.smtplib.SMTP"
        ) as mock_smtp:
            mock_server = MagicMock()
            mock_smtp.return_value.__enter__.return_value = mock_server

            response = action.send_email(
                "receiver@example.com",
                "Test Subject",
                "Hello from the voice assistant.",
            )

            mock_smtp.assert_called_once_with(
                "smtp.gmail.com",
                587,
                timeout=10,
            )

            mock_server.starttls.assert_called_once()
            mock_server.login.assert_called_once_with(
                "sender@example.com",
                "test-password",
            )
            mock_server.send_message.assert_called_once()

        assert response == (
            "Email sent successfully to receiver@example.com."
        )


def test_send_email_requires_configuration():
    with patch.dict(
        "os.environ",
        {},
        clear=True,
    ):
        action = EmailActions()

        response = action.send_email(
            "receiver@example.com",
            "Test Subject",
            "Hello",
        )

    assert response == (
        "Email is not configured. "
        "Please configure the email credentials first."
    )


def test_send_email_requires_recipient():
    with patch.dict(
        "os.environ",
        {
            "EMAIL_SENDER": "sender@example.com",
            "EMAIL_PASSWORD": "test-password",
        },
    ):
        action = EmailActions()

        response = action.send_email(
            "",
            "Test Subject",
            "Hello",
        )

    assert response == "Please tell me the recipient email address."


def test_send_email_handles_smtp_error():
    with patch.dict(
        "os.environ",
        {
            "EMAIL_SENDER": "sender@example.com",
            "EMAIL_PASSWORD": "test-password",
        },
    ):
        action = EmailActions()

        with patch(
            "src.actions.email_actions.smtplib.SMTP",
            side_effect=smtplib.SMTPException("connection failed"),
        ):
            response = action.send_email(
                "receiver@example.com",
                "Test Subject",
                "Hello",
            )

    assert response == (
        "Unable to send email: connection failed"
    )