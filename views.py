from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
import datetime
from django.template import loader
from polls.models import Question,Choice

def index(request):
	latest_question_list = Question.objects.all()
	template=loader.get_template('polls/index.html')
	context={'latest_question_list': latest_question_list, 'date':'2018/9/16', 'name':'RABIN'}
	return HttpResponse(template.render(context, request))

def ourblog(request):
	latest_question_list = Question.objects.all()
	template=loader.get_template('polls/ourblog.html')
	context={'latest_question_list': latest_question_list, 'date':'2018/9/16', 'name':'RABIN'}
	return HttpResponse(template.render(context, request))
	

def contact(request):
    return HttpResponse("<b>Contact</b>")

def date(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now <b>%s</b>.<br><p>I have displayed current date</p></body></html>" % now 
    return HttpResponse(html)

def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question': question,'title':'welcome tothe daetail page'})
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

