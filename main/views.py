from django.shortcuts import render, get_object_or_404
from .models import Game, GameImage, Hobby, Tip

def index(request):
    games = Game.objects.all()
    hobbies = Hobby.objects.all()
    latest_tips = Tip.objects.select_related('game').order_by('-created_at')[:5]
    
    context = {
        'author_name': 'Луцай Иван Григорьевич',
        'games': games,
        'hobbies': hobbies,
        'latest_tips': latest_tips,
    }
    return render(request, 'main/index.html', context)

def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'main/game_detail.html', {'game': game})

def gallery(request):
    selected_game_id = request.GET.get('game')
    games = Game.objects.all()
    
    if selected_game_id:
        images = GameImage.objects.filter(game_id=selected_game_id)
    else:
        images = GameImage.objects.all()

    context = {
        'games': games,
        'images': images,
        'selected_game_id': selected_game_id,
    }
    return render(request, 'main/gallery.html', context)
