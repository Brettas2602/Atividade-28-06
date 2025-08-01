# Generated by Django 5.2.3 on 2025-06-28 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_aluno_data_nascimento_aluno_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('editora', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=20, unique=True)),
                ('quantidade_disponivel', models.PositiveIntegerField()),
            ],
        ),
    ]
