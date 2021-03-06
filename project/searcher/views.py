from django.shortcuts import render
from django.urls import reverse

from django.views.generic import (
  FormView, ListView
)
from django.db.models import Q
from functools import reduce
from account.models import Profile
from .forms import SearchForm

from django.shortcuts import redirect
from django.core import serializers
from friendship.models import Friendship

from helpers import _decorate_name

class ResultsView(ListView):
  template_name = 'searcher/results.html'
  context_object_name = 'profiles'
  paginate_by = 5

  def get(self, *args, **kwargs):
    return super(ResultsView, self).get(*args, **kwargs)

  def get_queryset(self):
    return list(serializers.deserialize('json',self.request.session['results']))

  def get_context_data(self, **kwargs):
    context = {
      # 'profiles': serializers.deserialize('json',self.request.session['results']),
      'friends': self.request.user.profile.get_user_friends(),
    }
    return super(ResultsView, self).get_context_data(**context)

class SearchView(FormView):
  form_class = SearchForm
  template_name = 'searcher/user_search.html'
 
  @property
  def success_url(self):
    return reverse('searcher:results')

  def form_valid(self, form):
    if not form.cleaned_data:
      return self.form_invalid(form)

    qs = self.lookup_account_function(form.cleaned_data)
    self.request.session['results'] = serializers.serialize('json', qs)
    return super(SearchView, self).form_valid(form)

  def lookup_account_function(self, fields):
    lookup_dict = {
      'email': Q(user__email__istartswith=fields.get('email')) ,
      'first_name': Q(user__first_name__istartswith=fields.get('first_name')),
      'last_name': Q(user__last_name__istartswith=fields.get('last_name')),
      'skill_serial1': Q(skill__data__id=fields.get('skill_serial1')),
      'skill_serial2': Q(skill__data__id=fields.get('skill_serial2')),
      'project_name': Q(projectpages___name__istartswith=fields.get('project_name'))
    }
    predicate = reduce(Q.__and__, [ lookup_dict.get(k) for k in lookup_dict.keys() if fields.get(k) ])
    results = Profile.objects.filter(predicate).exclude(user=self.request.user)
    return results
