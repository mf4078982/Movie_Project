from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render,HttpResponseRedirect
from .models import MovieModel
from .forms import MovieForm, registrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout



# Create your views here.

def movie(request, id):
    # Retrieve the specific movie using the id
    movie = MovieModel.objects.get(pk=id)
    return render(request, 'movie_detail.html', {'movie': movie})

@login_required
def movie_list(request):
    movies = MovieModel.objects.all()
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            form = MovieForm()
    else:
        form = MovieForm()
    return render(request, 'movie_list.html', {'form': form, 'movies': movies})        
    
@login_required   
def show(request):
    show_movie = MovieModel.objects.all()
    return render(request, 'show_movie.html',{'show_movie':show_movie}) 

@login_required
def edit(request, id):
    movie = MovieModel.objects.get(pk=id)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/show/')
    else:
        form = MovieForm(instance=movie)
    
    return render(request, 'edit.html', {'form': form})
@login_required
def delete_movie(request, id):
    movie = MovieModel.objects.get(id=id)
    if request.method == 'POST':
        movie.delete()
        return HttpResponseRedirect('/show/')
    else:
        return render(request, 'delete.html', {'movie': movie})
    
    
def register(request):
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = registrationForm()
    return render(request, 'registration/register.html', {'form': form})    


def movieapp_view(request):
    return render(request, 'movieapp.html')

