# Generated by Django 5.0.4 on 2024-05-02 09:22

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("funcionarios", "0005_alter_funcionario_salario"),
    ]

    operations = [
        migrations.CreateModel(
            name="Salarios",
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
                ("data_inicio", models.DateField()),
                ("data_fim", models.DateField()),
                (
                    "falta",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("valor", models.DecimalField(decimal_places=2, max_digits=10)),
                ("receibo", models.FileField(upload_to="")),
                (
                    "funcionario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="funcionarios.funcionario",
                    ),
                ),
            ],
        ),
    ]
