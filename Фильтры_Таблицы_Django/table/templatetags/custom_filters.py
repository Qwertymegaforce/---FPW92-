from django import template

register = template.Library()

trashtalk = {
    'Черт!' : '*'*4
}

@register.filter()
def cursed_words(word):
    i = -1
    word_super = word.split(' ')
    for letter in word_super:
        i += 1
        if letter in trashtalk:
            word_super[i:] = trashtalk[f'{letter}']
    return f'{" ".join(word_super)}'
