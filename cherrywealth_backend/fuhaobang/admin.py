from django.contrib import admin
from .models import Person, Event, Link
# Register your models here.


#admin.site.register(Person)
#admin.site.register(Event)


class EventInLine(admin.StackedInline):
    model = Event
    extra = 0


class LinkInLine(admin.StackedInline):
    model = Link
    extra = 0


class PersonAdmin(admin.ModelAdmin):
    inlines = [EventInLine, LinkInLine]
    #inlines = [LinkInLine]

admin.site.register(Person, PersonAdmin)
