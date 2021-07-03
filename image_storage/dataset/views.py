from django.urls import reverse
from django.db.models.query import QuerySet

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView

from .models import Dataset


class ListView(LoginRequiredMixin, ListView):
    model = Dataset
    template_name = 'dataset/list.html'
    context_object_name = 'datasets'

    def get_queryset(self) -> QuerySet[Dataset]:
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)

# Create your views here.
class CreateView(LoginRequiredMixin, CreateView):
    model = Dataset
    fields = ['name']
    template_name = 'dataset/create.html'

    def get_success_url(self) -> str:
        """ Add owner to newly created dataset object """
        print(dir(self))
        object = self.object
        object.owner = self.request.user
        object.save()
        return reverse('dashboard:index') 