import requests
from typing import Optional
from healint_data_toolkit.constants import HTTPRequestPageSourceOutput


class HTTPRequestManager:

    @staticmethod
    def download_pg_source(
            url: str,
            local_path: str,
            output: str = 'string',
            encoding='utf-8'
    ) -> Optional[str]:
        response = requests.get(url)

        if output == HTTPRequestPageSourceOutput.FILE.value:

            with open(local_path, 'w') as file_written:
                file_written.write(response.content.decode(encoding))

        elif output == HTTPRequestPageSourceOutput.STRING.value:

            return response.content


