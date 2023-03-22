from django.forms import ModelForm
from .models import Team


class TeamUpdateForm(ModelForm):
    class Meta:
        model = Team
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TeamUpdateForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})