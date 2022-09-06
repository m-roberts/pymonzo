"""
Monzo API attachments resource.
"""
from typing import Dict

from pymonzo.resources import BaseResource


class AttachmentsResource(BaseResource):
    """
    Monzo API attachments resource.

    Docs:
        https://docs.monzo.com/#attachments
    """

    def upload(
        self,
        file_name: str,
        file_type: str,
        content_length: int,
    ) -> Dict[str, str]:
        """
        Upload an attachment.

        The response will include a 'file_url' which will be the URL of the resulting
        file, and an 'upload_url' to which the file should be uploaded to.

        Docs:
            https://docs.monzo.com/#upload-attachment
        """
        endpoint = "/attachment/upload"
        params = {
            "file_name": file_name,
            "file_type": file_type,
            "content_length": content_length,
        }
        response = self._get_response(method="post", endpoint=endpoint, params=params)

        return response.json()
