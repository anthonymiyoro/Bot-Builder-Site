from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from jobs.models import Location


def location_match_view(request, slug):
    try:
        instance = Location.objects.get(slug=slug)
    except Location.MultipleObjectsReturned:
        queryset = Location.objects.filter(slug=slug).order_by('-id')
        instance = queryset[0]
    except Location.DoesNotExist:
        raise Http404

    template = "matches/location_match_view.html"
    context = {
        "instance": instance,
    }
    return render(request, template, context)
