# Generated by Django 3.2.5 on 2021-08-06 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
        ('Issues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='projet_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Projects.projects'),
        ),
    ]