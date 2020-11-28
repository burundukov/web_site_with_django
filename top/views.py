from django.shortcuts import render
from .models import News 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ShowNewsView(ListView):
	model = News
	template_name = 'top/index.html'
	context_object_name = 'info'
	ordering = ['-date']

	def get_context_data(self, **kwards):
		context = super(ShowNewsView, self).get_context_data(**kwards)
		context['title'] = "Главная страница сайта"

		return context


class NewsDetailView(DetailView):
	model = News
	
	def get_context_data(self, **kwards):
		context = super(NewsDetailView, self).get_context_data(**kwards)
		context['title'] = News.objects.filter(pk = self.kwargs['pk']).first()

		return context

class CreateNewsView(LoginRequiredMixin, CreateView):
	model = News
	fields = ['title', 'text']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = News
	fields = ['title', 'text']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		news = self.get_object()
		if self.request.user == news.author:
			return True
		else:
			return False

class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = News
	success_url='/'

	def test_func(self):
		news = self.get_object()
		if self.request.user == news.author:
			return True
		else:
			return False

def top(request):
	data = {
		'info': News.objects.all(),
		'title': "Главная страница сайта",
	}
	return render(request, 'top/index.html', data)


def about(request):
	return render(request, 'top/about.html', {'title': "Страница о нас. Мы пока не расскажем о себе."})