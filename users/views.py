from django.contrib.auth import get_user_model
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse


def lazy_load_users(request):
    page = request.POST.get('page')
    users = get_user_model().objects.all()

    # use Django's pagination
    # https://docs.djangoproject.com/en/dev/topics/pagination/
    results_per_page = 6
    paginator = Paginator(users, results_per_page)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(2)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    # build a html users list with the paginated users
    users_html = loader.render_to_string('users/lazy-list.html', {'user_list': users})

    # package output data and return it as a JSON object
    output_data = {'users_html': users_html, 'has_next': users.has_next()}
    return JsonResponse(output_data)
