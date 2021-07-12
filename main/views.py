from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Forum, Discussion
from .forms import RegisterUserForm, LoginForm, NewForumForm, NewDiscussionForm, NewReplyForm

# Create your views here.

def registerPage(request):
	form = RegisterUserForm()

	if request.method == 'POST':
	 	try:
	 		form = RegisterUserForm(request.POST)
	 		if form.is_valid():
	 			user = form.save()
	 			login(request, user)
	 			return redirect('index')
	 	except Exception as e:
	 		print (e)
	 		raise

	context = {
		'form': form
	}
	return render(request, 'register.html', context)

def loginPage(request):
	form = LoginForm()

	if request.method == 'POST':
		try:
			form = LoginForm(data=request.POST)
			if form.is_valid():
				user = form.get_user()
				login(request, user)
				return redirect('index')
		except Exception as e:
			print(e)
			raise

	context = {'form': form}
	return render(request, 'login.html', context)

@login_required(login_url='register')
def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='register')
def newForumPage(request):
	form = NewForumForm()

	if request.method == 'POST':
		try:
			form = NewForumForm(request.POST)
			if form.is_valid():
				forum = form.save(commit=False)
				forum.author = request.user
				forum.save()
		except Exception as e:
			print(e)
			raise

	context = {'form': form}
	return render(request, 'new-forum.html', context)

def homePage(request):
	forums = Forum.objects.all().order_by('created_at')
	context = {
		'forums': forums
	}
	return render(request,'homePage.html', context)


def forumPage(request, id):
	discussion_form = NewDiscussionForm()
	reply_form = NewReplyForm()

	if request.method == 'POST':
		try:
			discussion_form = NewDiscussionForm(request.POST)
			if discussion_form.is_valid():
				discussion = discussion_form.save(commit=False)
				discussion.user = request.user
				discussion.forum = Forum(id=id)
				discussion.save()
				return redirect('/forum/'+str(id)+'#'+str(discussion.id))
		except Exception as e:
			print(e)
			raise

	forum = Forum.objects.get(id=id)
	context = {
		'forum': forum,
		'discussion_form': discussion_form,
		'reply_form': reply_form,
	}
	return render(request, 'forum.html', context)

@login_required(login_url='register')
def replyPage(request):
	if request.method == 'POST':
		try:
			form = NewReplyForm(request.POST)
			if form.is_valid():
				forum_id = request.POST.get('forum')
				parent_id = request.POST.get('parent')
				reply = form.save(commit=False)
				reply.user = request.user
				reply.forum = Forum(id=forum_id)
				reply.parent = Discussion(id=parent_id)
				reply.save()
				return redirect('/forum/'+str(forum_id)+'#'+str(reply.id))
		except Exception as e:
			print(e)
			raise

	return redirect('index')