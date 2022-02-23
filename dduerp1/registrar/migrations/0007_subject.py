# Generated by Django 4.0.2 on 2022-02-23 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0006_teachingschemehead_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('code', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('shortName', models.CharField(max_length=10)),
                ('examScheme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registrar.examschemehead')),
                ('teachingScheme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registrar.teachingschemehead')),
            ],
        ),
    ]