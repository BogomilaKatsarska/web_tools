#middlewares can be seen as decorators for the views
#'get_response' gets the response from the next middleware or view
from django.shortcuts import redirect
from django.utils import timezone


def measure_time_middleware(get_response):
    def middleware(request, *args, **kwargs):
        start_time = timezone.now

        response = get_response(request, *args, **kwargs)

        end_time = timezone.now()
        print(f'executed in {end_time-start_time}')

        return response

    return middleware


class MeasureTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        start_time = timezone.now

        response = self.get_response(request, *args, **kwargs)

        end_time = timezone.now()
        print(f'executed in {end_time - start_time}')
        return response


def redirect_to_index_on_error_middleware(get_response):
    def middleware(*args, **kwargs):
        response = get_response(*args, **kwargs)
        if response.status_code == 500:
            return redirect('index')
        return response

    return middleware
