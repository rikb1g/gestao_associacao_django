# Generated by Django 5.0.4 on 2024-04-29 22:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("funcionarios", "0002_funcionario_escola"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="funcionario",
            name="Horas",
        ),
        migrations.AddField(
            model_name="funcionario",
            name="horas_contrato",
            field=models.IntegerField(
                default=1, verbose_name="Horas contratadas diárias"
            ),
            preserve_default=False,
        ),
    ]
