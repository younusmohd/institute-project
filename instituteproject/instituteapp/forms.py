from django import forms
from multiselectfield import MultiSelectFormField

class FeedBackForm(forms.Form):
    name = forms.CharField(
        label="Enter your Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',


            }

        )
    )
    rating=forms.IntegerField(
        label="Enter your rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your rating'
            }
        )
    )
    feedback=forms.CharField(
        label="Enter your Feedback",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your feedback',
                # 'cols': '15',
                # 'rows': '4',

            }

        )
    )

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }
        )
    )


    email=forms.EmailField(
        label="Enter your Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email'
            }
        )
    )

    mobile=forms.IntegerField(
        label="Enter your Mobile number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Mobile number'
            }
        )
    )
    COURSES_CHOICES=(
         ('py','Python'),
         ('dj','Django'),
         ('ui','UI'),
         ('rest','Rest Api')
     )
    courses=MultiSelectFormField(max_length=200, choices=COURSES_CHOICES)
    SHIFT_CHOICES = (
        ('mrg', 'Morning'),
        ('aftn', 'Afternoon'),
        ('eveng', 'Evening'),
        ('night', 'Night')
    )
    shifts = MultiSelectFormField(max_length=200, choices=SHIFT_CHOICES)


    LOCATIONS_CHOICES=(
        ('hyd','Hyderabad'),
        ('bang','Bangalore'),
        ('che','Chennai'),
        ('pune','Pune')

    )
    locations = MultiSelectFormField(max_length=200, choices=LOCATIONS_CHOICES)

    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    genders = forms.ChoiceField(
        widget=forms.RadioSelect, choices=GENDER_CHOICES
    )

    start_date=forms.DateField(
        widget=forms.SelectDateWidget()
    )



