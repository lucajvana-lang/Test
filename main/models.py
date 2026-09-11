from django.db import models

class Game(models.Model):
    title = models.CharField("Название игры", max_length=100)
    slug = models.SlugField("URL-метка", unique=True)
    description = models.TextField("Описание игры")
    genre = models.CharField("Жанр", max_length=50)
    hours_played = models.PositiveIntegerField("Часов сыграно", default=0)
    cover = models.ImageField("Обложка", upload_to='covers/', blank=True, null=True)

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

    def __str__(self):
        return self.title


class GameImage(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='images', verbose_name="Игра")
    image = models.ImageField("Скриншот", upload_to='gallery/')
    caption = models.CharField("Подпись к картинке", max_length=150, blank=True)

    class Meta:
        verbose_name = "Скриншот галереи"
        verbose_name_plural = "Скриншоты галереи"

    def __str__(self):
        return f"Скриншот {self.game.title} - {self.caption or 'Без названия'}"


class Tip(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='tips', verbose_name="Игра")
    title = models.CharField("Заголовок совета", max_length=150)
    content = models.TextField("Текст совета")
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)

    class Meta:
        verbose_name = "Совет по игре"
        verbose_name_plural = "Советы по играм"

    def __str__(self):
        return f"{self.game.title} — {self.title}"


class Hobby(models.Model):
    title = models.CharField("Увлечение", max_length=100)
    description = models.TextField("Описание")
    icon = models.CharField("Иконка (эмодзи)", max_length=10, default="🎮")

    class Meta:
        verbose_name = "Увлечение"
        verbose_name_plural = "Увлечения"

    def __str__(self):
        return self.title
