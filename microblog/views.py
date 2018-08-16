from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def page_permission_denied(request):
    return HttpResponse('<h1 style="align:center">Permission denied</h1>')


def page_not_found(request):
    return HttpResponse('<h1 style="align:center">Not found</h1>')


def page_inter_error(request):
    return HttpResponse('<h1 style="align:center">Ohh, something error here!</h1>')