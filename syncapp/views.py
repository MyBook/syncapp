from django.template.response import TemplateResponse


def index_page(request):
    return TemplateResponse(request, 'index.html', {})
