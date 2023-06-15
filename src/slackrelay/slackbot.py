from io import StringIO  # this library will allow us to

import requests
import slack_sdk


class SlackMessenger:
    def __init__(self, token, channel):
        self.token = token
        self.channel = channel

        self.client = slack_sdk.WebClient(token=token)

    def message(self, message, thread=None, files=None, attachments=None):
        # data = {
        #    "token": self.token,
        #    "channel": self.channel,
        #    "as_user": True,
        #    "text": message,
        # }
        # if attachments:
        #    data["attachments"] = attachments

        if files:
            for file in files:
                upload = self.client.files_upload_v2(file=file, filename=file)
                message = message + "<" + upload["file"]["permalink"] + "| >"

        # print (data)
        # r = requests.post(url="https://slack.com/api/chat.postMessage", data=data)

        r = self.client.chat_postMessage(
            channel=self.channel, text=message, thread_ts=thread
        )

        return r

    def attach_file(self, file_path: str, thread: str):
        # https://stackoverflow.com/questions/43464873/how-to-upload-files-to-slack-using-file-upload-and-requests
        # https://api.slack.com/methods/files.upload

        url = "https://slack.com/api/files.upload"

        # params = {
        #    "channels":[self.channel],
        #    "file":file_path,
        #    "ts":thread
        # }

        # files = {
        #  file_path : (file_path, open(file_path, 'r'), 'csv')
        # }

        sio = StringIO()
        # pd.read_csv(file_path).to_csv(sio)
        csv_content = sio.getvalue()

        request_data = {
            "channels": [self.channel],
            "content": csv_content,  # required
            "filename": file_path,  # required
            "filetype": "csv",  # helpful :)
            "text": "File uploaded",  # optional
            "title": file_path,  # optional
        }

        headers = {
            "Authorization": f"Bearer {self.token}",
        }

        r = requests.post(url=url, data=request_data, headers=headers)

        r.raise_for_status()

        return r
