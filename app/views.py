from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from app.models import Match

@login_required
def index(request):
    matches_list = Match.objects.order_by('date')
    template = loader.get_template('app/index.html')
    context = {
        'matches_list': matches_list,
    }
    return HttpResponse(template.render(context, request))