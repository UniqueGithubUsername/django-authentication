from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.
def index(request):
	context = {}
	return render(request, 'main/home.html', context)

def register(request):
	# if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = RegistrationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            output = "Successfully created account."
            context = {'output':output}
            return render(request, 'main/home.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistrationForm()

    return render(request, "registration/register.html", {"form": form})