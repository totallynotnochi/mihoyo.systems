from django import forms


class GenshinUidForm(forms.Form):
    GenshinUID = forms.IntegerField(label="Your Genshin Impact UID:")



