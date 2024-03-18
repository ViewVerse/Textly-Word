from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    prams={'name':'Qtm', 'place':'Mars'}
    return render(request,'index.html',prams)
def analyze(request):

    #Get the text
    djtext=request.POST.get('text','default')

    #Check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')

    org=djtext
    open=False
    purpose=''
    #Check which & how many checkboxes is on...
    if removepunc=="on":
        purpose+='Removed Punctuations, '
        open=True
        analyzed=''
        punctuations='''!()-+[]{}=;:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        djtext=analyzed        

    if (fullcaps=='on'):
        purpose+='Changed To Upper Case, '
        open=True
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
        djtext=analyzed

    if (newlineremover=='on'):
        purpose+='Remove New Lines, '
        open=True
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        djtext=analyzed

    if (extraspaceremover=='on'):
        purpose+='Remove Extra Spaces, '
        open=True
        analyzed=""
        for index,char in enumerate(djtext):
            '''if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed=analyzed+char'''
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        djtext=analyzed

    n=0      
    if (charcount=='on'):
        purpose+='No. Of Characters'
        open=True
        for char in org:
           n+=1

    if open:
        params = {'purpose':purpose,'analyzed_text':djtext,'charcount':n}
        return render(request,'analyze.html',params)   
    else:
        return HttpResponse('Error')