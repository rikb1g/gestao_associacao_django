# Generated by Django 5.0.2 on 2024-04-27 18:30

import apps.estudantes.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("estudantes", "0033_mensalidadepagamento_atraso_and_more"),
    ]

    operations = [
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
