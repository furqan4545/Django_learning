from django.shortcuts import render, get_object_or_404, redirect 
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy   
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
class AboutView(TemplateView):
    template_name = "about.html"
    # now we need to specify this file path in urls.py file.
    # remember first of all we need to specify general path to default urls.py file

class PostListView(ListView):
    model = Post

    # Here I m creating sql query that I want to perform on my Post model.
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')  # i m saying grab the post model and grab all the objects
        # inside the Post model. filter out base on these conditions which are grab the published_date and specifying __lte mean less than or equal to. 
        # after grabing the published_date objects order them by ascending order/descending order. - sign indentifies the order. so in - minus most recent
        # blogs will come on the top of list view. 
    # so now lets add this view to urls.py file

class PostDetailView(DetailView):
    model = Post
    # rest of the things it will take care for you. 


# In class based views: for authentication that either the use is logged in or not, we use LoginRquiredMixin
class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'  # so in case if the person is not logged in, he will go to this url.
    redirect_field_name = 'blog/post_detail.html'  # so once the person get logged in he will be redirected to this url. 
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'  # so in case if the person is not logged in, he will go to this url.
    redirect_field_name = 'blog/post_detail.html'  # so once the person get logged in he will be redirected to this url. 
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post  # we r connecting to the model from which we will delete things
    success_url = reverse_lazy("post_list")   # after deleting successfully u will get redirected to this url.


# This will list my unpublished post/drafts. This view is to show my drafts or unpublished posts.
class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    # now i will write a query to specify that I only need those records which doesnt have publication date with them.
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')  # grab only those records which doesnt have publication date.    


##################################################################################################
##################################################################################################

# From here we will work on function based views. 
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)



@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    post_pk = comment.post.pk  # here I m storing post id
    comment.delete()  # here i m deleting the comment from that post
    return redirect('post_detail', pk=post_pk)  # here I m redirecting my user to post again after deleting comment. 
    # we stored the post primary key previously before deleting blc if delete the comment then we would have lost the primary key of the post too.








         