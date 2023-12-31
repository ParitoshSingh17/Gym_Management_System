# Generated by Django 4.2.7 on 2023-11-23 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_galleryimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gallery",
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
                ("title", models.CharField(max_length=150)),
                ("detail", models.TextField()),
                ("img", models.ImageField(null=True, upload_to="gallery/")),
            ],
        ),
    ]
