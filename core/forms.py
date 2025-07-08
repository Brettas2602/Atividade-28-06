from django import forms
from .models import Aluno, Livro

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome_completo', 'matricula', 'email', 'curso', 'data_nascimento']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'w-full px-4 py-1 border rounded shadow-sm'}),
            'matricula': forms.TextInput(attrs={'class': 'w-full px-4 py-1 border rounded shadow-sm'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-1 border rounded shadow-sm'}),
            'curso': forms.TextInput(attrs={'class': 'w-full px-4 py-1 border rounded shadow-sm'}),
            'data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-4 py-1 border rounded shadow-sm'}),
        }

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'editora', 'isbn', 'quantidade_disponivel']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded shadow-sm'}),
            'autor': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded shadow-sm'}),
            'editora': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded shadow-sm'}),
            'isbn': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded shadow-sm'}),
            'quantidade_disponivel': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border rounded shadow-sm'}),
        }
        
from .models import Emprestimo

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['aluno', 'livro', 'data_prevista_devolucao']
        widgets = {
            'aluno': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded shadow-sm'}),
            'livro': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded shadow-sm'}),
            'data_prevista_devolucao': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-2 border rounded shadow-sm'
            }),
        }