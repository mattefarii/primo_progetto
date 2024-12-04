from django.shortcuts import render
import datetime

def index2(request):
    context = {
        "link1" : "Es if",
        "link2" : "If else elif",

    }
    return render(request, "index2.html", context)

def es_if(request):
    context = {
        "var1" : 200,
        "var2" : 200,
        "var3" : 300,
    }
    return render(request, "es_if.html", context)

def if_else_elif(request):
    context = {
        "var1" : 100,
        "var2" : 100.0,
        "var3" : 100.50,
    }
    return render(request, "if_else_elif.html", context)

def es_for(request):
    context = {
       "list1" : [1, datetime.date(2024, 7, 19), "do not give up!"],
       "list2" : [2, datetime.date(2020, 8, 16), "do not give up!"],

    }
    return render(request, "es_for.html", context)