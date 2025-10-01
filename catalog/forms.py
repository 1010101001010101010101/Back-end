from django import forms
from .models import ProductAlertRule

class ProductAlertRuleForm(forms.ModelForm):
    class Meta:
        model = ProductAlertRule
        fields = ["product", "alert_rule", "threshold_min", "threshold_max"]

    def clean(self):
        cleaned = super().clean()
        minv = cleaned.get("threshold_min")
        maxv = cleaned.get("threshold_max")

        # Si ambos están vacíos o solo uno está presente, no forzamos relación
        if minv is None or maxv is None:
            return cleaned

        # Validación de consistencia
        if minv >= maxv:
            raise forms.ValidationError(
                "El umbral mínimo debe ser menor que el umbral máximo."
            )
        return cleaned
