# Generated by Django 5.0.2 on 2024-04-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gestao", "0005_alter_despesas_ficheiro"),
    ]

    operations = [
        migrations.AlterField(
            model_name="despesas",
            name="data",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
