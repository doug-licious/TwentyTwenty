from django import forms


class FilterForm(forms.Form):
    filter_text = forms.CharField(label='Filter', max_length=50, required=False)
    rows = forms.IntegerField(label='Graph Rows', initial=50)
    flatten_versions = forms.BooleanField(label='Flatten versions', initial=True, required=False)
