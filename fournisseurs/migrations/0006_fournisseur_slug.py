# Generated by Django 2.1.5 on 2019-03-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fournisseurs', '0005_fournisseur_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='fournisseur',
            name='slug',
            field=models.SlugField(default='christopher-raeburn', unique=True),
            preserve_default=False,
        ),
    ]
