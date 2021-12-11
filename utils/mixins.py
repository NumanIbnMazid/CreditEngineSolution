from django import forms
# Crispy Form Imports
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Submit, Column, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


"""
----------------------- * Form Mixins * -----------------------
"""


class CustomSimpleForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CustomSimpleForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-xl-1 col-lg-1 col-md-2 col-sm-4 col-xs-6 col-6 fw-bold'
        self.helper.field_class = 'col-xl-11 col-lg-11 col-md-10 col-sm-8 col-xs-6 col-6'
        # self.helper.form_tag = False
        
        layout = self.helper.layout = Layout()
        for field_name, field in self.fields.items():
            layout.append(
                Div(
                    Field(field_name, placeholder=field.widget.attrs.get(
                        "placeholder", f"Enter {field.label}...")),
                    Div(
                        HTML("""
                            <div class='text-center mb-1'>
                                <div class="help-block with-errors"></div>
                            </div>
                        """)
                    )
                )
            )

        layout.append(
            ButtonHolder(
                Div(
                    Submit('submit', 'Submit',
                           css_class='btn btn-md btn-primary m-1'),
                    Button(
                        'button', 'Cancel', css_class='btn btn-md btn-danger m-1', data_dismiss="modal"),
                    css_class="text-center"
                )
            )
        )


class CustomModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomModelForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-xl-2 col-lg-2 col-md-2 col-sm-4 col-xs-6 col-6 fw-bold'
        self.helper.field_class = 'col-xl-10 col-lg-10 col-md-10 col-sm-8 col-xs-6 col-6'
        # self.helper.form_tag = False

        layout = self.helper.layout = Layout()
        for field_name, field in self.fields.items():
            layout.append(
                Div(
                    Field(field_name, placeholder=field.widget.attrs.get(
                        "placeholder", f"Enter {field.label}...")),
                    Div(
                        HTML("""
                            <div class='text-center mb-1'>
                                <div class="help-block with-errors"></div>
                            </div>
                        """)
                    )
                )
            )

        layout.append(
            ButtonHolder(
                Div(
                    Submit('submit', 'Submit',
                           css_class='btn btn-md btn-primary m-1'),
                    Button(
                        'button', 'Cancel', css_class='btn btn-md btn-danger m-1', data_dismiss="modal"),
                    css_class="text-center"
                )
            )
        )

        # self.helper.form_show_labels = False
