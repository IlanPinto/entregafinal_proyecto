# Generated by Django 4.1.2 on 2022-11-28 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiApp', '0004_alter_blogs_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='cuerpo',
            field=models.CharField(default='-', max_length=400),
            preserve_default=False,
        ),
    ]
