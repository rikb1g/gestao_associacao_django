# Generated by Django 5.0.2 on 2024-04-17 14:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("escolas", "0002_alter_atividades_options"),
        ("gestao", "0010_remove_entradas_fatura"),
    ]

    operations = [
        migrations.AddField(
            model_name="tipodespesa",
            name="escola",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="escolas.escola",
            ),
            preserve_default=False,
        ),
    ]