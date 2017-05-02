from django import forms


class SessionForm(forms.Form):
    key = forms.CharField(required=True)
    value = forms.CharField(required=True)

    def clean_value(self):
        if self.cleaned_data["key"] == self.cleaned_data["value"]:
            raise forms.ValidationError("key and value cant be same")
        return self.cleaned_data["value"]

    def save(self, request):
        request.session[self.cleaned_data["key"]] = self.cleaned_data["value"]
