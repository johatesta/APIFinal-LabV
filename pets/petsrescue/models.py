from django.db import models

import os

def get_image_path(instance, filename):
    return os.path.join('pics', str(instance.id), filename)

# Create your models here.
class Pets(models.Model):
    pet_foto = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    DOG = 'C'
    CAT = 'G'
    ESPECIE_CHOICES = (
        (DOG, 'Perro'),
        (CAT, 'Gato')
    )
    tamanio = models.CharField(max_length=1, choices=ESPECIE_CHOICES, default=DOG)

    PEQ = 'Pq'
    MED = 'Md'
    GDE = 'Gd'
    PORTE_CHOICES = (
        (PEQ, 'Pequeno'),
        (MED, 'Mediano'),
        (GDE, 'Grande')
    )
    edad = models.CharField(max_length=2, choices=PORTE_CHOICES, default=GDE)

    CACHORRO = 'C'
    ADULTO = 'A'
    IDADE_CHOICES = (
        (CACHORRO, 'Cachorro'),
        (ADULTO, 'Adulto')
    )

    nombre = models.CharField(max_length=50, null=False)
    edad = models.CharField(max_length=1, choices=IDADE_CHOICES, default=ADULTO)
    raza = models.CharField(max_length=100, null=False)
    adopted = models.Boolean(default=False)
     
    def __str__(self):
        return "pet_foto: {}\nEspecie: {}\nTamanio: {}\nNome: {}\nEdad: {}\nRaza: {}"\
        .format(self.pet_foto, self.tamanio, self.tamanio, self.nombre, self.edad, self.raza)
     
class Estado_adoptivo(models.Model):
    adopted: models.ForeignKey(Pets,on_delete=models.CASCADE, verbose_name="Pets")
class Persona:
    nombre=models.CharField(max_length=50,null=False)
    apellido=models.CharField(max_length=50,null=False)
    dni=models.IntegerField()
    frchanacimiento=models.DateField()
    trlefono=models.IntegerField
    email=models.CharField(max_length=50,default=False)

class Adoptante (models.Model):
    datospersonales = models.ForeignKey(Persona,on_delete=models.CASCADE,verbose_name="persona")
    direccion= models.CharField(max_length=50,null=False)

    

# Create your models here.
