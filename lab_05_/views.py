import json

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world!")


def indexRender(request):
    return render(request, 'index.html', {})


def universityInfo(request):
    json_data = json.loads(str(open("json_data.json", 'r', encoding='utf-8').read()))
    FacCount = 0
    for i in list(json_data["subdivision"]["studies"]["mf"]):
        FacCount += len(i["f"])
    return render(request, "universityInfo.html", {"json_data": json_data,
                                                   "AdminUnitsCount": len(json_data["subdivision"]["administration"]),
                                                   "MegafacCount": len(json_data["subdivision"]["studies"]["mf"]),
                                                   "FacCount": FacCount})


def disciplineInfo(request):
    json_data = json.loads(str(open("json_data.json", 'r', encoding='utf-8').read()))
    return render(request, "disciplineInfo.html",
                  {"mf": json_data["subdivision"]["studies"]["mf"]})


def groupsInfo(request):
    mf = json.loads(str(open("json_data.json", 'r', encoding='utf-8').read()))["subdivision"]["studies"]["mf"]
    return render(request, "groupsInfo.html", {"mf": mf})


def departmentsInfo(request):
    mf = json.loads(str(open("json_data.json", 'r', encoding='utf-8').read()))["subdivision"]["studies"]["mf"]
    return render(request, "departmentsInfo.html", {"mf": mf})


def universityStructure(request):
    json_data = json.loads(str(open("json_data.json", 'r', encoding='utf-8').read()))
    name = json.loads(str(open("json_data.json", 'r', encoding='utf-8').read()))["rector"]["name"][:1]
    tname = json.loads(str(open("json_data.json", 'r', encoding='utf-8').read()))["rector"]["tname"][:1]
    return render(request, "universityStructure.html", {"json": json_data, "name": name, "tname": tname})
