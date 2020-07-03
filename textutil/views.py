
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    onlyoneline = request.POST.get('onlyoneline', 'off')
    charcount = request.POST.get('charcount', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed =""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'remove punctuation','analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on" :
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'full capitalized', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'new line remove', 'analyzed_text': analyzed}
        djtext = analyzed



    if (extraspaceremove == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'extra space remove', 'analyzed_text': analyzed}


    if(removepunc != "on" and newlineremove != "on" and extraspaceremove != "on" and fullcaps != "on"):
        return HttpResponse("please select any method")

    return render(request, 'analyze.html', params)






# def capfirst(request):
#     return HttpResponse("capitlaized first")
# def newlineremove(request):
#     return HttpResponse("new line remover first")
#
# def spaceremove(request):
#     return HttpResponse("space remove first")
# def charcount(request):
#     return HttpResponse("char count first")
#
