from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Author(models.Model):
    author_Relation = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_Author = models.IntegerField(default=0)

    def update_rating(self):
        post_rating = self.Post_set.aggregate(postRating=Sum('rating'))
        post_all = 0
        post_all += post_rating.get('postRating')

        comment_rating = self.author_Relation.Comment_set.aggregate(commentRating=Sum('rating'))
        comment_all = 0
        comment_all += comment_rating.get('commentRating')

        self.rating_Author = post_all * 3 + comment_all
        self.save()



class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)


class Post(models.Model):
    news = 'НВ'
    article = 'СТ'
    choice = [
        (news, 'Новость'),
        (article, 'Статья')
    ]
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    rating = models.IntegerField(default=0)
    text = models.TextField(default='Здесь ничего нет...')
    type = models.CharField(max_length=2, choices=choice, default=news)
    creation_date = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'Заголовок - {self.title}. Текст - {self.text[0:123] } ...'

class PostCategory(models.Model):
    post_related = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_related = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(default='Пользователь не оставил комментария')
    comment_creation_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

