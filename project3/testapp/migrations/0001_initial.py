# Generated by Django 3.1.2 on 2020-11-08 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='datamodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NO', models.IntegerField()),
                ('Challan_Tender_Date', models.DateField()),
                ('Challan_Serial_No', models.IntegerField(unique=True)),
                ('Received_Date', models.DateField()),
                ('Major_Head_Code', models.CharField(max_length=100)),
                ('Minor_Head_Code', models.IntegerField()),
                ('Nature_Of_Payment', models.CharField(max_length=100)),
                ('Status', models.BooleanField()),
                ('Amount', models.FloatField()),
            ],
        ),
    ]