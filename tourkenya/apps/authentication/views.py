from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
# Create your views here.

from .models import UserAuthentication
from .form import SignUpForm

def signup_view(request):
    print(request.POST)
    form = SignUpForm(request.POST or None)
    import pdb; pdb.set_trace()
    if form.is_valid():
        print(form.cleaned_data['firstName'])
        form = UserAuthentication.objects.create(**form.cleaned_data)

        form = SignUpForm()

    context = {"form": form}
    template_name = "signup.html"
    return render(request, template_name, context)
    # if request.method == 'POST':
    #     # response = HttpResponse()
    #     # check if user email exists
    #     exists = UserAuthentication.objects.all().filter(email=request.POST.get('email'))
    #     if exists:
    #         return HttpResponse("Sorry the user email exists")
    #     else:
    #         # import pdb; pdb.set_trace()
    #         # import pdb; pdb.set_trace()
    #         data = request.POST
    #         user = {
    #             'firstName': data['firstName'],
    #             'lastName': data['lastName'],
    #             'email': data['email'],
    #             'password': data['password']
    #         }
    #         import pdb; pdb.set_trace()
    #         new_user = UserAuthentication()
    #         new_user.save(**data)
    #         return HttpResponse("You have successfully Registered. Proceed to login")

    # #     # fName =  request.POST.get('firstName')
    # #     # lName =  request.POST.get('lastName')
    # #     # eMail =  request.POST.get('email') 
    # #     # pAssword = request.POST.get('password')

    # #     # return data
        

    # #     #  perfom password validation

    # #     print(fName,lName, eMail, pAssword)

    # # # context = {"form": form}
    # template_name = "signup.html"
    # return render(request, template_name)
