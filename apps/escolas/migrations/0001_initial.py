# Generated by Django 5.0.2 on 2024-03-24 15:20

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Escola",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Funcionario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                (
                    "Horas",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Horas contratadas diárias",
                    ),
                ),
                (
                    "salario",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0.0)],
                        verbose_name="Salário",
                    ),
                ),
                ("funcao", models.CharField(max_length=50, verbose_name="Função")),
            ],
        ),
        migrations.CreateModel(
            name="Atividades",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                (
                    "valor",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0.0)],
                    ),
                ),
                (
                    "escola",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="escolas.escola"
                    ),
                ),
            ],
            options={
                "verbose_name": "Atividade",
                "verbose_name_plural": "Atividades",
            },
        ),
        migrations.CreateModel(
            name="Mensalidade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                (
                    "valor",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0.0)],
                    ),
                ),
                (
                    "escola",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="escolas.escola"
                    ),
                ),
            ],
        ),
    ]