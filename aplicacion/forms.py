from django import forms


class CursoForm(forms.Form):
    nombre= forms.CharField(max_length=50, required=True)
    comision= forms.IntegerField(required=True)
    email= forms.EmailField(label="Email", required=False)
    TURNOS = (
        (1, "Mañana"),
        (1, "Tarde"),
        (1, "Noche"),
        )
    turno = forms.ChoiceField(label="Turno elegido", choices=TURNOS, required=True)
    becado = forms.BooleanField()