from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from accounts.models import User


class HomeView(View):

    def get(self, request):
        return redirect('account_login')

class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'profile.html', {
            'user': User.objects.filter(username=request.user.username)[0]
            })
