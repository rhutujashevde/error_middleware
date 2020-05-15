import json

from .models import ErrorStack
from datetime import datetime

from django.utils.deprecation import MiddlewareMixin
from django.http.response import JsonResponse

class ErrorStackMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        request_data = {
            "META": request.META,
            "data": request.POST,
            "params": request.GET
        }
        error_stack = response.reason_phrase if response.status_code != 200 else None
        error_stack_object = ErrorStack.objects.create(
            request = request_data,
            method = request.method,
            response = response.content,
            error = response.status_code,
            error_stack = error_stack,
            created_date = datetime.now(),
            modified_date = datetime.now(),
        )
        return response