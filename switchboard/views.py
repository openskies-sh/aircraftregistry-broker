import datetime
import json
from datetime import datetime
from django.views.generic.edit import FormView, CreateView
from .forms import SearchQueryForm
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.utils import translation
from django.views.generic import TemplateView
from rest_framework import generics, mixins, status, viewsets
from rest_framework.authentication import (SessionAuthentication, TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import reverse_lazy
from .models import SearchQuery
from .serializers import (SearchQuerySerializer)
from django.urls import reverse
from .tasks import QueryRegistries
from django.utils.decorators import method_decorator
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

# class AccessMixin:
#     """
#     Abstract CBV mixin that gives access mixins the same customizable
#     functionality.
#     """
#     login_url = None
#     permission_denied_message = ''
#     raise_exception = False
#     redirect_field_name = REDIRECT_FIELD_NAME

#     def get_login_url(self):
#         """
#         Override this method to override the login_url attribute.
#         """
#         login_url = self.login_url or settings.LOGIN_URL
#         if not login_url:
#             raise ImproperlyConfigured(
#                 '{0} is missing the login_url attribute. Define {0}.login_url, settings.LOGIN_URL, or override '
#                 '{0}.get_login_url().'.format(self.__class__.__name__)
#             )
#         return str(login_url)

#     def get_permission_denied_message(self):
#         """
#         Override this method to override the permission_denied_message attribute.
#         """
#         return self.permission_denied_message

#     def get_redirect_field_name(self):
#         """
#         Override this method to override the redirect_field_name attribute.
#         """
#         return self.redirect_field_name

#     def handle_no_permission(self):
#         if self.raise_exception:
#             raise PermissionDenied(self.get_permission_denied_message())
#         return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())


# class LoginRequiredMixin(AccessMixin):
#     """Verify that the current user is authenticated."""
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return self.handle_no_permission()
#         return super().dispatch(request, *args, **kwargs)

# class AjaxableResponseMixin:

#     """
#     Mixin to add AJAX support to a form.
#     Must be used with an object-based FormView (e.g. CreateView)
#     """

#     def form_invalid(self, form):
#         response = super().form_invalid(form)
#         if self.request.is_ajax():
#             return JsonResponse(form.errors, status=400)
#         else:
#             return response

#     def form_valid(self, form):
#         # We make sure to call the parent's form_valid() method because
#         # it might do some processing (in the case of CreateView, it will
#         # call form.save() for example).
#         response = super().form_valid(form)
#         if self.request.is_ajax():
#             data = {
#                 'pk': self.object.pk,
#             }
#             return JsonResponse(data)
#         else:
#             return response

# Create your views here.

class SuccessView(TemplateView):

    template_name = 'switchboard/search_success.html'

class HomeView(TemplateView):

    template_name = 'switchboard/index.html'

class SearchView(LoginRequiredMixin,CreateView):
    
    template_name = 'switchboard/search.html'
    form_class = SearchQueryForm    
    

    def get_context_data(self, *args, **kwargs):
        # additional_context = {}
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        user = self.request.user
        auth0user = user.social_auth.get(provider='auth0')
       
        context['access_token'] = auth0user.access_token
        context['auth0user'] = auth0user
        
        return context
   
    def get_success_url(self):  
        job_id = str(self.object.id)
        QueryRegistries.delay(jobid = job_id)
        # content = {'Location': '/api/v1/jobs' + job_id}
        # return Response(content, status=status.HTTP_202_ACCEPTED)
        return '{}'.format(reverse('success',kwargs={'pk':self.object.id}))
        # return reverse('search_details',args=(self.object.id,))


class SearchDetails(mixins.RetrieveModelMixin,
				  generics.GenericAPIView):
	"""
	List all jobs in the database / return value for current job
	"""

	# authentication_classes = (SessionAuthentication,TokenAuthentication)
	# permission_classes = (IsAuthenticated,)

	queryset = SearchQuery.objects.all()
	serializer_class = SearchQuerySerializer


	def get(self, request, *args, **kwargs):
	    return self.retrieve(request, *args, **kwargs)
