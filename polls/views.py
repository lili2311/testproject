# Create your views here.
from django.http import HttpResponse
from polls.models import Poll
from django.template import Context, loader
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
#def index(request):
#    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#    output = ', '.join([p.question for p in latest_poll_list])
#    return HttpResponse(output)
def index(request):
        latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
        t = loader.get_template('index.html')
        c = Context({
            'latest_poll_list': latest_poll_list,
        })
        return HttpResponse(t.render(c))
def detail(request, poll_id):
        p = get_object_or_404(Poll, pk=poll_id)
        return render_to_response('detail.html', {'poll': p})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
