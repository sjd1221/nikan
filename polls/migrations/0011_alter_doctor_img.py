# Generated by Django 4.2.2 on 2023-06-26 04:49

from django.db import migrations, models
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_alter_doctor_img_alter_doctor_name_alter_person_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='IMG',
            field=models.ImageField(blank=True, null=True, upload_to=polls.models.PathAndRename.wrapper),
        ),
    ]
