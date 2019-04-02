import json
import logging

from django import views
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class WebhookView(views.View):
    """Webhook View"""

    logger = logging.getLogger(__name__)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """Dispatch method"""
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        """Post"""
        try:
            message = json.loads(request.body)
            if 'action' in message and message.get('action') == 'download' \
                    and 'source' in message and 'url' in message:
                self.logger.debug(f'--> {message}')
        except json.decoder.JSONDecodeError:
            return HttpResponse('JSONDecodeError', status=500)
        return HttpResponse(f'Ok {url}')
