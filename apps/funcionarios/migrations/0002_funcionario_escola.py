# Generated by Django 5.0.4 on 2024-04-29 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("escolas", "0003_delete_funcionario"),
        ("funcionarios", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="funcionario",
            name="escola",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="escolas.escola",
            ),
            preserve_default=False,
        ),
    ]
