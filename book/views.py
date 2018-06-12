import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from book.models import Book


# Create your views here.
def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponseRedirect('/admin/')
    return HttpResponse(html)
    # return render(request, 'index.html', {'time': now}, status='220')


def book_list(request):
    books = Book.objects.all()
    number = Book.objects.count()
    return render(request, 'list2.html', {'book_list': books, 'count': number})


@login_required
def book_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        description = request.POST.get('description')
        print(1, name, description)
        if not name or not description or not author:
            print('name or description is null')
            return render(request, 'add.html', {'message': '必须填写书名、作者、描述'})
        if Book.objects.filter(name=name):
            return render(request, 'add.html', {'message': '该书已经登记'})
        Book.objects.create(name=name, author=author, description=description)
        return HttpResponseRedirect('/book/')
    return render(request, 'add.html')


def book_show(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'show.html', {'book': book})


def book_edit(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'edit.html', {'book': book})


def book_update(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        name = request.POST.get('name')
        author = request.POST.get('author')
        description = request.POST.get('description')
        print('book_id', book_id)
        if not id:
            return HttpResponseRedirect('/book/')
        else:
            Book.objects.filter(id=book_id).update(name=name, author=author, description=description)
            return HttpResponseRedirect('/book/')
    return HttpResponseRedirect('/book/')


def book_delete(request, id):
    Book.objects.get(id=id).delete()
    return HttpResponseRedirect('/book/')


def get_book_list(request):
    books = Book.objects.all()
    data = []
    for b in books:
        book = {}
        book.setdefault('id', b.id)
        book.setdefault('name  ', b.name)
        book.setdefault('author', b.author)
        book.setdefault('description', b.description)
        data.append(book)
    return JsonResponse({'status': 200, 'data': data})


@csrf_exempt
def add_book(request):
    name = request.POST.get('name')
    if Book.objects.filter(name=name):
        return JsonResponse({'status': 403, 'message': 'book already exists.'})
    author = request.POST.get('author')
    description = request.POST.get('description')
    Book.objects.create(name=name, author=author, description=description)
    return JsonResponse({'status': 200, 'message': 'add book success'})


'''
https://docs.djangoproject.com/en/2.0/ref/request-response/
https://docs.djangoproject.com/en/2.0/topics/http/views/
https://docs.djangoproject.com/en/2.0/ref/models/fields/#charfield
https://docs.djangoproject.com/en/2.0/topics/db/queries/
https://v3.bootcss.com/examples/theme/
https://v3.bootcss.com/components
'''


