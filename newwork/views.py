from http.client import HTTPResponse
import profile
from django.shortcuts import redirect, render
from referal.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User


def signup_view(self):
    proile_id=self.session.get('ref_profile')
    print('profile_id',proile_id)
    form=UserCreationForm(self.POST or None)
    if form.is_valid():
        if proile_id is not None:
            
            recommended_by_profile=Profile.objects.get(id=proile_id)
            instance=form.save()
            registered_user=User.objects.get(id=instance.id)
            registered_profile=Profile.objects.get(user=registered_user)
            registered_profile.recomend_by = recommended_by_profile.user
            if self.POST:
                registered_profile.t1=self.POST['role1']
                # print('inside',self.POST['role'])    
            registered_profile.save()
            # i=Profile.objects.get(id=1)
            # r=Profile.objects.filter(recomend_by=i.id)
            # print(r,'inside r')
            # r.update(Role=True)
        else:
            form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')   
        user=authenticate(username=username, password = password )
        login(self,user)
        return redirect('main-view')
    context={'form':form}
    return render(self,'signup.html',context)

def main_view(self,*args,**kwargs):
    c=str(kwargs.get('ref_code'))
    try:
        p=Profile.objects.get(code=c)
        self.session['ref_profile']=p.id
        print('id',p.id)
    except:
        pass
    print(self.session.get_expiry_age())    
    return render(self,'main.html',{})

def popup(self):
    return render(self,'popup.html')

