# Generated by Django 2.1.7 on 2019-03-17 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commandes', '0005_auto_20190313_2324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commande',
            old_name='commande_livrée',
            new_name='commande_livree',
        ),
    ]
