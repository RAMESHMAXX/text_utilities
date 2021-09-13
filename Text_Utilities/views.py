from django.shortcuts import render
from django.http import HttpResponse
import string

def index(request):
    return render(request,'index.html')

def analyze(request):
    text=request.POST.get('textarea','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get("UPPERCASE",'off')
    newlineremover=request.POST.get("newline",'off')
    extraspaceremover=request.POST.get("extraspaceremover",'off')
    charcount=request.POST.get('charcount','off')

    param={}
    if(removepunc=='on'):
        analyzed = ""
        for i in text:
            if(i not in string.punctuation):
                analyzed=analyzed+i

        param = {'purpose': 'Remove Punctuation', 'analyzed_sentence': analyzed}
        text=analyzed

        #return render(request, 'analyze.html', param)

    if(fullcaps=='on'):
        analyzed=""
        for j in text:
            analyzed=analyzed+j.upper()
        param = {'purpose': 'UPPERCASE', 'analyzed_sentence': analyzed}
        text=analyzed;
        #return render(request, 'analyze.html', param)

    if(newlineremover=="on"):
        analyzed = ""
        for j in text:
            if(j !='\n' and j !='\r'):
                analyzed = analyzed + j
        param = {'purpose': 'Remove new line', 'analyzed_sentence': analyzed}
        text=analyzed
        #return render(request, 'analyze.html', param)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index,k in enumerate(text):
            if (text[index]==" " and text[index+1]==" "):
                pass
            else:
                analyzed = analyzed + k

        param = {'purpose': 'Remove Extra space', 'analyzed_sentence': analyzed}
        text=analyzed
        #return render(request, 'analyze.html', param)
    if(charcount=="on"):
        count=0
        for data in text:
            count+=1;

        param = {'purpose': 'Count Charactor', 'analyzed_sentence':count}

    if(charcount!="on" and extraspaceremover!="on" and newlineremover!="on" and fullcaps!='on' and removepunc!='on' ):

        return HttpResponse("Please select any operation and try again.")

    return render(request, 'analyze.html', param)
