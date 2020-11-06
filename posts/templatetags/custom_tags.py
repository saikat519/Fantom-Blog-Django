from django import template


from posts.models import Category

from posts.models import Tag,Post

register = template.Library()

@register.simple_tag(name="categories")
def all_category():
    return Category.objects.all()


@register.simple_tag(name="tags")
def all_tags():
    return Tag.objects.all()

@register.simple_tag(name="hit_posts")
def hit_post():
    return Post.objects.order_by('-hit')[:5]
