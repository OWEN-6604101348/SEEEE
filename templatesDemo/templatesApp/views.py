
from django.shortcuts import render


def renderTemplate(request):
    myDict={"name":"Poramat JunYon"}
    return render(request, 'templatesApp/firstTemplate.html',context=myDict)


def renderEmployee(request):
    myDict={"id":6604101348,"name":"Poramatjunyon","sal":999999}
    return render(request, 'templatesApp/employeeTemplate.html',context=myDict)