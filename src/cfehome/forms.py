from django import forms


class LandingPageForm(forms.Form):
    # name = forms.CharField(label="Your name")
    # age = forms.IntegerField()
    email = forms.EmailField()


# data = {
#     "name": "",
#     "email": "",
#     "age": "",
#     "nationality": ""
# }

# print(data)
