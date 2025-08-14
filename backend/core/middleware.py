from django.db import connection

class SetCurrentUserIdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            with connection.cursor() as cursor:
                cursor.execute("SET app.current_user_id = %s", [str(request.user.id)])
        else:
            with connection.cursor() as cursor:
                cursor.execute("RESET app.current_user_id")
        response = self.get_response(request)
        return response