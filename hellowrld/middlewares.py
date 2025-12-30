from django.http import HttpResponseForbidden

class FiltraIPMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, func, args, kwargs):
        ips_autorizados = ['127.0.0.1']
        ip = request.META.get('REMOTE_ADDR')

        if ip not in ips_autorizados:
            return HttpResponseForbidden("IP não autorizado")

        return None
