from django.db.models import fields
from timmyBlog.models import Post, Comment
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView,View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from timmyBlog.forms import CommentForm, PostForm
from cloudinary.forms import cl_init_js_callbacks 

# Create your views here.
class HomePage(ListView):
    model = Post
    template_name = 'homePage.html'
    ordering = ['-post_date']


class DetailPost(DetailView):
    model = Post
    template_name = 'detail-post.html'


    def get_context_data(self, **kwargs):
        context = super(DetailPost, self).get_context_data()
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        show_like = True
        show_dislike = True
        total_likes = stuff.number_of_likes()
        total_dislikes = stuff.number_of_dislikes()
        if stuff.likes.filter(id=self.request.user.id).exists() and not stuff.dislikes.filter(id=self.request.user.id).exists():
            show_like = False
            show_dislike = True
        elif not stuff.likes.filter(id=self.request.user.id).exists() and stuff.dislikes.filter(id=self.request.user.id).exists():
            show_like = True
            show_dislike = False
        elif not stuff.likes.filter(id=self.request.user.id).exists() and not stuff.dislikes.filter(id=self.request.user.id).exists():
            show_like = True
            show_dislike = True
        else:
            None 
        context["total_dislikes"] = total_dislikes
        context["show_dislike"] = show_dislike
        context["total_likes"] = total_likes
        context["show_like"] = show_like
        return context



class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'



class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'



class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add-comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists() and not post.dislikes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    elif not post.likes.filter(id=request.user.id).exists() and post.dislikes.filter(id=request.user.id).exists():
        None
    elif not post.likes.filter(id=request.user.id).exists() and not post.dislikes.filter(id=request.user.id).exists():
        post.likes.add(request.user)
    else:
        None
    return HttpResponseRedirect(reverse('detail-post', args=[str(pk)]))


def DislikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('dislike_id'))
    if post.dislikes.filter(id=request.user.id).exists() and not post.likes.filter(id=request.user.id).exists():
        post.dislikes.remove(request.user)
    elif not post.dislikes.filter(id=request.user.id).exists() and post.likes.filter(id=request.user.id).exists():
        None
    elif not post.dislikes.filter(id=request.user.id).exists() and not post.likes.filter(id=request.user.id).exists():
        post.dislikes.add(request.user)
    else:
        None
    return HttpResponseRedirect(reverse('detail-post', args=[str(pk)]))