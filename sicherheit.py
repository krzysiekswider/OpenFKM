# Lastfaktor

jS = 1.0

# Materialfaktor: Grund-Sicherheitsfaktoren

def get_jm(wahrscheindlichkeit, schadensfolge):
    return{"hoch": {"hoch": 2.0, "mittel": 1.85, "niedrig": 1.75},
     "niedrig": {"hoch": 1.8, "mittel": 1.7, "niedrig": 1.6}}[wahrscheindlichkeit][schadensfolge]

def get_jp(wahrscheindlichkeit, schadensfolge):
    return{"hoch": {"hoch": 1.5, "mittel": 1.4, "niedrig": 1.3},
     "niedrig": {"hoch": 1.35, "mittel": 1.25, "niedrig": 1.2}}[wahrscheindlichkeit][schadensfolge]

def get_jmt(wahrscheindlichkeit, schadensfolge):
    return{"hoch": {"hoch": 1.5, "mittel": 1.4, "niedrig": 1.3},
     "niedrig": {"hoch": 1.35, "mittel": 1.25, "niedrig": 1.2}}[wahrscheindlichkeit][schadensfolge]

def get_jpt(wahrscheindlichkeit, schadensfolge):
    return{"hoch": {"hoch": 1.0, "mittel": 1.0, "niedrig": 1.0},
     "niedrig": {"hoch": 1.0, "mittel": 1.0, "niedrig": 1.0}}[wahrscheindlichkeit][schadensfolge]

# Materialfaktor: Teil-Sicherheitsfaktoren

# für Gussbauteile
def get_jG(gepruefft: bool=False)->float:
    """Teil-Sicherheitsfaktor für Gussbauteile.
    
    jG = 1.4    nicht zerstörungsfrei geprüfte Gussstücke
    jG = 1.25   zerstörungsfrei geprüfte Gussstücke
    """
    if gepruefft:
        return 1.25
    else:
        return 1.4

# TODO: für geschweißte Bauteile

# TODO: für nichtduktile Gussbauteile

# Gesamt-Sicherheitsfaktor
def get_jges(jm,jp,Rp,Rm,jz,jS=1.0,jmt=None,jpt=None,KTm=1,KTp=1,KTtm=1,KTtp=1,deltaj=0,
        normal_temperatur=True,
        walzstahl_und_duktile_alu_in_geschw=False):
    """Gesamt-Sicherheitsfaktor"""
    if normal_temperatur:
        safety_factors = [jm*Rp/Rm, jp]
    elif Rp/Rm <=0.75:
        safety_factors = [jp/KTp, jpt/KTtp]
    elif Rp/Rm > 0.75:
        safety_factors = [jm/KTm*Rp/Rm, jmt,KTtm*Rp/Rm]
    elif walzstahl_und_duktile_alu_in_geschw:
        safety_factors = [jp/KTp, jpt/KTtp]
    else:
        safety_factors = [jm/KTm*Rp/Rm, jp/KTp, jmt,KTtm*Rp/Rm, jpt/KTtp]
    return jS * (jz*max(safety_factors)+deltaj)


def test_jm():
    assert jm("hoch", "hoch") == 2.0
    assert jp("hoch", "mittel") == 1.4
    