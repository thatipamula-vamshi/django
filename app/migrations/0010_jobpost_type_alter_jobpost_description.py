# Generated by Django 4.2.2 on 2023-08-23 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_jobpost_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='type',
            field=models.CharField(choices=[('Full time', 'fulltime'), ('Part time', 'parttime')], default='Full time', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='description',
            field=models.TextField(),
        ),
    ]