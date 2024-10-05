from flask import Flask, render_template, request
import plotly as pl

app = Flask(__name__, template_folder='templates')

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        country = request.form[
            'country'
        ]
        if (checkCountry(country)):
            return f'Country selected : {country}'
        else:
            return f'Invalid country selection: {country}'
    return render_template('index.html')

def checkCountry(country):

    countries = [
        # Europe - Scandinavia
        [
            "Denmark", "Finland", "Iceland", "Norway", "Sweden"
        ],

        # Europe - West Europe
        [
            "Austria", "Belgium", "France", "Germany", "Ireland", "Liechtenstein",
            "Luxembourg", "Monaco", "Netherlands", "Switzerland", "United Kingdom"
        ],

        # Europe - Central Europe
        [
            "Czech Republic", "Hungary", "Poland", "Slovakia"
        ],

        # Europe - Eastern Europe
        [
            "Belarus", "Moldova", "Russia", "Ukraine"
        ],

        # Europe - Balkans
        [
            "Albania", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Greece", "Kosovo",
            "Montenegro", "North Macedonia", "Romania", "Serbia", "Slovenia"
        ],

        # Europe - Baltics
        [
            "Estonia", "Latvia", "Lithuania"
        ],

        # Europe - Southern Europe
        [
            "Andorra", "Italy", "Malta", "Portugal", "San Marino", "Spain", "Vatican City"
        ],

        # North America - Caribbean
        [
            "Antigua and Barbuda", "Bahamas", "Barbados", "Cuba", "Dominica",
            "Dominican Republic", "Grenada", "Haiti", "Jamaica", "Saint Kitts and Nevis",
            "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago"
        ],

        # North America - Central America
        [
            "Belize", "Costa Rica", "El Salvador", "Guatemala", "Honduras",
            "Mexico", "Nicaragua", "Panama"
        ],

        # North America - Northern America
        [
            "Canada", "United States of America"
        ],

        # South America
        [
            "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador",
            "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"
        ],

        # Oceania - Australia and New Zealand
        [
            "Australia", "New Zealand"
        ],

        # Oceania - Pacific Islands
        [
            "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru",
            "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga",
            "Tuvalu", "Vanuatu"
        ],
        # Africa - North Africa
        [
            "Algeria", "Egypt", "Libya", "Morocco", "Sudan", "Tunisia", "Mauritania"
        ],

        # Africa - West Africa
        [
            "Benin", "Burkina Faso", "Cape Verde", "Cote d'Ivoire (Ivory Coast)", "Gambia",
            "Ghana", "Guinea", "Guinea-Bissau", "Liberia", "Mali", "Niger",
            "Nigeria", "Senegal", "Sierra Leone", "Togo"
        ],

        # Africa - Central Africa
        [
            "Angola", "Cameroon", "Central African Republic", "Chad", "Congo (Congo-Brazzaville)",
            "Democratic Republic of the Congo", "Equatorial Guinea", "Gabon", "Sao Tome and Principe"
        ],

        # Africa - East Africa
        [
            "Burundi", "Comoros", "Djibouti", "Eritrea", "Ethiopia", "Kenya", "Madagascar",
            "Malawi", "Mauritius", "Mozambique", "Rwanda", "Seychelles", "Somalia",
            "South Sudan", "Tanzania", "Uganda", "Zambia", "Zimbabwe"
        ],

        # Africa - Southern Africa
        [
            "Botswana", "Eswatini", "Lesotho", "Namibia", "South Africa"
        ],

        # Asia - East Asia
        [
            "China", "Japan", "Mongolia", "North Korea", "South Korea", "Taiwan"
        ],

        # Asia - Southeast Asia
        [
            "Brunei", "Cambodia", "East Timor (Timor-Leste)", "Indonesia", "Laos", "Malaysia",
            "Myanmar (formerly Burma)", "Philippines", "Singapore", "Thailand", "Vietnam"
        ],

        # Asia - South Asia
        [
            "Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives", "Nepal", "Pakistan", "Sri Lanka"
        ],

        # Asia - Central Asia
        [
            "Kazakhstan", "Kyrgyzstan", "Tajikistan", "Turkmenistan", "Uzbekistan"
        ],

        # Asia - Western Asia (Middle East)
        [
            "Armenia", "Azerbaijan", "Bahrain", "Cyprus", "Georgia", "Iran", "Iraq",
            "Israel", "Jordan", "Kuwait", "Lebanon", "Oman", "Qatar", "Saudi Arabia",
            "Syria", "Turkey", "United Arab Emirates", "Yemen"
        ]
    ]

    found = False
    for sublist in countries:
        if country.upper() not in (listc.upper() for listc in sublist):
            continue
        else:
            found = True
            break

    return found


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')