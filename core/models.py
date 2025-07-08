from django.db import models
from django.utils import timezone

# Create your models here.

class Aluno(models.Model):
    nome_completo = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    curso = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    
    def __str__(self):
        return f'{self.nome_completo} ({self.matricula})'
    
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    quantidade_disponivel = models.PositiveIntegerField()
    
    def __str__(self):
        return self.titulo
    
class Emprestimo(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(default=timezone.now)
    data_prevista_devolucao = models.DateField()
    data_devolucao = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.aluno.nome_completo} → {self.livro.titulo}'

    def esta_ativo(self):
        return self.data_devolucao is None