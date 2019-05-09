from django.apps import apps
from django.http import HttpResponse
from django.core.serializers import serialize


def home(request, app, model, pk=None):
    rel = request.GET.get('rel', None)
    fmt = request.GET.get('fmt', 'json')

    model = apps.get_model(f'{app}.{model}')
    qs = model.objects.all()

    if pk:
        qs = qs.filter(pk=pk)

    if rel:
        related = rel.split(',')
        qs = qs.select_related(*related)

    return HttpResponse(serialize(fmt, qs), content_type=f'application/{fmt}')

