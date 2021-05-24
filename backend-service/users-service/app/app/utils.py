from typing import Any, Dict, Optional


def send_email(
        email_to: str,
        subject_template: str = "",
        html_template: str = "",
        environment: Dict[str, Any] = {},
) -> None:
    pass


def send_test_email(email_to: str) -> None:
    pass


def send_reset_password_email(email_to: str, email: str, token: str) -> None:
    pass


def send_new_account_email(email_to: str, username: str, password: str) -> None:
    pass


def generate_password_reset_token(email: str) -> str:
    pass


def verify_password_reset_token(token: str) -> Optional[str]:
    pass
