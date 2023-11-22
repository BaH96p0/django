from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def main(request, name, work, interest):
    return HttpResponse(f'<h2>My name is: {name}</h2> <br> <h2>I work as a {work}</h2> <br> <h2>I like to {interest}</h2>')


def about(request, wherefrom, grades, study):
    return HttpResponse(f'<h2>I am from {wherefrom}</h2> <br> <h2>I have a {grades} grades at school </h2> <br> <h2>I {study} to study </h2>')


def contacts(request, github, tg, email):
    return HttpResponse(f'<h2>Github: {github}</h2> <br> <h2>Telegram: {tg}</h2> <br> <h2>e-mail: {email}</h2>')

