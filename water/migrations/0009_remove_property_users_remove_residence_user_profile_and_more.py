# Generated by Django 4.2 on 2023-10-14 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('water', '0008_rename_persons_property_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='users',
        ),
        migrations.RemoveField(
            model_name='residence',
            name='user',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('properties', models.ManyToManyField(through='water.Residence', to='water.property')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='profiles',
            field=models.ManyToManyField(through='water.Residence', to='water.profile'),
        ),
        migrations.AddField(
            model_name='residence',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='water.profile'),
            preserve_default=False,
        ),
    ]
