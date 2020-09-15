from django import template

register = template.Library()

@register.filter
def changetime(value): 
	time = str(value).split(':')
	time_h = time[0]
	time_m = time[1]
	time_h = int(time_h) + 3
	new_time = str(time_h) + ':' + time_m
	return new_time