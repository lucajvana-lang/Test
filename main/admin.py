from django.contrib import admin
from .models import Game, GameImage, Tip, Hobby

class GameImageInline(admin.TabularInline):
    model = GameImage
    extra = 2

class TipInline(admin.StackedInline):
    model = Tip
    extra = 1

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'hours_played')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [GameImageInline, TipInline]

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon')

@admin.register(GameImage)
class GameImageAdmin(admin.ModelAdmin):
    list_display = ('game', 'caption')
    list_filter = ('game',)

@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    list_display = ('game', 'title', 'created_at')
    list_filter = ('game',)
