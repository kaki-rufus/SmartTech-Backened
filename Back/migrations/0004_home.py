# Generated by Django 4.2.2 on 2023-06-25 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Back", "0003_alter_analysis_options_alter_contacts_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Home",
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
                ("bg_image", models.ImageField(upload_to="")),
            ],
        ),
    ]
