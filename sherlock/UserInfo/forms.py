from django import forms
from auth.models import SherlockUser

from django.forms.fields import DateField
from django.forms.extras.widgets import SelectDateWidget

BIRTH_YEAR_CHOICES = range(1913,2014)

RACE_CHOICES = (
<<<<<<< HEAD
    ('Afghanistan'), ('Albania'), ('Algeria'), ('Andorra'), ('Angola'), ('Antigua and Barbuda'), ('Argentina'), ('Armenia'), ('Australia'), ('Austria'), ('Azerbaijan'), ('The Bahamas'), ('Bahrain'), ('Bangladesh'), ('Barbados'), ('Belarus'), ('Belgium'), ('Belize'), ('Benin'), ('Bhutan'), ('Bolivia'), ('Bosnia and Herzegovina'), ('Botswana'), ('Brazil'), ('Brunei'), ('Bulgaria'), ('Burkina Faso'), ('Burma'), ('Burundi'), ('Cambodia'), ('Cameroon'), ('Canada'), ('Cape Verde'), ('Central African Republic'), ('Chad'), ('Chile'), ('China'), ('Colombia'), ('Comoros'), ('Democratic Republic of the Congo'), ('Republic of the Congo'), ('Costa Rica'), ('Ivory Coast'), ('Croatia'), ('Cuba'), ('Cyprus'), ('Czech Republic'), ('Denmark'), ('Djibouti'), ('Dominica'), ('Dominican Republic'), ('East Timor'), ('Ecuador'), ('Egypt'), ('El Salvador'), ('Equatorial Guinea'), ('Eritrea'), ('Estonia'), ('Ethiopia'), ('Fiji'), ('Finland'), ('France'), ('Gabon'), ('The Gambia'), ('Georgia (country)'), ('Germany'), ('Ghana'), ('Greece'), ('Grenada'), ('Guatemala'), ('Guinea'), ('Guinea-Bissau'), ('Guyana'), ('Haiti'), ('Honduras'), ('Hungary'), ('Iceland'), ('India'), ('Indonesia'), ('Iran'), ('Iraq'), ('Republic of Ireland'), ('Israel'), ('Italy'), ('Jamaica'), ('Japan'), ('Jordan'), ('Kazakhstan'), ('Kenya'), ('Kiribati'), ('North Korea'), ('South Korea'), ('Kuwait'), ('Kyrgyzstan'), ('Laos'), ('Latvia'), ('Lebanon'), ('Lesotho'), ('Liberia'), ('Libya'), ('Liechtenstein'), ('Lithuania'), ('Luxembourg'), ('Republic of Macedonia'), ('Madagascar'), ('Malawi'), ('Malaysia'), ('Maldives'), ('Mali'), ('Malta'), ('Marshall Islands'), ('Mauritania'), ('Mauritius'), ('Mexico'), ('Federated States of Micronesia'), ('Moldova'), ('Monaco'), ('Mongolia'), ('Montenegro'), ('Morocco'), ('Mozambique'), ('Namibia'), ('Nauru'), ('Nepal'), ('Kingdom of the Netherlands'), ('New Zealand'), ('Nicaragua'), ('Niger'), ('Nigeria'), ('Norway'), ('Oman'), ('Pakistan'), ('Palau'), ('State of Palestine'), ('Panama'), ('Papua New Guinea'), ('Paraguay'), ('Peru'), ('Philippines'), ('Poland'), ('Portugal'), ('Qatar'), ('Romania'), ('Russia'), ('Rwanda'), ('Saint Kitts and Nevis'), ('Saint Lucia'), ('Saint Vincent and the Grenadines'), ('Samoa'), ('San Marino'), ('São Tomé and Príncipe'), ('Saudi Arabia'), ('Senegal'), ('Serbia'), ('Seychelles'), ('Sierra Leone'), ('Singapore'), ('Slovakia'), ('Slovenia'), ('Solomon Islands'), ('Somalia'), ('South Africa'), ('South Sudan'), ('Spain'), ('Sri Lanka'), ('Sudan'), ('Suriname'), ('Swaziland'), ('Sweden'), ('Switzerland'), ('Syria'), ('Tajikistan'), ('Tanzania'), ('Thailand'), ('Togo'), ('Tonga'), ('Trinidad and Tobago'), ('Tunisia'), ('Turkey'), ('Turkmenistan'), ('Tuvalu'), ('Uganda'), ('Ukraine'), ('United Arab Emirates'), ('United Kingdom'), ('United States'), ('Uruguay'), ('Uzbekistan'), ('Vanuatu'), ('Vatican City'), ('Venezuela'), ('Vietnam'), ('Yemen'), ('Zambia'), ('Zimbabwe'), ('Abkhazia'), ('Cook Islands'), ('Republic of Kosovo'), ('Nagorno-Karabakh Republic'), ('Niue'), ('Northern Cyprus'), ('Sahrawi Arab Democratic Republic'), ('Somaliland'), ('South Ossetia'), ('Taiwan'), ('Transnistria')
)
=======
    ('Asian'),
    ('White'),
    ('Black'),
    ('Hispanic'))
>>>>>>> 7a83820c0d10ffb8d014e5c889366dbaa1690e51

class SherlockUserForm(forms.Form):
    photo = forms.ImageField()

    #user profile info (main)
    race = forms.ChoiceField(choices=RACE_CHOICES)

    # ethnicity = forms.CharField(max_length=255, required=False)
    # nationality = forms.CharField(max_length=255, required=False)
    date_of_birth = DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    #user profile info (possiblez) some info that might be fun to play around with in the future
    # mood = forms.CharField(max_length=1024, required=False) #not sure how I want to store this one yet. word descriptions? numerical levels? idk
    # occupation = forms.CharField(max_length=1024, required=False) #this one might actually be kind of fun
    # intelligence = forms.CharField(max_length=1024, required=False) #not sure how to measure this either. degree of education?
    # socialclass = forms.CharField(max_length=1024, required=False) #income levels?
    # attractiveness = forms.IntegerField(required=False) #1-10 i guess
