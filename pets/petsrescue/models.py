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
    especie = models.CharField(max_length=1, choices=ESPECIE_CHOICES, default=DOG)

    PEQ = 'Pq'
    MED = 'Md'
    GDE = 'Gd'
    PORTE_CHOICES = (
        (PEQ, 'Pequeno'),
        (MED, 'Mediano'),
        (GDE, 'Grande')
    )
    porte = models.CharField(max_length=2, choices=PORTE_CHOICES, default=GDE)

    CACHORRO = 'C'
    ADULTO = 'A'
    IDADE_CHOICES = (
        (CACHORRO, 'Cachorro'),
        (ADULTO, 'Adulto')
    )

    nombre = models.CharField(max_length=50, null=False)
    edad = models.CharField(max_length=1, choices=IDADE_CHOICES, default=ADULTO)
    raza = models.CharField(max_length=100, null=False)
    obs = models.TextField(max_length=500, null=True, blank=True)
    adopted = models.Boolean(default=False)
     
    def __str__(self):
        return "pet_foto: {}\nEspecie: {}\nPorte: {}\nNome: {}\nIdade: {}\nRaça: {}\nObs.: {}"\
        .format(self.pet_foto, self.especie, self.porte, self.nome, self.idade, self.raca, self.obs)
     
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
