# Generated by Django 2.0 on 2017-12-03 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BindHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(max_length=256)),
                ('ip_addr', models.GenericIPAddressField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('bind_hosts', models.ManyToManyField(to='audit.BindHost')),
            ],
        ),
        migrations.CreateModel(
            name='HostUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('auth_type', models.PositiveSmallIntegerField(choices=[(0, 'Password'), (1, 'KEY')])),
                ('password', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='date_of_birth',
        ),
        migrations.AlterUniqueTogether(
            name='hostuser',
            unique_together={('username', 'auth_type', 'password')},
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='audit.IDC'),
        ),
        migrations.AddField(
            model_name='bindhost',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='audit.Host'),
        ),
        migrations.AddField(
            model_name='bindhost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='audit.HostUser'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bind_hosts',
            field=models.ManyToManyField(to='audit.BindHost'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='host_groups',
            field=models.ManyToManyField(to='audit.HostGroup'),
        ),
        migrations.AlterUniqueTogether(
            name='bindhost',
            unique_together={('host', 'user')},
        ),
    ]
