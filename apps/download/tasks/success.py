import requests
from celery import shared_task
from conf import settings


@shared_task(bind=True, max_retries=3)
def success_task(self, absolute_url, source):
    """Send success event to topic"""
    try:
        response = requests.post(settings.WEBHOOK_URL, json={'url': absolute_url, 'source': source})
        return response.status_code
    except Exception:
        self.retry(countdown=1)
