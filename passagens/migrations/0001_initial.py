# Generated by Django 3.0.3 on 2020-03-04 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origem', models.CharField(max_length=100)),
                ('destino', models.CharField(max_length=100)),
                ('data_ida', models.DateField()),
                ('data_volta', models.DateField()),
                ('data_pesquisa', models.DateField()),
                ('classe_viagem', models.TextField(choices=[('ECONOMICA', 'Econômica'), ('EXECUTIVA', 'Executiva'), ('PRIMEIRA_CLASSE', 'Primeira classe')], default=0, max_length=15)),
                ('informacoes', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
