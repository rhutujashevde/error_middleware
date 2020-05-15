from datetime import datetime
import json

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http.response import JsonResponse
from rest_framework import serializers
from rest_framework.views import APIView

from .models import ErrorStack


class ErrorStackAPI(APIView):
    def get(self, request):
        try:
            stack_id = request.GET.get('stack_id')
            search = request.GET.get('search') or 0
            data = ErrorStack.objects.filter(
                Q(id=stack_id)
                |Q(
                    Q(method=search)
                    | Q(error=search)
                    | Q(error_stack=search)
                )
            ).values()

            if not data:
                return JsonResponse(
                    {
                        "message": "Not Found",
                        "data": None
                    }, status=404
                )

            return JsonResponse({
                "message": "Read Successful",
                "data": list(data)
            })
        except Exception as e:
            return JsonResponse(
                {
                    "message": "Something went wrong",
                    "data": str(e)
                }, status=500
            )

    def post(self, request):
        try:
            request_data = request.data
            error_stack_object = ErrorStack.objects.create(
                request = request_data.get('request'),
                method = request_data.get('method'),
                response = request_data.get('response'),
                error = request_data.get('status_code'),
                error_stack = request_data.get('error_stack'),
                created_date = datetime.now(),
                modified_date = datetime.now(),
            )

            return JsonResponse({
                "message": "Create Successful",
                "data": None
            })

        except Exception as e:
            return JsonResponse(
                {
                    "message": "Something went wrong",
                    "data": str(e)
                }, status=500
            )


    def put(self, request):
        try:
            request_data = request.data
            stack_id = request_data.get("stack_id")
            stack_object = ErrorStack.objects.get(
                id=stack_id
            )
            if not stack_object:
                return JsonResponse(
                    {
                        "message": "Not Found",
                        "data": None
                    },
                    status=404
                )
            if request_data.get('request'):
                stack_object.request = request_data.get('request')
            if request_data.get('method'):
                stack_object.method = request_data.get('method')
            if request_data.get('response'):
                stack_object.response = request_data.get('response')
            if request_data.get('status_code'):
                stack_object.error = request_data.get('status_code')
            if request_data.get('error_stack'):
                stack_object.error_stack = request_data.get('error_stack')
            stack_object.modified_date = datetime.now()
            stack_object.save()

            return JsonResponse({
                "message": "Update Successful",
                "data": None
            })

        except ObjectDoesNotExist:
                return JsonResponse(
                    {
                        "message": "Not Found",
                        "data": None
                    }, status=404
                )

        except Exception as e:
            return JsonResponse(
                {
                    "message": "Something went wrong",
                    "data": str(e)
                }, status=500
            )


    def delete(self, request):
        try:
            request_data = request.data
            stack_id = request_data.get("stack_id")
            ErrorStack.objects.filter(id=stack_id).delete()

            return JsonResponse({
                "message": "Delete Successful",
                "data": None
            })

        except Exception as e:
            return JsonResponse(
                {
                    "message": "Something went wrong",
                    "data": str(e)
                }, status=500
            )