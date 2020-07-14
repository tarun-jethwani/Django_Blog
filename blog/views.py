from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView


# posts = [
#     {
#         'author': 'A. P. J. Abdul Kalam',
#         'title': 'Past',
#         'content': 'Accept your past without regret ! \n Handle your present with confidence \n and Face you future without fear',
#         'date_posted': "January 26th 2003"
#     },
#     {
#         'author': 'Napolean Bonaparte',
#         'title': 'Victory',
#         'content': 'Victory is not always winning the battle \n but rising everytime you fall',
#         'date_posted': 'March 11th 1706'
#     },
#
# ]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# Create your views here.
