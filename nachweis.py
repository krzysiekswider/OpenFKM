def get_aSK(sigV,sigSK,jges):
    """Auslastungsgrad der Vergleichsspannung
    
    sigv    Vergleichsauslastung im Nachweispunkt nach Abschnitt 3.1.1
    sigSK   statische Bauteilfestigkeit, Gl. (3.4.1)
    jges    Gesamtsicherheitsfaktor, Gl. (3.5.5)
    """
    return sigV / sigSK / jges
    
def get_h():
    """Gl. (3.1.10)"""
    return None

def get_aSHZug(sigH,sigSH_Zug,jges):
    return None