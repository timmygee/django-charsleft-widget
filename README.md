![Screenshot](https://github.com/timmyomahony/django-charsleft-widget/blob/master/charsleft-screen-small.jpg?raw=true)

A simple django widget that appends a character count to a text input which is determined by the `max_length` of that particular field. This only works on text *inputs* and not *text areas* (as they don't respect `max_length` anyway)

## Installation

The package can be installed via:

    pip install git+https://github.com/timmyomahony/django-charsleft-widget.git


## Usage

For the most common usage, first create a model:

```python
from django.db import models

class Song(models.Model):
  title = models.CharField(max_length=100)
```

then create a custom model form that uses the custom widget class.

```python
from django import forms
from charsleft_widget.widgets import CharsLeftInput

from .models import Song

class SongForm(forms.ModelForm):
  name = forms.CharField(widget=CharsLeftInput())

  class Meta:
    model = Song
    fields = "__all__"
```

If you are using it in the Django admin, import your custom model form in your `ModelAdmin`:


```python
from django.contrib import admin

from .models import Song
from .forms import SongForm


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    form = SongForm
```


You can optionally toggle off the color changing feature by initialising the widget (from the example above) with:

```python
  name = forms.CharField(widget=CharsLeftInput(attrs={'change_color': False}))
```
