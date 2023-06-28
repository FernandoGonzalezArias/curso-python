from django.shortcuts import render


def books_list(request):
    context = {'valores':[0,1,2,3,4,5], 'name': 'Fernando Gonzalez'}
    return render(request, 'books_list.html', context)
