# Generated by Django 4.2.2 on 2023-06-25 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Back", "0002_alter_networking_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="analysis",
            options={"verbose_name_plural": "Analysis"},
        ),
        migrations.AlterModelOptions(
            name="contacts",
            options={"verbose_name_plural": "Contacts"},
        ),
        migrations.AlterModelOptions(
            name="members",
            options={"verbose_name_plural": "Members"},
        ),
        migrations.AlterModelOptions(
            name="mentorship",
            options={"verbose_name_plural": "Mentorship"},
        ),
        migrations.AlterModelOptions(
            name="pc",
            options={"verbose_name_plural": "PC"},
        ),
        migrations.AlterModelOptions(
            name="web",
            options={"verbose_name_plural": "Web"},
        ),
    ]
