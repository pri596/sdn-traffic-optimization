from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout as auth_logout
import numpy as np
import joblib
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm
from .models import NetworkData
from .forms import NetworkDataForm



def home(request):
    return render(request, 'users/home.html')

@login_required(login_url='users-register')


def index(request):
    return render(request, 'app/index.html')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality

class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import joblib
from .utils.network_collector import get_latest_network_data, ip_to_int
from .sdn_simulator import SDNController
from .qos_policy import map_intent_to_qos

# Load your trained ML model
Model = joblib.load('users/network_model.pkl')
sdn = SDNController()

# Mapping ML class to intent
ml_to_intent = {
    "ATTACK": "REAL_TIME",
    "DNS": "BULK",
    "DOWNLOAD": "BULK",
    "FTP": "BULK",
    "GAMING": "REAL_TIME",
    "VIDEO": "REAL_TIME",
    "VOIP": "REAL_TIME",
    "WEB": "BACKGROUND"
}

@csrf_exempt
def real_time_ingest(request):
    """
    Called by frontend every 2 seconds.
    Returns real-time network data + ML prediction + QoS + SDN simulation.
    """
    if request.method == "GET":
        try:
            data = get_latest_network_data()

            # Convert IPs to int for ML
            src_ip_int = ip_to_int(data['src_ip'])
            dst_ip_int = ip_to_int(data['dst_ip'])
            features = np.array([[src_ip_int, dst_ip_int, data['protocol'],
                                  data['duration_ms'], data['packet_count'], data['bytes']]])

            # 1️⃣ ML Prediction
            prediction_index = Model.predict(features)[0]
            classes = ["ATTACK", "DNS", "DOWNLOAD", "FTP",
                       "GAMING", "VIDEO", "VOIP", "WEB"]
            ml_class = classes[prediction_index]
            data['prediction'] = ml_class

            # 2️⃣ Map ML class to intent
            intent = ml_to_intent.get(ml_class, "BACKGROUND")
            data['intent'] = intent

            # 3️⃣ Map intent to QoS
            qos = map_intent_to_qos(intent)
            data['priority'] = qos['priority']
            data['queue'] = qos['queue']

            # 4️⃣ Apply simulated SDN policy
            sdn_result = sdn.apply_policy({
                "src_ip": data["src_ip"],
                "dst_ip": data["dst_ip"],
                "intent": intent,
                "priority": qos['priority'],
                "queue": qos['queue']
            })
            data['sdn_status'] = sdn_result['status']
            data['path'] = sdn_result['path']

            print(f"[REAL-TIME] {data}")

            # 5️⃣ Return JSON to frontend
            return JsonResponse({"status": "success", "data": data})

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    return JsonResponse({"status": "error", "message": "GET only"}, status=405)


def live_dashboard(request):
    """
    Renders the dashboard HTML page.
    """
    return render(request, "app/real_time.html")



def Air_db(request):
    data = NetworkData.objects.all()
    return render(request, 'app/Air_db.html', {'data': data})




def logout_view(request):  
    auth_logout(request)
    return redirect('/')
from .sdn_simulator import SDNController
from .qos_policy import map_intent_to_qos

sdn = SDNController()

# After ML classification:
intent = "REAL_TIME"  # Example
qos = map_intent_to_qos(intent)
qos_data = {
    "src_ip": "192.168.1.10",
    "dst_ip": "8.8.8.8",
    "intent": intent,
    "priority": qos["priority"],
    "queue": qos["queue"]
}
result = sdn.apply_policy(qos_data)
qos_data["sdn_status"] = result["status"]
qos_data["path"] = result["path"]
