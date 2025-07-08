from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno, Livro, Emprestimo
from .forms import AlunoForm, LivroForm, EmprestimoForm
from django.utils import timezone

# Views de aluno
def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'listar_alunos.html', {'alunos': alunos})

def criar_aluno(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_alunos')
    return render(request, 'form_aluno.html', {'form': form})

def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    form = AlunoForm(request.POST or None, instance=aluno)
    if form.is_valid():
        form.save()
        return redirect('listar_alunos')
    return render(request, 'form_aluno.html', {'form': form})

def deletar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        aluno.delete()
        return redirect('listar_alunos')
    return render(request, 'confirmar_delete.html', {'aluno': aluno})

# Views de livro
def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'listar_livros.html', {'livros': livros})

def criar_livro(request):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_livros')
    return render(request, 'form_livro.html', {'form': form})

def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    form = LivroForm(request.POST or None, instance=livro)
    if form.is_valid():
        form.save()
        return redirect('listar_livros')
    return render(request, 'form_livro.html', {'form': form})

def deletar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros')
    return render(request, 'confirmar_delete_livro.html', {'livro': livro})

# Views de emprestimo
def listar_emprestimos(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'listar_emprestimos.html', {'emprestimos': emprestimos})

def registrar_emprestimo(request):
    form = EmprestimoForm(request.POST or None)
    if form.is_valid():
        livro = form.cleaned_data['livro']
        if livro.quantidade_disponivel > 0:
            livro.quantidade_disponivel -= 1
            livro.save()
            form.save()
            return redirect('listar_emprestimos')
        else:
            form.add_error('livro', 'Este livro não está disponível no momento.')
    return render(request, 'form_emprestimo.html', {'form': form})

def registrar_devolucao(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    if request.method == 'POST':
        emprestimo.data_devolucao = timezone.now().date()
        emprestimo.livro.quantidade_disponivel += 1
        emprestimo.livro.save()
        emprestimo.save()
        return redirect('listar_emprestimos')
    return render(request, 'confirmar_devolucao.html', {'emprestimo': emprestimo})