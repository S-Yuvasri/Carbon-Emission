from django.shortcuts import render
#from django.http import HttpResponse
def Welcome(request):
    return render(request,'home.html')
def User(request):
    username=request.GET['username']
    #print(username)
    return render(request, 'user.html',{'name':username})