# Source: Row 2 in ./dataset/CVEfixes/Analysis/results/Python/df_python_cwe_434.xlsx

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.xml', '.nessus', '.json']
    if ext not in valid_extensions:
        raise ValidationError(u'File not supported!')


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
    file = forms.FileField(widget=forms.FileInput(
        attrs={'accept': 'text/xml,application/json'}),
        validators=[validate_file_extension]
    )
