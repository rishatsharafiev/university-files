import uuid
import os
from urllib.parse import urlparse
import requests

from conf import settings


def download_file(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        path = urlparse(url).path
        path_list = os.path.splitext(path)
        if len(path_list) >= 2:
            extension = path_list[1]
        else:
            extension = 'bin'
        filename = f'{uuid.uuid4()}{extension}'
        url_path = os.path.join(settings.MEDIA_URL, filename)
        file_path = os.path.join(settings.MEDIA_ROOT, filename)
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        return url_path, file_path
