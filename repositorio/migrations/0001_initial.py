# Generated by Django 4.1 on 2022-08-23 17:18

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeironome', models.CharField(max_length=200)),
                ('ultimonome', models.CharField(max_length=200)),
                ('foto', models.ImageField(upload_to='fotos/')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('modalidade', models.CharField(choices=[('B', 'BACHARELADO'), ('L', 'LICENCIATURA'), ('T', 'TECNOLOGICO')], max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Orientador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeironome', models.CharField(max_length=200)),
                ('ultimonome', models.CharField(max_length=200)),
                ('linkcurriculolattes', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Tcc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('anododocumento', models.IntegerField()),
                ('resumo', models.TextField()),
                ('arquivododocumento', models.FileField(upload_to='documentos/')),
                ('palavras_chave', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repositorio.autor')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repositorio.curso')),
                ('orientador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repositorio.orientador')),
            ],
        ),
    ]
