# Manually created file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name': 'aniket', 'place': 'pune'}
    return render(request, 'index.html',params)
    # return HttpResponse("Home")

def analyze(request):
    backtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    print(removepunc)
    print(backtext)

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in backtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        backtext = analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps == "on":
        analyzed = ""
        for char in backtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        backtext = analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover == "on":
        analyzed = ""
        for char in backtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        backtext = analyzed
        # return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(backtext):
            if not (backtext[index] == " " and backtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Extraspace remover', 'analyzed_text': analyzed}

    if(extraspaceremover!="on" and newlineremover != "on" and fullcaps != "on" and removepunc != "on"):
        return HttpResponse("Error")


    return render(request, 'analyze.html', params)
