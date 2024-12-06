from django.shortcuts import render, redirect
from .forms import PacienteForm
from .models import Paciente


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso recomendado"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade moderada (Classe I)"
    elif 35 <= imc < 40:
        return "Obesidade severa (Classe II)"
    else:
        return "Obesidade morbida (Classe III)"


def calculer_imc(request):
    resultat = None
    classification = None
    if request.method == "POST":
        if "calcular" in request.POST:
            form = PacienteForm(request.POST)
            if form.is_valid():
                patient = form.save(commit=False)
                hauteur_m = patient.altura / 100
                patient.imc = patient.peso / (hauteur_m**2)
                patient.save()

                resultat = f"IMC : {patient.imc:.2f}"
                classification = classificar_imc(patient.imc)
            else:
                resultat = "Données invalides."
        elif "reiniciar" in request.POST:
            form = PacienteForm()
            resultat = None
            classification = None
        elif "sair" in request.POST:
            return redirect("home")
    else:
        form = PacienteForm()

    context = {"form": form, "resultat": resultat, "classification": classification}
    return render(request, "pacientes/calculo_imc.html", context)


def home(request):
    pacientes = Paciente.objects.all()
    context = {"pacientes": pacientes}
    return render(request, "pacientes/home.html", context)
