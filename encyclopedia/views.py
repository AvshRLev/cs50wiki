import markdown2
import html2markdown
from django.shortcuts import render
from django import forms
from random import choice

from . import util

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title")
    entry = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    if request.method == "POST": 
        query = request.POST.get('q')
        entry_list = [each_entry.lower() for each_entry in util.list_entries()]
        matches = [match for match in entry_list if query in match]

        if query in entry_list :
             return render(request, "encyclopedia/entry.html", {
            "title": query,
            "entry":  markdown2.markdown(util.get_entry(query))
            })
        elif query in matches:
            return render(request, "encyclopedia/searchsub.html", {
                "title": query,
                "matches": matches
            })
        else:
            return render(request, "encyclopedia/searchsub.html", {
                "title": query,
                "matches": matches
            })

    entry_list = [each_entry.lower() for each_entry in util.list_entries()]
    if entry.lower() in entry_list :
        return render(request, "encyclopedia/entry.html", {
        "title": entry,
        "entry": markdown2.markdown(util.get_entry(entry))
    })
    
    return render(request, "encyclopedia/entry.html", {
            "title": "Not Found",
            "entry": "<h1>The page you have requested was not found</h1>"
            })

def search(request):
    if request.method == "POST": 
        query = request.POST.get('q')
        entry_list = [each_entry.lower() for each_entry in util.list_entries()]
        if query in entry_list :
             return render(request, "encyclopedia/entry.html", {
            "title": entry,
            "entry":  markdown2.markdown(util.get_entry(entry))
            })

def new(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            new = form.cleaned_data["entry"]
            entry_list = [each_entry.lower() for each_entry in util.list_entries()]
            if title.lower() not in entry_list:
                util.save_entry(title, new)
                return render(request, "encyclopedia/entry.html", {
                    "title": title,
                    "entry": markdown2.markdown(util.get_entry(title))
                })
            else:
                return render(request, "encyclopedia/exists.html", {
                    "title": title
                })    
        else:
            render(request, "encyclopedia/new.html", {
                "form": form
            })
    return render(request, "encyclopedia/new.html", {
        "form": NewEntryForm()
        } )

def edit_save(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            new = form.cleaned_data["entry"]
            util.save_entry(title, new)
            return render(request, "encyclopedia/entry.html", {
                    "title": title,
                    "entry": markdown2.markdown(util.get_entry(title))
                })
    

def edit(request):
    title = request.POST.get('title')
    entry = request.POST.get('entry')
    return render(request, "encyclopedia/edit.html", {
        "form": NewEntryForm(initial={'title': title, 'entry': html2markdown.convert(entry)})
    })

def random(request):
    entry_list = [each_entry.lower() for each_entry in util.list_entries()]
    random = choice(entry_list)
    return entry(request, random)
