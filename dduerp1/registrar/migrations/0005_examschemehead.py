# Generated by Django 4.0.2 on 2022-02-18 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0004_program'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamSchemeHead',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('external', models.IntegerField()),
                ('sessional', models.IntegerField()),
                ('practical', models.IntegerField()),
                ('theory', models.IntegerField()),
                ('maxMarks', models.IntegerField()),
                ('minMarks', models.IntegerField()),
            ],
        ),
    ]