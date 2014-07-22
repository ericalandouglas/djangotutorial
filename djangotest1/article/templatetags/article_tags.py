from django import template

register = template.Library() # decorator

@register.filter(name='article_shorten_body') # tmeplate uses this name
def article_shorten_body(bodytext, length):
	return "%s ..." % bodytext[:length] if len(bodytext) > length else bodytext
