from django.shortcuts import render, redirect


def base(request):
    return render(request, 'main_page/base.html')
