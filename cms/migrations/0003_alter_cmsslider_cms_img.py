# Generated by Django 4.0.2 on 2022-02-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_alter_cmsslider_cms_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmsslider',
            name='cms_img',
            field=models.ImageField(upload_to='slider'),
        ),
    ]
