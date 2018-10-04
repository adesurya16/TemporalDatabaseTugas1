from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Context, Template
from django.template.loader import render_to_string
from temporalaps.models import Client, Anggota, Proyek
from datetime import datetime

# Create your views here.
def home(request):
    return redirect(index, id = 1)

def index(request, id):
    if id is None:
        id = 1
    # template = "<h1> hai </h1>"
    # context = Context({ "panggilan" : "hai" })
    # return HttpResponse(template.render(context))
    # return render(request, 'temporalaps/index.html')
    template = 'temporalaps/templates/temporalaps/nav.html'
    context = getQuestion(id)
    print(context)
    return render(request, template, context)

def showentity(request):
    return render(request, 'temporalaps/templates/temporalaps/er.html')

def showrelational(request):
    return render(request, 'temporalaps/templates/temporalaps/relational.html')

def inputquery(request):
    return render(request, 'temporalaps/templates/temporalaps/query.html')

def showabout(request):
    return render(request, 'temporalaps/templates/temporalaps/about.html')

def answerquestion(request, id):
    # tambahin disini lebih bagus buat method sendiri untuk setiap pertanyaan
    # jangan lupa lo bagian question berapa (liat di drive pembagian nomor pertanyaan)
    if id == 1:
        return getAnswer1()
    elif id == 2:
        return getAnswer2()
    elif id == 6:
        return getAnswer6()
    elif id == 10:
        return getAnswer10()
    elif id == 14:
        return getAnswer14()
    elif id == 18:
        return getAnswer18()
    else:
        return []

def getAnswer1():
    ans = []
    objectsOfProyek = Proyek.objects.all()
    datenow = datetime.now()
    for obj in objectsOfProyek:
        if datenow > obj['Valid_time_start'] and datenow < obj['Valid_time_end']:
            org = obj['Id_client']
            if not org['Organisasi'] in ans:
                ans.append(org['Organisasi'])   
    return {"Organisasi" : ans}

def getAnswer2():
    m = datetime.now().month
    m = m - 3
    for obj in objectsOfProyek:
        if m < obj['Valid_time_start'].month:
            org = obj['Id_client']
            if not org['Organisasi'] in ans:
                ans.append(org['Organisasi'])   
    return {"Organisasi" : ans}

def getAnswer6():
    return {}

def getAnswer10():
    return {}

def getAnswer14():
    return {}

def getAnswer18():
    return {}

def getQuestion(id):
    question = [{
        "id" : 1,
        "Operasi" : "Projection", #1
        "Pertanyaan" : "Organisasi apa saja yang sedang menjalankan proyek saat ini?"
    },
    {
        "id" : 2,
        "Operasi" : "Selection ", #2
        "Pertanyaan" : "Organisasi apa saja yang sudah menjadi client dari 3 bulan kebelakang?"
    },
    {
        "id" : 3,
        "Operasi" : "Union", #3
        "Pertanyaan" : "Siapa saja nama anggota IIT yang pernah menjadi client?" 
    },
    {
        "id" : 4,
        "Operasi" : "Join", #4
        "Pertanyaan" : "Siapa saja anggota IIT yang mengerjakan proyek saat ini?"
    },
    {
        "id" : 5,
        "Operasi" : "Differences", #5
        "Pertanyaan" : "Siapa saja nama client yang tidak terdaftar sebagai anggota IIT?"
    },
    {
        "id" : 6,
        "Operasi" : "Transaction timeslice", #6
        "Pertanyaan" : "Apa saja proyek yang diinput kemarin?"
    },
    {
        "id" : 7,
        "Operasi" : "Valid timeslice", #7
        "Pertanyaan" : "Apa saja proyek yang sedang berjalan saat ini?"
    },
    {
        "id" : 8,
        "Operasi" : "A before B", #8
        "Pertanyaan" : "Apakah proyek A berjalan sebelum proyek B?"
    },
    {
        "id" : 9,
        "Operasi" : "A overlaps B", #9
        "Pertanyaan" : "Apa sajakah proyek yang mulai sebelum proyek B dimulai dan  selesai antara rentang waktu proyek B?"
    },
    {
        "id" : 10,
        "Operasi" : "A contains B", #10
        "Pertanyaan" : "Apa sajakah proyek yang mulai sebelum proyek KIB jilid II selesai dan selesai setelah proyek KIB jilid II selesai?"
    },
    {
        "id" : 11,
        "Operasi" : "A starts B", #11
        "Pertanyaan" : "Apa sajakah proyek yang mulai bersamaan dengan proyek B, tetapi selesai sebelum proyek B berakhir?"
    },
    {
        "id" : 12,
        "Operasi" : "A finished-by B", #12
        "Pertanyaan" : "Apa sajakah proyek yang mulai setelah proyek B dimulai dan selesai bersamaan dengan proyek B?"
    },
    {
        "id" : 13,
        "Operasi" : "A meets B",
        "Pertanyaan" : "Apa sajakah proyek yang berjalan tepat setelah proyek A?"
    },
    {
        "id" : 14,
        "Operasi" : "A equal B",
        "Pertanyaan" : "Siapa saja manajer yang mengerjakan dua proyek berbeda pada rentang waktu yang sama?"
    },
    {
        "id" : 15,
        "Operasi" : "A after B",
        "Pertanyaan" : "Apa sajakah proyek yang berjalan dua hari setelah proyek B selesai?"
    },
    {
        "id" : 16,
        "Operasi" : "A overlapped-by B",
        "Pertanyaan" : "Apa sajakah proyek yang mulai sebelum proyek A dimulai dan  selesai antara rentang waktu proyek A?"
    },
    {
        "id" : 17,
        "Operasi" : "A during B",
        "Pertanyaan" : "Apa sajakah proyek yang mulai sebelum proyek B selesai dan selesai setelah proyek B selesai?"
    },
    {
        "id" : 18,
        "Operasi" : "A started-by B",
        "Pertanyaan" : "Apa sajakah proyek yang mulai bersamaan dengan proyek Rekayasa Pinus tetapi selesai setelah proyek Rekayasa Pinus berakhir?"
    },
    {
        "id" : 19,
        "Operasi" : "A finished B",
        "Pertanyaan" : "Apa sajakah proyek yang mulai setelah proyek B dimulai dan berakhir bersamaan dengan proyek B?"
    },
    {
        "id" : 20,
        "Operasi" : "A met-by B",
        "Pertanyaan" : "Apakah sajakah proyek yang berakhir tepat setelah proyek A?"
    }
    ]
    return question[id - 1]