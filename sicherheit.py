def jm(wahrscheindlichkeit, schadensfolge):
    return{"hoch": {"hoch": 2.0, "mittel": 1.85, "niedrig": 1.75},
     "niedrig": {"hoch": 1.8, "mittel": 1.7, "niedrig": 1.6}}[wahrscheindlichkeit][schadensfolge]

def jp(wahrscheindlichkeit, schadensfolge):
    return{"hoch": {"hoch": 1.5, "mittel": 1.4, "niedrig": 1.3},
     "niedrig": {"hoch": 1.35, "mittel": 1.25, "niedrig": 1.2}}[wahrscheindlichkeit][schadensfolge]

def jmt(wahrscheindlichkeit, schadensfolge):
    return{"hoch": {"hoch": 1.5, "mittel": 1.4, "niedrig": 1.3},
     "niedrig": {"hoch": 1.35, "mittel": 1.25, "niedrig": 1.2}}[wahrscheindlichkeit][schadensfolge]

def jpt(wahrscheindlichkeit, schadensfolge):
    return{"hoch": {"hoch": 1.0, "mittel": 1.0, "niedrig": 1.0},
     "niedrig": {"hoch": 1.0, "mittel": 1.0, "niedrig": 1.0}}[wahrscheindlichkeit][schadensfolge]

def jG(gepruefft: bool=False)->float:
    """Teil-Sicherheitsfaktor für Gussbauteile.
    
    jG = 1.4    nicht zerstörungsfrei geprüfte Gussstücke
    jG = 1.25   zerstörungsfrei geprüfte Gussstücke
    """
    if gepruefft:
        return 1.25
    else:
        return 1.4

def test_jm():
    assert jm("hoch", "hoch") == 2.0
    assert jp("hoch", "mittel") == 1.4