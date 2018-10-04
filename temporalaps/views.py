from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Context, Template
from django.template.loader import render_to_string
from temporalaps.models import Client, Anggota, Proyek
import datetime
import time
from datetime import timedelta
from django.http.response import JsonResponse
# from rest_framework.response import Response

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
    elif id == 4:
        return getAnswer4()
    elif id == 6:
        return getAnswer6()
    elif id == 8:
        return getAnswer8()
    elif id == 10:
        return getAnswer10()
    elif id == 12:
        return getAnswer12()
    elif id == 14:
        return getAnswer14()
    elif id == 16:
        return getAnswer16()
    elif id == 18:
        return getAnswer18()
    elif id == 20:
        return getAnswer20()
    else:
        return JsonResponse([])

def getAnswer1():
    # print("Answer 1")
    save = []
    ans = []
    objectsOfProyek = Proyek.objects.all()
    # print(objectsOfProyek)
    # datenow = datetime.date(time.strftime("%Y-%m-%d"))
    datenow = datetime.date.today()
    # print(datenow)
    for obj in objectsOfProyek:
        # print(obj.Valid_time_start, type(obj.Valid_time_start))
        if datenow > obj.Valid_time_start and datenow < obj.Valid_time_end:
            org = obj.Id_client
            if not org.Organisasi in save:
                save.append(org.Organisasi)
                ans.append({"Organisasi" : org.Organisasi, "Valid_time_start" : org.Valid_time_start, "Valid_time_end" : org.Valid_time_end})   
    return JsonResponse({ "data" : ans })

def getAnswer2():
    save = []
    a = str(datetime.date.today())
    datee = datetime.datetime.strptime(a, "%Y-%m-%d")
    m = datee.month
    print(m)
    m = m - 3
    ans = []
    objectsOfProyek = Proyek.objects.all()
    for obj in objectsOfProyek:
        if m < int(obj.Valid_time_start.month):
            org = obj.Id_client
            if not org.Organisasi in save:
                save.append(org.Organisasi)
                ans.append({"Organisasi" : org.Organisasi, "Valid_time_start" : org.Valid_time_start, "Valid_time_end" : org.Valid_time_end})   
    return JsonResponse({ "data" : ans })

def getAnswer4():
    save = []
    ans = []
    objectsOfProyek = Proyek.objects.all()
    datenow = datetime.date.today()
    for obj in objectsOfProyek:
        if datenow > obj.Valid_time_start and datenow < obj.Valid_time_end:
            org = obj.Id_iit
            if not org.Nama in save:
                save.append(org.Nama)
                ans.append({"Nama Anggota IIT" : org.Nama, "Nama Proyek": obj.Nama, "Valid_time_start" : obj.Valid_time_start, "Valid_time_end" : obj.Valid_time_end})   
    print(ans)
    return JsonResponse({ "data" : ans })

def getAnswer6():
    return {}

def getAnswer8():
    ans = []
    save = []
    projectB = Proyek.objects.get(Id_proyek=12)
    objectAll = Proyek.objects.all()
    for obj in objectAll:
        if projectB.Valid_time_start > obj.Valid_time_start:
            if not obj.Nama in save:
                save.append(obj.Nama)
                ans.append({"Nama" : obj.Nama, "Valid_time_start" : obj.Valid_time_start, "Valid_time_end" : obj.Valid_time_end})
    return JsonResponse({ 'data' : ans })
    
def getAnswer10():
    ans = []
    save = []
    object10 = Proyek.objects.get(Id_proyek=12)
    print(object10)
    objectAll = Proyek.objects.all()
    print(objectAll)
    for obj in objectAll:
        if object10.Valid_time_start < obj.Valid_time_start and object10.Valid_time_end > obj.Valid_time_end:
            if not obj.Nama in save:
                save.append(obj.Nama)
                ans.append({"Nama" : obj.Nama, "Valid_time_start" : obj.Valid_time_start, "Valid_time_end" : obj.Valid_time_end})
    return JsonResponse({ 'data' : ans })

def getAnswer12():
    ans = []
    save = []
    projectB = Proyek.objects.get(Id_proyek=13)
    objectAll = Proyek.objects.all()
    for obj in objectAll:
        if projectB.Valid_time_start > obj.Valid_time_start and projectB.Valid_time_end == obj.Valid_time_end:
            if not obj.Nama in save:
                save.append(obj.Nama)
                ans.append({"Nama" : obj.Nama, "Valid_time_start" : obj.Valid_time_start, "Valid_time_end" : obj.Valid_time_end})
    return JsonResponse({ 'data' : ans })
    
def getAnswer14():
    ans = []
    objectAnggota = Anggota.objects.all()
    for obj in objectAnggota:
        counters = Proyek.objects.filter(Id_iit = obj.Nim)
        if counters.count() > 1 :
            ans.append(counters)
    print(ans)
    ans2 = []
    for counter in ans:
        isEqual = False
        print(counter)
        p = len(counter)
        for i in range(0, p - 1):
            for j in range(i+1, p):
                if counter[i].Valid_time_start == counter[j].Valid_time_start and counter[i].Valid_time_end == counter[j].Valid_time_end and not isEqual:
                    isEqual = True
                    manager = counter[i].Id_iit
        if isEqual:
            ans3 = []
            for ob in counter:
                ans3.append(ob.Nama) 
            ans2.append({"Nama_manager" : manager.Nama, "Nama_mama_proyek" : ans3, "Valid_time_start" : counter[0].Valid_time_start, "Valid_time_end" : counter[0].Valid_time_end}) 
            
    # cari tiap tuple di list apakah 
    return JsonResponse({ 'data' : ans2 })

def getAnswer16():
    ans = []
    save = []
    projectA = Proyek.objects.get(Id_proyek=20)
    objectAll = Proyek.objects.all()
    for obj in objectAll:
        if projectA.Valid_time_start > obj.Valid_time_start and projectA.Valid_time_end > obj.Valid_time_end and projectA.Valid_time_start < obj.Valid_time_end:
            if not obj.Nama in save:
                save.append(obj.Nama)
                ans.append({"Nama" : obj.Nama, "Valid_time_start" : obj.Valid_time_start, "Valid_time_end" : obj.Valid_time_end})
    return JsonResponse({ 'data' : ans })
    
def getAnswer18():
    ans = []
    save = []
    object10 = Proyek.objects.get(Id_proyek=2)
    print(object10)
    objectAll = Proyek.objects.all()
    for obj in objectAll:
        if object10.Valid_time_start < obj.Valid_time_start and object10.Valid_time_end > obj.Valid_time_end:
            if not obj.Nama in save:
                save.append(obj.Nama)
                ans.append({"Nama" : obj.Nama})
    return JsonResponse({ 'data' : ans })

def getAnswer20():
    ans = []
    save = []
    projectA = Proyek.objects.get(Id_proyek=9)
    objectAll = Proyek.objects.all()
    for obj in objectAll:
        if projectA.Valid_time_start - timedelta(1) == obj.Valid_time_end:
            if not obj.Nama in save:
                save.append(obj.Nama)
                ans.append({"Nama" : obj.Nama, "Valid_time_start" : obj.Valid_time_start, "Valid_time_end" : obj.Valid_time_end})
    return JsonResponse({ 'data' : ans })
    
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
        "Pertanyaan" : "Apa saja proyek yang berjalan sebelum proyek B?"
    },
    {
        "id" : 9,
        "Operasi" : "A overlaps B", #9
        "Pertanyaan" : "Apa sajakah proyek yang mulai sebelum proyek B dimulai dan  selesai antara rentang waktu proyek B?"
    },
    {
        "id" : 10,
        "Operasi" : "A contains B", #10
        "Pertanyaan" : "Apa sajakah proyek yang mulai sebelum proyek 'Rekayasa stroberi' mulai dan selesai setelah proyek 'Rekayasa stroberi' selesai?"
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
        "Pertanyaan" : "Apa sajakah proyek yang mulai bersamaan dengan proyek 'Rekayasa Pinus' tetapi selesai setelah proyek 'Rekayasa Pinus' berakhir?"
    },
    {
        "id" : 19,
        "Operasi" : "A finished B",
        "Pertanyaan" : "Apa sajakah proyek yang mulai setelah proyek B dimulai dan berakhir bersamaan dengan proyek B?"
    },
    {
        "id" : 20,
        "Operasi" : "A met-by B",
        "Pertanyaan" : "Apakah sajakah proyek yang berakhir tepat sebelum proyek A dimulai?"
    }
    ]
    return question[id - 1]