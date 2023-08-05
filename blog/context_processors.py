from users.models import Profile


def access_profile(request):
    if request.user.is_authenticated:
        try:
            access_profiles = Profile.objects.get(name =request.user)
            return {"access_profile":access_profiles }
        
        except:    
            access_profiles = ""
            return {"access_profile":access_profiles }
               
    else:
        return {}