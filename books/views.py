from django.http import HttpResponseRedirect
from django.shortcuts import render

from books.forms import library_system
from books.models import book_data


# Create your views here.
def main(requests):
    if requests.method=='POST':
        bk = library_system(requests.POST)
        if bk.is_valid():
            # print(bk)
            bk.save()
            bk =library_system()
            return HttpResponseRedirect('/')
         
    else:
        bk =library_system()
    stud = book_data.objects.all()
    return render(requests,'main.html',{'form':bk,'data':stud})

def delete(requests,id):
    dat  = book_data.objects.get(pk=id)
    dat.delete()
    return HttpResponseRedirect('/')


def update(requests,id):
    if requests.method=='POST':
        dat = book_data.objects.get(pk=id)
        bk = library_system(requests.POST,instance=dat)
        if bk.is_valid():
            bk.save()
    else:
        dat = book_data.objects.get(pk=id)
        bk =library_system(instance=dat)
    return render(requests,'update.html',{'form':bk})