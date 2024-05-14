# Generated by Django 5.0.6 on 2024-05-13 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='periodo',
            field=models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')], default='M', max_length=1),
        ),
    ]
