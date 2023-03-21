import os

from flask_mail import Message
from flask import current_app, url_for

from pupsite import mail


class SendMail:
    """
    Will be used to send mail with the given message and html
    """

    def __init__(self, subject, recipients=None, sender=None):
        """
        Instantiate the mail object to be used to send mail

        Args:
            subject(str) : The subject of the message to be sent
            recipients(list) : a list of members to send the email to

        """
        self.sender = current_app.config.get("MAIL_USERNAME") if not sender else sender
        self.subject = subject
        self.recipients = [] if not recipients else recipients

    def send_mail(self, html=None, token=None):
        """
        Send a Message with the given message using the given html Template
        Args:
            html (str) : the html template to use in the message
            token (str): the authentication token used in the request
        Returns:
             bool : True for success and False otherwise
        """
        body = f"""
                To reset the password, Just click
                 <a href='{url_for("memberblueprint.reset_password", token=token, _external=True)}'>here</a>
            """
        html = f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>Paasword reset</title>
            </head>
            <body>
                <h1>Please reset your password</h1>
                <div>
                <P>
                {body}
                </P>
                </div>
            </body>
        </html>
        """

        message = Message(
            subject=self.subject,
            recipients=self.recipients,
            body=body,
            html=html,
            sender=self.sender
        )
        mail.send(message=message)
