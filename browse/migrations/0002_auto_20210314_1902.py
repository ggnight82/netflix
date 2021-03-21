# Generated by Django 3.1.7 on 2021-03-14 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productions_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='actor',
            new_name='Actors',
        ),
        migrations.RenameModel(
            old_name='genre',
            new_name='Genres',
        ),
        migrations.RenameModel(
            old_name='video',
            new_name='Videos',
        ),
        migrations.AddField(
            model_name='contents',
            name='contents_productions',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='browse.productions'),
            preserve_default=False,
        ),
    ]