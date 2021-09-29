from django import template

register = template.Library()

def plus_one(value):
    data = value + 1
    return data


def cut_url(raw_url):
    return raw_url.split('static/')[1]

register.filter('plus_one', plus_one)
register.filter('cut_url', cut_url)
