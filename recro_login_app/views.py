from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    return render(request, 'recro_login_app/home.html')

def save_profile(backend,details, user, response, *args, **kwargs):
    print(backend)
    print(details)
    print(user)
#     print(response)
#     if backend.name == 'facebook':
#         sign_up = User.objects.get(username=user)
#         sign_up.profile.gender = response.get('gender')
#         sign_up.save()

def social_details(backend, details, response, *args, **kwargs):
    print("social details",response)
    return {'details': dict(backend.get_user_details(response),
                            **details)}