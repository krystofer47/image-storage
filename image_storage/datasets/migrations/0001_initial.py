# Generated by Django 3.2.5 on 2021-07-10 18:53

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=16)),
                ('description', models.CharField(default='None', max_length=64)),
                ('annotation_file_format', models.CharField(choices=[('pascal_voc', 'Pascal VOC'), ('coco', 'COCO'), ('yolo', 'Yolo')], max_length=32)),
                ('labels', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), size=64)),
                ('owner', models.ForeignKey(db_column='owner', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.dataset')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('path', models.CharField(max_length=255)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.dataset')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('path', models.CharField(max_length=255)),
                ('format', models.CharField(max_length=32)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageTransaction',
            fields=[
                ('transaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='datasets.transaction')),
                ('images', models.ManyToManyField(to='datasets.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('datasets.transaction',),
        ),
    ]
