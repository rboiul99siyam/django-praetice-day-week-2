from django.shortcuts import render,redirect
from first_app.forms import StudentData

def home(res):
    if res.method == 'POST':
        forms = StudentData(res.POST)
        if forms.is_valid():     
            print(forms.cleaned_data)
        return render(res,'home.html',{'form':forms})

    else:
        forms = StudentData()
        return render(res,'home.html',{'form':forms})
