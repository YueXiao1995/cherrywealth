from django.shortcuts import get_object_or_404, render
from .models import Person
# Create your views here.

from django.http import HttpResponse
def index(request):
    person_list = Person.objects.order_by('-rank')[:5]
    context = {'person_list': person_list}
    for person in person_list:
        print(person.name)
    return render(request, 'fuhaobang/fuhaobang.html', context)

def detail(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    event_list = person.event_set.order_by('-time')
    return render(request, 'fuhaobang/detail.html', {'person': person, 'event_list': event_list})
