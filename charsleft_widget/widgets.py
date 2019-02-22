from django import forms, VERSION
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

try:
    # py2.x
    from django.utils.encoding import force_unicode as force_str
except ImportError:
    # py3.x
    from django.utils.encoding import force_text as force_str
try:
    # Django >=1.7
    from django.forms.utils import flatatt
except ImportError:
    # Django <1.7
    from django.forms.util import flatatt

from charsleft_widget.utils import compatible_staticpath


class CharsLeftInput(forms.TextInput):
    template_name = 'charsleft_widget/input.html'
    type = 'text'

    class Media:
        css={
            "all": ("charsleft-widget/css/charsleft.css", )
        }
        js=(compatible_staticpath("charsleft-widget/js/charsleft.js"), )

    def __init__(self, attrs=None):
        """
        Override init to initialise change_color attribute
        """
        if attrs is None:
            attrs = {}
        # If change_color present in widget attrs use the value, otherwise it's True by default
        attrs.setdefault('change_color', True)
        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['type'] = self.input_type
        maxlength = int(context['widget']['attrs'].get('maxlength', attrs.get('maxlength', 0)))
        context['current_count'] = force_str(maxlength - len(value))
        return context
