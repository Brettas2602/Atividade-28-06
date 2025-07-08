from django.urls import path
from . import views

urlpatterns = [
    path('alunos/', views.listar_alunos, name='listar_alunos'),
    path('alunos/novo/', views.criar_aluno, name='criar_aluno'),
    path('alunos/<int:id>/editar/', views.editar_aluno, name='editar_aluno'),
    path('alunos/<int:id>/deletar/', views.deletar_aluno, name='deletar_aluno'),

    path('livros/', views.listar_livros, name='listar_livros'),
    path('livros/novo/', views.criar_livro, name='criar_livro'),
    path('livros/<int:id>/editar/', views.editar_livro, name='editar_livro'),
    path('livros/<int:id>/deletar/', views.deletar_livro, name='deletar_livro'),
    
    path('emprestimos/', views.listar_emprestimos, name='listar_emprestimos'),
    path('emprestimos/novo/', views.registrar_emprestimo, name='registrar_emprestimo'),
    path('emprestimos/<int:id>/devolver/', views.registrar_devolucao, name='registrar_devolucao'),

]