# Generated by Django 5.0.2 on 2024-04-09 22:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gestao", "0003_receita_file"),
    ]

    operations = [
        migrations.RenameField(
            model_name="receita",
            old_name="file",
            new_name="ficheiro",
        ),
        migrations.AddField(
            model_name="despesas",
            name="ficheiro",
            field=models.FileField(blank=True, upload_to=""),
        ),
    ]
