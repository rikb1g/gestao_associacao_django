# Generated by Django 5.0.2 on 2024-04-22 12:56

import apps.estudantes.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("estudantes", "0031_aluno_contacto_aluno_enc_educacao_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="aluno",
            old_name="contacto",
            new_name="contato",
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