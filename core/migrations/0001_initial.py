# Generated by Django 3.2.12 on 2022-06-23 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Tecnico',
                'verbose_name_plural': 'Tecnicos',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descricao')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Preco')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('tecnico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.tecnico')),
            ],
            options={
                'verbose_name': 'Atendimento',
                'verbose_name_plural': 'Atendimentos',
                'ordering': ('descricao',),
            },
        ),
    ]