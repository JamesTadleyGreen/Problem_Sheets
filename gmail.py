from __future__ import print_function
import os.path
import base64

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient import errors

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import mimetypes
from email import encoders

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]


class Gmail:
    def __init__(self, mailing_list, file_list) -> None:
        self.mailing_list = mailing_list
        self.file_list = file_list

    def credentials(self):
        """Shows basic usage of the Gmail API.
        Lists the user's Gmail labels.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        service = build("gmail", "v1", credentials=creds)
        return service

    def create_message(
        self, sender, to, subject, message_text, attachments=None, images=None
    ):
        message = MIMEMultipart()
        message["bcc"] = ','.join(to)
        message["from"] = sender
        message["subject"] = subject

        if attachments is not None:
            for attachment in attachments:
                content_type, _ = mimetypes.guess_type(attachment)
                main_type, sub_type = content_type.split("/", 1)
                file_name = os.path.basename(attachment)

                f = open(attachment, "rb")

                myFile = MIMEBase(main_type, sub_type)
                myFile.set_payload(f.read())
                myFile.add_header(
                    "Content-Disposition", "attachment", filename=file_name
                )
                encoders.encode_base64(myFile)

                f.close()

                message.attach(myFile)

        if images is not None:
            for image in images:
                img_name = os.path.basename(image)
                html_img = MIMEText(
                    f'<p><img src="cid:{img_name}" /></p>', _subtype="html"
                )
                message.attach(html_img)

                i = open(image, "rb").read()
                img = MIMEImage(i, "png")
                img.add_header("Content-Id", f"<{img_name}>")
                img.add_header("Content-Disposition", "inline", filename=f"{img_name}")
                message.attach(img)

        message.attach(MIMEText(message_text, "html"))

        b64_bytes = base64.urlsafe_b64encode(message.as_bytes())
        b64_string = b64_bytes.decode()
        body = {"raw": b64_string}
        return body

    def create_draft(self, service, message_body, user_id: str = "me"):
        try:
            message = {"message": message_body}
            draft = (
                service.users().drafts().create(userId=user_id, body=message).execute()
            )

            return draft
        except errors.HttpError as error:
            return None

