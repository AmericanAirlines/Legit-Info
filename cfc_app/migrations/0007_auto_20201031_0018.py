# Generated by Django 3.0.8 on 2020-10-31 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfc_app', '0006_auto_20201024_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='law',
            name='cite_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='law',
            name='relevance',
            field=models.CharField(max_length=800, null=True),
        ),
    ]
