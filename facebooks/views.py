from django.shortcuts import render

# Create your views here.
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    """home page for facebooks"""
    return render(request, 'facebooks/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request,'facebooks/topics.html', context)


def topic(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'facebooks/topic.html',context)


def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('facebooks:topics'))

    context = {'form': form}
    return render(request, 'facebooks/new_topic.html',
                  context)


def new_entry(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('facebooks:topic',args=[topic_id]))

    context = {'topic':topic,'form': form}
    return render(request, 'facebooks/new_entry.html', context)
