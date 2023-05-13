from django.shortcuts import redirect, render


def access_teacher(input_func):
    def wrapper(request, *args, **kwargs):
        print('Путь запроса:% s' % request.path)
        if not request.user.is_teacher and not (request.user.is_staff or request.user.is_admin):
            return redirect('main')
        return input_func(request, *args, **kwargs)

    return wrapper
