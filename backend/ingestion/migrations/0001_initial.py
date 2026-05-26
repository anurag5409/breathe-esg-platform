
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_type', models.CharField(choices=[('sap', 'SAP'), ('utility', 'Utility'), ('travel', 'Travel')], max_length=20)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('original_filename', models.CharField(max_length=255)),
                ('uploaded_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingestion.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='EmissionRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('scope', models.CharField(max_length=20)),
                ('activity_value', models.FloatField()),
                ('activity_unit', models.CharField(max_length=50)),
                ('normalized_value', models.FloatField(blank=True, null=True)),
                ('normalized_unit', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True)),
                ('suspicious', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingestion.datasource')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingestion.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingestion.emissionrecord')),
            ],
        ),
    ]
