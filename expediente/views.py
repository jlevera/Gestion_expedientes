from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Carpeta
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.shortcuts import redirect


# Create your views here.
@login_required
def carpeta_list(request):
    posts = Carpeta.objects.all()
    return render(request, 'expediente/carpeta_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Carpeta, pk=pk)
    return render(request, 'expediente/carpeta_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.creado_por = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'expediente/carpeta_edit.html', {'form': form})