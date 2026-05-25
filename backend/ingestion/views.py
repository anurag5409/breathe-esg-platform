from django.shortcuts import render

import pandas as pd

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *


class SAPUploadView(APIView):

    def post(self, request):

        if 'file' not in request.FILES:

            return Response(
                {"error": "No file uploaded"},
                status=status.HTTP_400_BAD_REQUEST
            )

        file = request.FILES['file']

        try:

            df = pd.read_csv(file)

            tenant, _ = Tenant.objects.get_or_create(
                name="Demo Enterprise"
            )

            source = DataSource.objects.create(
                tenant=tenant,
                source_type='sap',
                uploaded_by=request.user if request.user.is_authenticated else None,
                original_filename=file.name
            )

            created_records = []

            for _, row in df.iterrows():

                suspicious = False

                if float(row['amount']) > 100000:
                    suspicious = True

                record = EmissionRecord.objects.create(

                    tenant=tenant,
                    source=source,

                    category=row['category'],

                    scope='Scope 1',

                    activity_value=float(row['amount']),

                    activity_unit=row['unit'],

                    normalized_value=float(row['amount']),

                    normalized_unit='kgCO2e',

                    description=row['description'],

                    suspicious=suspicious
                )

                created_records.append(record.id)

            return Response({
                "message": "SAP upload successful",
                "records_created": len(created_records)
            })

        except Exception as e:

            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UtilityUploadView(APIView):

    def post(self, request):

        if 'file' not in request.FILES:

            return Response(
                {"error": "No file uploaded"},
                status=status.HTTP_400_BAD_REQUEST
            )

        file = request.FILES['file']

        try:

            df = pd.read_csv(file)

            tenant, _ = Tenant.objects.get_or_create(
                name="Demo Enterprise"
            )

            source = DataSource.objects.create(
                tenant=tenant,
                source_type='utility',
                uploaded_by=request.user if request.user.is_authenticated else None,
                original_filename=file.name
            )

            created_records = []

            for _, row in df.iterrows():

                suspicious = False

                if float(row['kwh']) > 10000:
                    suspicious = True

                record = EmissionRecord.objects.create(

                    tenant=tenant,
                    source=source,

                    category="Electricity",

                    scope='Scope 2',

                    activity_value=float(row['kwh']),

                    activity_unit='kWh',

                    normalized_value=float(row['kwh']) * 0.82,

                    normalized_unit='kgCO2e',

                    description=row['meter'],

                    suspicious=suspicious
                )

                created_records.append(record.id)

            return Response({
                "message": "Utility upload successful",
                "records_created": len(created_records)
            })

        except Exception as e:

            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TravelUploadView(APIView):

    def post(self, request):

        if 'file' not in request.FILES:

            return Response(
                {"error": "No file uploaded"},
                status=status.HTTP_400_BAD_REQUEST
            )

        file = request.FILES['file']

        try:

            df = pd.read_csv(file)

            tenant, _ = Tenant.objects.get_or_create(
                name="Demo Enterprise"
            )

            source = DataSource.objects.create(
                tenant=tenant,
                source_type='travel',
                uploaded_by=request.user if request.user.is_authenticated else None,
                original_filename=file.name
            )

            created_records = []

            for _, row in df.iterrows():

                suspicious = False

                if float(row['distance']) > 5000:
                    suspicious = True

                record = EmissionRecord.objects.create(

                    tenant=tenant,
                    source=source,

                    category=row['travel_type'],

                    scope='Scope 3',

                    activity_value=float(row['distance']),

                    activity_unit='km',

                    normalized_value=float(row['distance']) * 0.14,

                    normalized_unit='kgCO2e',

                    description=row['route'],

                    suspicious=suspicious
                )

                created_records.append(record.id)

            return Response({
                "message": "Travel upload successful",
                "records_created": len(created_records)
            })

        except Exception as e:

            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ReviewQueueView(APIView):

    def get(self, request):

        records = EmissionRecord.objects.all().order_by('-created_at')

        serializer = EmissionRecordSerializer(
            records,
            many=True
        )

        return Response(serializer.data)


class ApproveRecordView(APIView):

    def post(self, request, pk):

        try:

            record = EmissionRecord.objects.get(id=pk)

            record.status = 'approved'
            record.save()

            AuditLog.objects.create(
                record=record,
                action='approved',
                user=request.user if request.user.is_authenticated else None,
                notes='Approved by analyst'
            )

            return Response({
                "message": "Record approved"
            })

        except EmissionRecord.DoesNotExist:

            return Response(
                {"error": "Record not found"},
                status=404
            )