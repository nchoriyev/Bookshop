# Generated by Django 5.0.6 on 2024-07-11 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savat',
            name='name',
        ),
        migrations.AddField(
            model_name='savat',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book.book'),
            preserve_default=False,
        ),
    ]
