from django.utils import timezone
from django.shortcuts import render, redirect
from .models import ReportModel
from .forms import ReportForm


def Report(request):

    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.username = request.user
            obj.save()

            return redirect('/')

    return render(request, 'main/report.html', {'form': form})
