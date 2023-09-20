from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = f'resultados da pergunta número {question_id}'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

from django.views.generic import CreateView, ListView, DetailView,DeleteView, UpdateView
from django.urls import reverse_lazy

class QuestionCreateView(CreateView):
    model = Question 
    fields = ('question_text',)
    success_url = reverse_lazy('index')
    template_name = 'polls/question_form.html'

class QuestionlistView(ListView):
    model = Question
    context_object_name = 'questions'

class QuestionDetailview(DetailView):
    model = Question
    context_object_name = 'question'

from django.contrib import messages

class QuestionDeleteView(DeleteView):
    model = Question
    success_url = reverse_lazy("question-list")
    success_message = "Enquete excluída com sucesso."

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

class QuestionUpdateView(UpdateView):
    model = Question
    success_url = reverse_lazy('question-list')
    fields = ('question_text',)