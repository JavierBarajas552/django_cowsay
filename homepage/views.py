from django.shortcuts import render
from homepage.models import CowModel
from homepage.forms import CowForm
import subprocess
# Create your views here.


def index(request):
    cow = False
    if request.method == 'POST':
        subform = CowForm(request.POST)
        if subform.is_valid():
            data = subform.cleaned_data
            CowModel.objects.create(
                text=data.get('text')
            )
            cow = subprocess.run(
                ['cowsay', data.get('text')], capture_output=True).stdout.decode('utf-8')
    form = CowForm()
    return render(request, 'index.html', {'cow': cow, 'form': form})


def last_ten(request):
    ten_posts = CowModel.objects.all().order_by('id').reverse()[:10]
    return render(request, 'last_ten.html', {'last': ten_posts})
