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
        
        
class Veiculo(models.Model):
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, related_name="veiculos"
    )
    modelo = models.CharField(max_length=15, null=False, default=0)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="veiculos"
    )
    cor = models.ForeignKey(
        Cor, on_delete=models.PROTECT, related_name="veiculos"
    )
    ano = models.IntegerField(null=True,default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=5, null=True, 
    default=0)

    def __str__(self):
        return f"Marca: {self.marca} Modelo: {self.modelo} Ano: {self.ano} Cor: {self.cor}"
    
    class Meta:
        verbose_name = "veículo"
        verbose_name_plural = "veículos"