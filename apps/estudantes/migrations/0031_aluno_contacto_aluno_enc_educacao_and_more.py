# Generated by Django 5.0.2 on 2024-04-22 12:54

import apps.estudantes.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("estudantes", "0030_alter_aluno_ano_matricula_alter_aluno_ano_saida"),
    ]

    operations = [
        migrations.AddField(
            model_name="aluno",
            name="contacto",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name="aluno",
            name="enc_educacao",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="Encarregado de Educação"
            ),
        ),
        migrations.AlterField(
            model_name="aluno",
            name="ano_matricula",
            field=apps.estudantes.models.AnoField(
                validators=[
                    apps.estudantes.models.validate_year,
                    apps.estudantes.models.validate_year,
                ]
            ),
        ),
        migrations.AlterField(
            model_name="aluno",
            name="ano_saida",
            field=apps.estudantes.models.AnoField(
                blank=True,
                null=True,
                validators=[
                    apps.estudantes.models.validate_year,
                    apps.estudantes.models.validate_year,
                ],
            ),
        ),
    ]