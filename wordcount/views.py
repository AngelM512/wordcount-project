from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html',)

def about_us(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']

    broketext = fulltext.split()

    word_dictionary = {}

    for word in broketext:
        if word in word_dictionary:
            word_dictionary[word] += 1  # ok cool add one
        else:
            word_dictionary[word] = 1

    sortedwords = sorted(word_dictionary.items(), key=operator.itemgetter(1),
                         reverse=True)

    return render(request,'count.html',{'broketext':len(broketext),
                'fulltext':fulltext,'sortedwords':sortedwords})
