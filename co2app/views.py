from django.shortcuts import render
from joblib import load
models=load('./savedmodels/model.joblib')
# Create your views here.
def predictor(request):
    return render(request,'main.html')
def formInfo(request):
    model=int(request.GET['model'])
    size=int(request.GET['size'])
    cylinder=int(request.GET['cylinder'])
    fuel=int(request.GET['fuel'])
    city=int(request.GET['city'])
    heavy=int(request.GET['heavy'])
    comb=int(request.GET['comb'])
    combm=int(request.GET['combm'])
    prediction=models.predict([[model,size,cylinder,fuel,city,heavy,comb,combm]])
    '''for i in y_pred:
        print(type(i))
    print("predicted value",y_pred)'''
    if(prediction<=100 or prediction<200):
        v="Less Emission"
    elif(prediction<=200 or prediction<300):
        v="Moderate Emission"
    elif(prediction<=300 or prediction<400):
        v="High emission"
    elif(prediction<=400 or prediction<500):
        v="Very high Emission"
    else:
        v="Please give the valid data, any of data you have given is incorrect"
    return render(request,'result.html',{'result':prediction,'pred':v})
    #return render(request,'result.html',{'result':prediction})
