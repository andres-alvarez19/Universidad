from django.db import models

# Create your models here.
class Carrera (models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)


    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()
    sexos = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )
    sexo = models.CharField(max_length=1, choices=sexos, default='M')
    carrera = models.ForeignKey(Carrera, null=True, blank=True, on_delete=models.CASCADE)

    def nombreCompleto(self):
        return "{0} {1}, {2}".format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

    def __str__(self):
        return self.nombreCompleto()
class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)
    carrera = models.ForeignKey(Carrera, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante,null=False,blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1}".format(self.estudiante, self.curso)