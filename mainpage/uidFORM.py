from django import forms


class GenshinUidForm(forms.Form):
    GenshinUID = forms.IntegerField(label="Your Genshin Impact UID:")

class GenshinPercentageForm(forms.Form):
    skillScale = forms.IntegerField(label="Your Rudimentary Skill Scalings (in percentage):")


