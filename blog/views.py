from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Post
from .forms import PostCreateForm
class BlogListView(View):
    def get(self,request,*args,**kwargs):
        context={
            
        }
        return render(request,'blog_list.html',context)
 
class BlogCreateView(View):
     def get(self,request,*args,**kwargs):
         return render(request,"create_post.html",{'form':PostCreateForm()})
        
     def post(self,request,*args,**kwargs):
         if request.method == "POST":
             form = PostCreateForm(request.POST)
             if form.is_valid():
                 title = form.cleaned_data.get('title')
                 content = form.cleaned_data.get('content')
                 p,created = Post.objects.get_or_create(title=title,content=content)
                 p.save()
                 return redirect('blog:create')         