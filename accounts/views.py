# from django.shortcuts import render,redirect
# from django.contrib.auth.forms import Authenticate
# from
# from django.contrib.auth import login
# from django.core.checks import messages
# from django.shortcuts import redirect, render
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login
# from django.contrib import messages
#
#
# def login_view(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.post['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('/')
#         else:
#             messages.info(request,'invalid credentials')
#             return redirect('accounts.login')
#     return render(request, "login.html")
#
#
#
#
# # def login_view(request):
# #     if request.method == 'POST':
# #         form = AuthenticationForm(data=request.POST)
# #         if form.is_valid():
# #             user = form.get_user()
# #             login(request, user)
# #             if 'next' in request.POST:
# #                 return redirect(request.POST.get('next'))
# #             return redirect('main:home')
# #         else:
# #             form = AuthenticationForm()
# #             return render(request, 'accounts/login.html', { 'form' : form })
#




