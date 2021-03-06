# Generated by Django 3.0.8 on 2020-10-24 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfc_app', '0004_auto_20201024_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hash',
            name='fob_method',
            field=models.CharField(editable=False, max_length=6),
        ),
        migrations.AlterField(
            model_name='hash',
            name='generated_date',
            field=models.DateField(editable=False),
        ),
        migrations.AlterField(
            model_name='hash',
            name='hashcode',
            field=models.CharField(editable=False, max_length=32),
        ),
        migrations.AlterField(
            model_name='hash',
            name='item_name',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='hash',
            name='size',
            field=models.PositiveIntegerField(editable=False),
        ),
    ]
