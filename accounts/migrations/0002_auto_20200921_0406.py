# Generated by Django 3.0.3 on 2020-09-20 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procurement',
            name='Total_LeadTime',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
