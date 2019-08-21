import requests
import logging
from typing import Optional, Union
from healint_data_toolkit.constants import HTTPRequestPageSourceOutput
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class HTTPRequestManager:

    @staticmethod
    def get_response(
            url: str,
            local_path: str = None,
            output: str = 'STRING',
            encoding='utf-8'
    ) -> Optional[Union[str, BeautifulSoup]]:
        response = requests.get(url)

        if not str(response.status_code).startswith("2"):
            logger.warning("Response status code does not start with 2")

        string_response = response.content.decode(encoding)
        output_format = HTTPRequestPageSourceOutput(output)

        if output_format == HTTPRequestPageSourceOutput.FILE:

            if local_path is None:
                raise Exception("You must define a local path for file output format")

            with open(local_path, 'w') as file_written:
                file_written.write(string_response)

        elif output_format == HTTPRequestPageSourceOutput.STRING:
            return string_response

        elif output_format == HTTPRequestPageSourceOutput.SOUP:
            return BeautifulSoup(string_response)

        elif output_format == HTTPRequestPageSourceOutput.JSON:
            return response.json()

        else:
            raise Exception("Unknown output format. ")


