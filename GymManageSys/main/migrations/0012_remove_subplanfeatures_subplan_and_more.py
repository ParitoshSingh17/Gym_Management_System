# Generated by Django 4.2.7 on 2023-11-24 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0011_subplan_highlight_status_alter_subplan_price"),
    ]

    operations = [
        migrations.RemoveField(model_name="subplanfeatures", name="subplan",),
        migrations.AddField(
            model_name="subplanfeatures",
            name="subplan",
            field=models.ManyToManyField(to="main.subplan"),
        ),
    ]