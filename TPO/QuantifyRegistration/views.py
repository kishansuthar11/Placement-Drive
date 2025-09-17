from django.shortcuts import render
from .forms import CandidateForm

# Form-based View
def register(request):
    if request.method == "POST":
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "QuantifyRegistration/success.html")
    else:
        form = CandidateForm()
    return render(request, "QuantifyRegistration/register.html", {"form": form})

# API View (DRF)
from rest_framework import viewsets
from .models import Candidate
from .serializers import CandidateSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
