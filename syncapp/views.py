from syncapp.mapper import get_maps
from django.views.generic import TemplateView


class ResultView(TemplateView):
    template_name = 'result.html'

    def get_context_data(self, **kwargs):
        audio_url = 'audio.mp3'
        text = 'content15.html'
        result_json, map_table = None, None #get_maps(text, audio_url)
        return {'audio': audio_url, 'map_table': map_table, 
                'audio_json': result_json, 'text': text}
