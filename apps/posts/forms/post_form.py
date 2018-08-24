from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=5)
    preview_image = forms.FileField(required=False)
    post_id = forms.CharField(widget=forms.HiddenInput())

    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[post_id].widget = forms.HiddenInput()
    # class Meta:
