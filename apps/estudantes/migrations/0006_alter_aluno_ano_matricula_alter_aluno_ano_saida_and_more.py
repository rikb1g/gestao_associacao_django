# Generated by Django 5.0.2 on 2024-03-26 12:24

import apps.estudantes.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("estudantes", "0005_alter_aluno_ano_matricula_alter_aluno_ano_saida"),
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
        migrations.AlterField(
            model_name="mensalidadepagamento",
            name="aluno",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mensalidades",
                to="estudantes.aluno",
            ),
        ),
    ]
