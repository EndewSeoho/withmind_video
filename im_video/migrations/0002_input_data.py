# Generated by Django 3.2.4 on 2021-06-28 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('im_video', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='input_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userkey', models.IntegerField()),
                ('videoNo', models.IntegerField()),
                ('videobyte', models.BinaryField()),
            ],
            options={
                'db_table': 'IM_input_data',
            },
        ),
    ]
