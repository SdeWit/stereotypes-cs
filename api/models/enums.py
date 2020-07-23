# pylint: disable=invalid-name, too-many-arguments, too-few-public-methods, no-member, dangerous-default-value
"""
Module that contains the enums used in the database
"""
import enum


class Experience(enum.Enum):
    """Enumeration of the choices for experience types"""

    School = "Ja, op school"
    Activiteit = "Ja, op een activiteit buiten school bijvoorbeeld in de bibliotheek of bij een codeclub"
    Thuis = "Ja, bij familie, vrienden of thuis"
    Nee = "Nee"

class Familiar(enum.Enum):
    """Enumeration of the choices for familiar types"""

    Ja_bekend = "Ja, iemand die ik vaak zie is programmeur"
    Ja_onbekend = "Ja, maar ik zie deze persoon niet vaak"
    Ja_tv = "Ja, van een film, serie of tv"
    Nee = "Nee"

class Gender(enum.Enum):
    """Enumeration of the choices for gender types"""

    Jongen = "Jongen"
    Meisje = "Meisje"
    Geen = "Geen van beide"
    Niet = "Zeg ik liever niet"


class Ethnicity(enum.Enum):
    """Enumeration of the choices for ethnicity types"""

    Nederlands = "Nederlands"
    Turks = "Turks"
    Marokkaans = "Marokkaans"
    Surinaams = "Surinaams"
    Indonesisch = "Indonesisch"
    Duits = "Duits"
    Pools = "Pools"
    Anders = "Anders"


class Metacategory(enum.Enum):
    """Enumeration of the choices for metacategories"""

    profession = "Profession"
    gender = "Gender"
    hobby = "Hobby"
    social = "Social"
    demo = "Demo"


class QuestionType(enum.Enum):
    """Enumeration of the choices for question types"""

    mc_single_answer = "mc_single_answer"
    mc_multiple_answer = "mc_multiple_answer"
    likert = "likert"
    binary = "binary"
    open_question = "open_question"
    information = "information"
    binary_information = "binary_information"
    finish = "finish"
    video = "video"
    notes = "researcher_notes"

    def __repr__(self):
        """The string representation of the object."""
        return str(self.value)


class ParticipantInformationType(enum.Enum):
    """
    Enum of questions that relate directly to a participant
    """
    age = "Age"
    gender = "Gender"
    ethnicity = "Ethnicity"
    researcher_notes = "Researcher notes"
    experience = "Programming experiences"
    familiar = "Familiar programmer"


class Version(enum.Enum):
    """Enumeration of the different scenarios"""

    A = "control-social-female"
    B = "control-social-male"
    C = "control-hobby-female"
    D = "control-hobby-male"
    E = "intervention-social-female"
    F = "intervention-social-male"
    G = "intervention-hobby-female"
    H = "intervention-hobby-male"
    I = "control-social-female-counter"
    J = "control-social-male-counter"
    K = "control-hobby-female-counter"
    L = "control-hobby-male-counter"
    M = "intervention-social-female-counter"
    N = "intervention-social-male-counter"
    O = "intervention-hobby-female-counter"
    P = "intervention-hobby-male-counter"
