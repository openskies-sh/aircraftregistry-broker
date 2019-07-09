from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode

import json


# @login_required
# def dashboard(request):
#     user = request.user
#     auth0user = user.social_auth.get(provider='auth0')
#     userdata = {
#         'user_id': auth0user.uid,
#         'name': user.first_name,
#         # 'picture': auth0user.extra_data['picture']
#     }

#     return render(request, 'dashboard.html', {
#         'auth0User': auth0user,
#         'userdata': json.dumps(userdata, indent=4)
#     })

def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)

# def public(request):
#     return JsonResponse({'message': 'Hello from a public endpoint! You don\'t need to be authenticated to see this.'})


# @api_view(['GET'])
# def private(request):
#     return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated to see this.'})


# @api_view(['GET'])
# @requires_scope('read:rpas')
# def private_rpas(request):
#     return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated and have a scope of read:rpas to see this.'})

# @api_view(['GET'])
# @requires_scope('read:operator')
# def private_operator(request):
#     return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated and have a scope of read:operator to see this.'})