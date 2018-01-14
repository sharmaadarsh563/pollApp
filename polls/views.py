from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# from django.views.decorators.cache import cache_page

from .models import Question, Choice

# @cache_page(60*15)
@login_required
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {
		'latest_question_list': latest_question_list,
	}
	return render(request, 'polls/index.html', context)

@login_required
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	context = {'question': question}
	return render(request, 'polls/detail.html', context)

@login_required
def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	context = {'question': question}
	return render(request, 'polls/results.html', context)

@login_required
def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice."
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=
			(question_id,)))