from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(func_view):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return func_view(request, *args, **kwargs)
    return wrapper_func

def allower_user(allower_roles=[]):
    def decorator(func_view):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allower_roles:
                return func_view(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page.')
        return wrapper_func
    return decorator


def admin_only(func_view):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('/products/customer')

        if group == "admin":
            return func_view(request, *args, **kwargs)
    return wrapper_func