# Generated by Django 4.1.6 on 2023-03-02 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('numerology', '0007_pithagorascendingdiagonal_pithagordescendingdiagonal'),
    ]

    operations = [
        migrations.CreateModel(
            name='PithagorEights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.PositiveIntegerField(default=0)),
                ('text_result', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PithagorFives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.PositiveIntegerField(default=0)),
                ('text_result', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PithagorFours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.PositiveIntegerField(default=0)),
                ('text_result', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PithagorNines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.PositiveIntegerField(default=0)),
                ('text_result', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PithagorOnes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.PositiveIntegerField(default=0)),
                ('text_result', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PithagorSevens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.PositiveIntegerField(default=0)),
                ('text_result', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PithagorSixes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.PositiveIntegerField(default=0)),
                ('text_result', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PithagorThrees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.PositiveIntegerField(default=0)),
                ('text_result', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PithagorTwos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.PositiveIntegerField(default=0)),
                ('text_result', models.TextField()),
            ],
        ),
    ]
