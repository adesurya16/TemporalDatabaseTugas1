from django.db import models

# Create your models here.

class Client(models.Model):
    # id = models.AutoField(primary_key = True)
    Nama = models.CharField(max_length = 255)
    Organisasi = models.CharField(max_length = 255)
    Telepon = models.CharField(max_length = 255)
    Email = models.CharField(max_length = 255)
    Valid_time_start = models.DateField(null = True)
    Valid_time_end = models.DateField(null = True)
    objects = models.Manager()

    def __str__(self):
        return self.Nama

class Anggota(models.Model):
    Nim = models.AutoField(primary_key = True)
    Nama = models.CharField(max_length = 255)
    Alamat = models.CharField(max_length = 255, null=True)
    Telepon = models.CharField(max_length = 255,  null=True)
    Email = models.CharField(max_length = 255)
    Divisi = models.CharField(max_length = 255)
    objects = models.Manager()

    def __str__(self):
        return self.Nama + " " + str(self.Nim) 

class Proyek(models.Model):
    Id_proyek = models.AutoField(primary_key = True)
    Nama = models.CharField(max_length = 255)
    Id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Id_iit = models.ForeignKey(Anggota, on_delete=models.CASCADE)
    Jumlah_developer = models.IntegerField()
    Deskripsi = models.TextField(blank=True, null=True)
    Valid_time_start = models.DateField()
    Valid_time_end = models.DateField()
    Durasi = models.IntegerField()
    objects = models.Manager()

    def getDuration(self):
        Day = self.Valid_time_end - self.Valid_time_start 
        return Day.days

    def __str__(self):
        return self.Nama
    
    

