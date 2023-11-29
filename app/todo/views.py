from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import List, Announcement, Feedback


def home(request):
    context = {
        'lists': List.objects.all()
    }
    return render(request, 'todo/home.html', context)


class ListView(LoginRequiredMixin, ListView):
    model = List
    template_name = 'todo/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'lists'
    ordering = ['-date_posted']
    paginate_by = 5
    

class UserListsView(ListView):
    model = List
    template_name = 'todo/user_lists.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'lists'
    paginate_by = 5
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return List.objects.filter(author=user).order_by('-date_posted') 
    
    
class ListDetailView(DetailView):
    model = List
    

class ListCreateView(LoginRequiredMixin, CreateView):
    model = List
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
    
class ListUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = List
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        list = self.get_object()
        if self.request.user == list.author:
            return True
        return False
    
    
class ListDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = List
    success_url = '/'
    
    def test_func(self):
        list = self.get_object()
        if self.request.user == list.author:
            return True
        return False
    
    
def about(request):
    return render(request, 'todo/about.html', {'title': 'About'})
    
    
class AnnouncementsView(ListView):
    model = Announcement
    template_name = 'todo/announcements.html'  
    context_object_name = 'announcements'
    ordering = ['-date_posted']

    def get_queryset(self):
        user = get_object_or_404(User, username='cwm')
        return Announcement.objects.filter(author=user).order_by('-date_posted')


   
class FeedbackView(LoginRequiredMixin, CreateView):
    model = Feedback
    template_name = 'todo/feedback.html'
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        feedback = Feedback.objects.create(title=title, content=content, author=request.user)
        messages.success(request, 'Your feedback has been submitted successfully.')
        return redirect('feedback')
    
    
class CalendarView(ListView):
    
    def get(self, request):
    
        return render(request, 'todo/calendar.html', {'title': 'Calendar'})