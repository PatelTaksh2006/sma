from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import *
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Taksh','age':18})


# def paperTrading(request):
#     return render(request,'paperTrading.html')


def login_page(request):
    if request.method=="POST":
        # print("in post of login")
        form=LoginForm(request, data=request.POST)
        if form.is_valid():
            # remeberme=bool(request.POST["RememberMe"])
            # if remeberme:
            # print("form is valid")
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            role = form.cleaned_data["role"]
            user=authenticate(request,username=username,password=password,role=role)
            if user is not None:
                
                # request.SESSION['role']=user.role
                if user.role == role:
                    login(request,user)
                    if user.role=="investor":
                        return render(request,"user_dashboard.html")
                    else:
                        return render(request,"guider_dashboard.html")    
                else:
                    messages.error(request,"No such user found. Please try again.")
                    return render(request,"login.html",{"form":form})
            else:
                # print("sacho user nakh")
                return render(request,"login.html",{"form":form})
        else:
            # print("form j valid nathi")
            return render(request,"login.html",{"form":form})
            

    else:
        print("Login kar")
        form=LoginForm()
        return render(request,"login.html",{"form":form})
                            

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username=form.cleaned_data['username']
            # Prevent Investors from starting with a number

            user.save()

            # Store Guider username for display (without "1" prefix)

            # Create corresponding entry in Investor or Guider
            if user.role == "investor":
                Investor.objects.create(name=user.username, email=user.email)
            else:
                Guider.objects.create(name=user.username, email=user.email)

            messages.success(request, "Registration successful. Please log in.")
            return redirect("login")

        else:
            messages.error(request, "Please correct the errors in the form.")
            return render(request,"signup.html",{"form":form})

    else:
        form = SignUpForm()
        return render(request,"signup.html",{"form":form})


def userdashboard(request):
    return render(request,"user_dashboard.html")

def guiderdashboard(request):
    return render(request,"guider_dashboard.html")


def cms(request):
    if request.method=="GET":
        form=searchForm()
        return render(request,"current_market_state.html",{"form":form})
    else:
        form=searchForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            print(name)
            # context={}
            # stock=Stock.objects.get(name=name)
            stock=get_object_or_404(Stock,name=name)
            return render(request,"current_market_state.html",{"data":stock,"form":form})


def papertrading(request):
    return render(request,"paper_trading.html")

def webinar_registration(request):
    if request.method=="GET":
        context={}
        context["web"]=Webinar.objects.all()
        if len(context["web"])>0:
            return render(request,"webinar_registration.html",context)
        return render(request,"webinar_registration.html")
    else:
        selected=request.POST.getlist("web")
        for id in selected:
            obj=get_object_or_404(Webinar,id=id)
            obj.number_of_attendee+=1
            obj.save()
        return render(request,"user_dashboard.html",{"message":"Successfully registered for given webinars"})

def marketanalysis(request):
    if request.method=="GET":
        form=searchForm()
        return render(request,"market_analy_pred.html",{"form":form})
    else:
        form=searchForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            try:
                stock=Stock.objects.get(name=name)
            except Stock.DoesNotExist:
                messages.error(request, "Given stock does not exist")
                return render(request, "market_analy_pred.html", {"form": form})
            # if stock is None:
            #     messages.error(request,"Given stock is not exist")
            #     return render(request,"market_analy_pred.html",{"form":form})
        return render(request,"market_analy_pred.html",{"form":form})
            

def sip(request):
    if request.method=="GET":
        form=InvestmentForm()
        return render(request,"sip.html")
    else:
        form=InvestmentForm(request.POST)
        if form.is_valid():
            investment=form.cleaned_data["investment"]
            duration=form.cleaned_data["duration"]
            expected_return=form.cleaned_data["expected_return"]
            
            investment=int(investment)
            duration=int(duration)
            expected_return=int(expected_return)

            duration*=12
            

def consultation(request):
    return render(request,"consultation.html")