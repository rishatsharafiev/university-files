from celery import shared_task
from utils.helper import download_file

from .success import success_task


@shared_task(bind=True, max_retries=3)
def download_task(self, url, source):
    """Download file by url"""
    absolute_url = None

    try:
        absolute_url = download_file(url)
    except Exception:
        self.retry(countdown=1)

    if absolute_url:
        success_task.delay(absolute_url, source)
    else:
        self.retry(countdown=1)
