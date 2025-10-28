from enum import Enum

class PlaceTypeEnum(str, Enum):
    RESTAURANTE = "restaurante"
    PONTO_TURISTICO = "ponto_turistico"
    BAR = "bar"
    FESTA = "festa"
    SHOW = "show"
    MUSEUM = "museum"
    PARK = "park"

    from enum import Enum

class PreferenceType(str, Enum):
    BARES = "bares"
    MUSEUS = "museus"
    PRAIAS = "praias"
    TRILHAS = "trilhas"
