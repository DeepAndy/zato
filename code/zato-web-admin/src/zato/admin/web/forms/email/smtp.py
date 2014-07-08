# -*- coding: utf-8 -*-

"""
Copyright (C) 2014 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
from smtplib import SMTP_PORT

# Django
from django import forms

# Zato
from zato.common import EMAIL

class CreateForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'required', 'style':'width:100%'}))
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'checked':'checked'}))

    host = forms.CharField(widget=forms.TextInput(attrs={'class':'required', 'style':'width:100%'}))
    port = forms.CharField(initial=SMTP_PORT, widget=forms.TextInput(attrs={'class':'required', 'style':'width:20%'}))
    timeout = forms.CharField(initial=EMAIL.DEFAULT.TIMEOUT, widget=forms.TextInput(attrs={'class':'required', 'style':'width:20%'}))
    is_debug = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    username = forms.CharField(widget=forms.TextInput(attrs={'style':'width:100%'}))
    mode = forms.ChoiceField(widget=forms.Select())

    def __init__(self, prefix=None, post_data=None):
        super(CreateForm, self).__init__(post_data, prefix=prefix)

        self.fields['mode'].choices[:] = []

        for name, value in EMAIL.SMTP.MODE.iteritems():
            self.fields['mode'].choices.append([value.value, name])

class EditForm(CreateForm):
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    is_debug = forms.BooleanField(required=False, widget=forms.CheckboxInput())
