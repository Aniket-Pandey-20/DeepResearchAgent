import os
from typing import Dict

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from agents import Agent, function_tool
from agent_config import gemini_model
from dotenv import load_dotenv

load_dotenv()

@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """Send an email with the given subject and HTML body using SMTP."""
    sender_email = "aniketpandey658@gmail.com"
    receiver_email = "aniket.study658@gmail.com"
    app_password = os.environ['APP_PASSWORD']

    # Create the email
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.attach(MIMEText(html_body, "html"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("✅ Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)


INSTRUCTIONS = """You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the 
report converted into clean, well presented HTML with an appropriate subject line."""

email_agent = Agent(
    name="Email agent",
    instructions=INSTRUCTIONS,
    tools=[send_email],
    model=gemini_model,
)