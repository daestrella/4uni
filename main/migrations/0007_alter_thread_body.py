# Generated by Django 4.2.11 on 2024-07-04 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_board_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
