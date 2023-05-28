# Generated by Django 4.2.1 on 2023-05-28 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='viaje',
            old_name='Alojamiento',
            new_name='alojamiento',
        ),
        migrations.RenameField(
            model_name='viaje',
            old_name='DesplazamientoIda',
            new_name='desplazamientoIda',
        ),
        migrations.RenameField(
            model_name='viaje',
            old_name='DesplazamientoVuelta',
            new_name='desplazamientoVuelta',
        ),
        migrations.RenameField(
            model_name='viaje',
            old_name='Paquete',
            new_name='paquete',
        ),
        migrations.RenameField(
            model_name='viaje',
            old_name='Usuario',
            new_name='usuario',
        ),
        migrations.RemoveField(
            model_name='alojamiento',
            name='fotos',
        ),
        migrations.AddField(
            model_name='desplazamiento',
            name='origen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='viaje_origen', to='principal.destino'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paquete',
            name='destino',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='principal.destino'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='desplazamiento',
            name='destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viaje_destino', to='principal.destino'),
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='viajes', verbose_name='foto')),
                ('alojamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.alojamiento')),
            ],
            options={
                'verbose_name': 'foto',
                'verbose_name_plural': 'fotos',
            },
        ),
    ]