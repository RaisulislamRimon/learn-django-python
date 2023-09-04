from django import forms


class LandingPageForm(forms.Form):
    name = forms.CharField(
        label="Write your name",
        required=False,
        # widget=forms.Textarea(attrs={"rows": 4}),
    )
    bio = forms.CharField(
        label=f"Write your bio",
        required=False,
        widget=forms.Textarea(attrs={"class": "forms-control-2", "rows": 3}),
    )
    # age = forms.IntegerField()
    email = forms.EmailField(label="Write your email here")
    email2 = forms.EmailField(label="Confirm email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            default_css_class = "form-control"  # bootstrap class
            new_attrs = {
                "class": default_css_class,
                "id": f"{field}",
                "placeholder": f"Your {field}",
            }
            if field == "email2":
                new_attrs["placeholder"] = "Confirm your email"
            self.fields[field].widget.attrs.update(new_attrs)

    def clean(self):
        data = self.cleaned_data
        email = data.get("email")
        email2 = data.get("email2")
        if email != email2:
            self.add_error("email", "Your email must match!")
        return data

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email.endswith("gmail.com"):
            # self.add_error("email", "You can not use gmail!")
            raise forms.ValidationError("You can not use gmail!")
        return email


# data = {
#     "name": "",
#     "email": "",
#     "age": "",
#     "nationality": ""
# }

# print(data)
