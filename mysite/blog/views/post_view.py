from django.views import generic
from blog.models import Post    

class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"

class PostDetail(generic.DetailView):  # Certifique-se de que a classe está escrita corretamente
    model = Post
    template_name = "post_detail.html"
