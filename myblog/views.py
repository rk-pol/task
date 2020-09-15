from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from re import *
from .models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def post(request):
	user_valid = False
	if request.user.is_authenticated:
		user_valid = True
	object_list = Article.objects.all().order_by('published')
	paginator = Paginator(object_list, 10)  # 10 поста на каждой странице
	page = request.GET.get('page')
	try:
		article_list = paginator.page(page)
	except PageNotAnInteger:
		article_list = paginator.page(1)
	except EmptyPage:
		article_list = paginator.page(paginator.num_pages)
	return render(request,  
			'content.html',  
			{'page': page,  
			'article_list': article_list,
			'user_valid':user_valid})
#
def email_valid(email):
	pattern = compile(r'(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
	is_valid = pattern.match(str(email))
	if not is_valid:
		error_msg = 'Email введен неверно'
		return error_msg

#
def amout_articles(articles):
    amount_articles = len(articles)
    amount_digits_pang = amount_articles%10 
    remainder = amount_articles//10
    if remainder > 0:
    	amount_digits_pang += 1
    return amount_digits_pang


#
class Sign_inView(TemplateView):
	template_name = "sign_in.html"
	def dispatch(self, request, *args, **kwargs):	
		errors = {}
		if request.method == 'POST':
			email = request.POST['email']
			password = request.POST['password']
			try:
			   user = User.objects.get(email=email)
			except Exception:
			   user = None   
			if user is not None:
				login(request, user)
				return redirect("{0}?page=1".format(reverse('post')))
			else:
				errors['error'] = 'Email или пароль не правильный.'	 
		return render(request, self.template_name, {'errors':errors})

#
class registrate(TemplateView):
	template_name = 'registrate.html'

	def dispatch(self, request, *args, **kwargs):
		errors = {}
		if request.method == 'POST':
			username = request.POST.get('username')
			email = request.POST.get('email')
			password1 = request.POST.get('password1')
			password2 = request.POST.get('password2')

			try:
				free_email = User.objects.get(email=email)
			except Exception:
				free_email = None

			email_valid_error = email_valid(email)
			if email_valid_error is not None:
				errors['email_valid_error'] = email_valid_error
			if free_email is not None: 
				errors['email'] = 'Email уже зарегестирирован'					
			if password1 != password2:
				errors['password'] = 'Пароли не совпадают'
			if not errors:
				user = User.objects.create_user(username, email, password1)
				user.save()	
				login(request, user)
				return redirect('/')		
		return render(request, self.template_name, {'errors':errors}) 	 	

#
def logout_view(request):
	errors = {}
	if request.user.is_authenticated: 
		logout(request)
	return redirect("{0}?page=1".format(reverse('post')))	

#
def article(request, id_article):
	article = Article.objects.get(id=id_article)
	url = 'article.html'
	return render(request, url, {'article':article})	