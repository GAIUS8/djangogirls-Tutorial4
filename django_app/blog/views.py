from django.http import HttpResponse
from django.shortcuts import render


def main_view(request):
    return HttpResponse('gogogogogogogogogo')

def main_view2(request):
    return HttpResponse('this Response from main_view2')