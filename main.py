from stress_functions import *
from sicherheit import *
from nachweis import *

# Material
Rp=240
Rm=400

# Bauteilfestigkeit

# Spannungen


# Sicherheiten
wahrscheinlichkeit = "hoch"
schadensfolgen = "mittel"
gepruefft = False
jm = get_jm(wahrscheinlichkeit, schadensfolgen)
jp = get_jp(wahrscheinlichkeit, schadensfolgen)
jG = get_jG(gepruefft)
jges = get_jges(jm,jp,Rp,Rm,jG)
print(round(jges,2))

# Nachweis
asK = get_aSK(jges)