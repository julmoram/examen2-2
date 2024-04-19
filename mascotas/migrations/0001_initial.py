# Generated by Django 5.0.4 on 2024-04-19 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('especie', models.CharField(choices=[('perro', 'Perro'), ('gato', 'Gato'), ('hamster', 'Hamster')], max_length=20)),
                ('fecha_creado', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
