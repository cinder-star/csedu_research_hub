from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, ButtonHolder
from crispy_forms.bootstrap import PrependedText, FormActions

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {
                "class": "form-control",
                "name": "title",
            }
        )
        self.fields["file"].widget.attrs.update(
            {
                "class": "form-control",
                "name": "myfile",
            }
        )
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            "title",
            "file",
            FormActions(Submit("upload", "Upload", css_class="btn btn-block btn-lg")),
        )
    def clean(self, *args, **keyargs):
        title = self.cleaned_data.get("title")
        file = self.cleaned_data.get("file")