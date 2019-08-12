import requests


class HTTPRequestManager:

    @staticmethod
    def download_pg_source_as_file(url: str, local_path: str, encoding='utf-8') -> None:
        response = requests.get(url)
        with open(local_path, 'w') as file_written:
            file_written.write(response.content.decode(encoding))
