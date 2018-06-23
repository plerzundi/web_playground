from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Thread
from django.http import Http404

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name="dispatch")
class ThreadList(TemplateView):
    template_name = "messenger/thread_list.html"

    """
    def get_queryset(self):
        queryset = super(ThreadList, self).get_queryset()
        return queryset.filter(users=self.request.user)   
    """

@method_decorator(login_required, name="dispatch")
class ThreadDetail(DetailView):
    model = Thread


    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404
        return obj

