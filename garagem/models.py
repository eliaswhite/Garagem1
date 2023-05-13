from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.nome.upper()


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descricao} ({self.id})"

    class Meta:
        verbose_name = "acessório"
        verbose_name_plural = "acessórios"
 
   
class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descricao}"

    class Meta:
        verbose_name = "cor"
        verbose_name_plural = "cores"


class Modelo(models.Model):
    descricao = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.descricao} ({self.id})"

    class Meta:
        verbose_name = "modelo"
        verbose_name_plural = "modelos"