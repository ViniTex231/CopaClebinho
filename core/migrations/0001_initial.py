# Generated by Django 5.0 on 2023-12-06 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=30)),
                ('conteudo', models.CharField(max_length=1000)),
                ('estado', models.BooleanField()),
                ('categorias', models.CharField(choices=[('Biografia', 'Biografia'), ('Crônica', 'Crônica'), ('Drama', 'Drama'), ('Fábula', 'Fábula'), ('Fantasia', 'Fantasia'), ('Ficção científica', 'Ficção científica'), ('Horror', 'Horror'), ('Humor', 'Humor'), ('Infantil', 'Infantil'), ('Jornalismo literário', 'Jornalismo literário'), ('LGBT', 'LGBT'), ('Mistério', 'Mistério'), ('Mitologia', 'Mitologia'), ('Poesia', 'Poesia'), ('Policial', 'Policial'), ('Realismo mágico', 'Realismo mágico'), ('Relato de viagem', 'Relato de viagem'), ('Romance', 'Romance'), ('Romance de época', 'Romance de época'), ('Sátira', 'Sátira'), ('Suspense', 'Suspense'), ('Terror', 'Terror')], max_length=100)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
