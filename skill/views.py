from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect

# def pagelabel(lang):
    
#     langqueryset = list(MasterLabels.objects.filter(lang=lang).values('keydata', 'label'))
#     dictvalue={}
#     for item in langqueryset:
#         dictvalue[item['keydata']] = item['label']
#     return dictvalue
def home(request):
    # lang='en'
    # context=pagelabel(lang)
    # context["title"]="this is title"
    # context["h5"]="this is h5"
    dict={}
    title="this is title"
    h1="home page"
    
    return render(request,'home.html',{"title":title,"h1":h1})
def skilltester(request):
    # lang='en'
    # context=pagelabel(lang)
    # context["title"]="this is title"
    # context["h5"]="this is h5"
    dict={}
    title="this is title"
    h1="home page"
    
    return render(request,'skilltester.html',{"title":title,"h1":h1})