# Generated by Django 3.0.5 on 2020-05-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20200503_0751'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'mst_enquiry_types',
            },
        ),
    ]
