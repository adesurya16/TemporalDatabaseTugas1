from django.db import models

# Create your models here.

class Client(models.Model):
    Nama = models.CharField(max_length = 255)
    Organisasi = models.CharField(max_length = 255)
    Telp = models.CharField(max_length = 255)
    Email = models.CharField(max_length = 255)

    def __str__(self):
        return self.Nama

class Anggota(models.Model):
    divisi = (
        ('1', 'Manpro'),
        ('2', 'Marketing'),
        ('3', 'Teknikal')
    )
    Nim = models.AutoField(primary_key = True)
    Nama = models.CharField(max_length = 255)
    Alamat = models.CharField(max_length = 255)
    Telepon = models.CharField(max_length = 255)
    Email = models.CharField(max_length = 255)
    Divisi = models.CharField(max_length = 1, choices=divisi)

    def __str__(self):
        return self.Nim

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

    def getDuration(self):
        Day = self.Valid_time_end - self.Valid_time_start 
        return Day.days

    def __str__(self):
        return self.Nama
    
    

