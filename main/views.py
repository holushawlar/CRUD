from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Goal
from .forms import GoalCreateForm


# for the listing of the whole todo items
class TodoListView(ListView):
    queryset = Goal.objects.all()
    template_name = "todo/goal_list.html"

# for the details of the individual goals element
class TodoDetailView(DetailView):
    queryset = Goal.objects.all()
    template_name = 'todo/goal_detail.html'

# for the creation of a new goal item from the frontend of the application
class GoalCreateView(CreateView):
    queryset = Goal.objects.all()
    template_name = "todo/goal_form.html"
    form_class = GoalCreateForm

    def form_valid(self, form):
        return super().form_valid(form)

# for the updating of the created goals elements
class GoalUpdateView(UpdateView):
    queryset = Goal.objects.all()
    template_name = "todo/goal_form.html"
    form_class = GoalCreateForm

    def form_valid(self, form):
        return super().form_valid(form)
        
# for the deleting of a goal item
class GoalDeleteView(DeleteView):
    queryset = Goal.objects.all()
    template_name = "todo/goal_delete.html"

    def get_success_url(self):
        return reverse("todo:home")