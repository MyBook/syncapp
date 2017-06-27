from syncapp.mapper import get_maps
from django.views.generic import TemplateView
from django.conf import settings
import os
import json


class ResultView(TemplateView):
    template_name = 'result.html'

    def get_context_data(self, **kwargs):
        audio_url = 'audio.mp3'
        text = 'content15.html'
        text_content = open(os.path.join(settings.MEDIA_ROOT, text), 'r').read()
        audio_path = os.path.join(settings.MEDIA_ROOT, audio_url)
        result_json, id_to_xpath = get_maps(text_content, audio_path)
        return {'audio': audio_url,
                'id_to_xpath': json.dumps(id_to_xpath),
                'xpath_to_id': json.dumps({val: key for key, val in id_to_xpath.items()}),
                'audio_json': result_json, 'text': text}
