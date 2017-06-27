from syncapp.mapper import get_maps
from django.views.generic import TemplateView


class ResultView(TemplateView):
    template_name = 'result.html'

    def get_context_data(self, **kwargs):
        audio_url = 'data/audio.mp3'
        text = open('data/content15.html', 'r').read()
        result_json, map_table = get_maps(text, audio_url)
        return {'audio': audio_url, 'map_table': map_table, 
                'audio_json': result_json, 'text': text}
