from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import UserProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def user_profile(request):
	if request.method == "POST":
		form = UserProfileForm(request.POST, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/loggedin/')
	else:
		profile = request.user.profile # create profile if needed (property in model)
		form = UserProfileForm(instance=profile)
	args = {'form': form}
	args.update(csrf(request))
	return render_to_response('profile.html', args)
