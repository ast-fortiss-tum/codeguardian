# Source: Row 2 in ./dataset/CVEfixes/Analysis/results/Python/df_python_cwe_434.xlsx

class ImportFindingsForm(forms.Form):
    class Meta:
        fields = ['engine', 'min_level', 'file']

    engine = forms.CharField(widget=forms.Select(
        attrs={'class': 'form-control form-control-sm'},
        choices=ENGINE_TYPES))
    min_level = forms.CharField(widget=forms.Select(
        attrs={'class': 'form-control form-control-sm'},
        choices=FINDING_SEVERITIES),
        label='Minimum severity')
    file = forms.FileField()
