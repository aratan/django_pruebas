# Generated by Django 4.1 on 2022-08-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Escribe el titulo del libro', max_length=64)),
                ('fecha_publicacion', models.DateField(help_text='Escribe la fecha')),
                ('genero', models.ManyToManyField(help_text='Selecciona el genero', to='catalogo.genero')),
            ],
        ),
    ]