# pylint: disable=line-too-long, too-many-locals, too-many-statements
"""Populates the database with data (categories, images, questions)"""
from api.models import Category, Metacategory, Image, Question, \
    QuestionType, QuestionChoice, Ethnicity, Gender, User, ParticipantInformationType, Experience, Familiar

from api import db

def populate():
    """Method that populates the databse with data"""

    db.session.close()
    db.drop_all()
    db.create_all()

    User.create_user("admin", "admin")

    c_male = Category.create_category(
        name="Jongen", metacategory=Metacategory.gender)
    c_female = Category.create_category(
        name="Meisje", metacategory=Metacategory.gender)
    c_programmer = Category.create_category(
        name="Programmeur", metacategory=Metacategory.profession)
    c_writer = Category.create_category(
        name="Schrijver", metacategory=Metacategory.profession)
    c_alone = Category.create_category(
        name="Alleen", metacategory=Metacategory.social)
    c_together = Category.create_category(
        name="Samen", metacategory=Metacategory.social)
    c_gaming = Category.create_category(
        name="Videospelletjes spelen", metacategory=Metacategory.hobby)
    c_tennis = Category.create_category(
        name="Tennissen", metacategory=Metacategory.hobby)
    c_fruit = Category.create_category(
        name="Fruit", metacategory=Metacategory.demo)
    c_vegetable = Category.create_category(
        name="Groente", metacategory=Metacategory.demo)

    male_images = [
        'https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276420/Gender/gender_male_1_dh1pbq.png',
        'https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276420/Gender/gender_male_2_bsbqc9.png',
        'https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276421/Gender/gender_male_3_eknmuv.png',
        'https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276421/Gender/gender_male_4_d1clch.png']

    female_images = [
        'https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276422/Gender/gender_female_1_nph1ga.png',
        'https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276420/Gender/gender_female_2_fjfxrv.png',
        'https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276420/Gender/gender_female_3_erg7nd.png',
        'https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276420/Gender/gender_female_4_b0vc8l.png'
    ]

    programmer_images = [
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276505/Profession/profession_programmer_1_c6pvby.png",
         "App"),
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276504/Profession/profession_programmer_2_rbcfov.png",
         "Laptop"),
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276504/Profession/profession_programmer_3_cjwqsw.png",
         "Keyboard"),
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276504/Profession/profession_programmer_4_xbviey.png",
         "Website")
    ]

    writer_images = [
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276504/Profession/profession_writer_1_o8xzue.png",
         "Newspaper"),
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276504/Profession/profession_writer_2_mmpdnx.png",
         "Papers"),
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276505/Profession/profession_writer_3_qyl8aq.png",
         "Pen"),
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276505/Profession/profession_writer_4_tbvw0b.png",
         "Book")
    ]

    gaming_images = [
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276493/Hobby/hobby_gaming_1_tlfl07.png",
         "Game Controller"),
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276493/Hobby/hobby_gaming_2_ruribs.png",
         "Game Controller"),
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276493/Hobby/hobby_gaming_3_hvkfme.png",
         "Game Controller"),
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276493/Hobby/hobby_gaming_4_cb1doe.png",
         "Game Controller")
    ]

    tenis_images = [
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276495/Hobby/hobby_tennis_1_ei7yic.png", "Net"),
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276493/Hobby/hobby_tennis_2_qx7tms.png", "Racket"),
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276493/Hobby/hobby_tennis_3_pdsnou.png", "Shoe"),
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276493/Hobby/hobby_tennis_4_v5yam2.png", "Ball")
    ]

    alone_images = [
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276518/Social/social_alone_1_wy8rpb.png", "Alone"),
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276516/Social/social_alone_2_vy3tmr.png", "Alone"),
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276518/Social/social_alone_3_ygnsbz.png", "Alone"),
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276517/Social/social_alone_4_ppasf1.png", "Alone")
    ]

    together_images = [
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276518/Social/social_together_1_eumalw.png",
         "Together"),
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276517/Social/social_together_2_ketyo1.png",
         "Together"),
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276517/Social/social_together_3_s4wzba.png",
         "Together"),
        ("https://res.cloudinary.com/hctr0xmqp/image/upload/v1591276517/Social/social_together_4_ea2yka.png",
         "Together")
    ]

    fruit_images = [
        ("https://www.delunchbus.nl/wp-content/uploads/2017/04/Appel-jg.png?versie=1",
         "Fruit"),
        ("https://www.delunchbus.nl/wp-content/uploads/2017/04/Appel-jg.png?versie=2",
         "Fruit"),
        ("https://www.delunchbus.nl/wp-content/uploads/2017/04/Appel-jg.png?versie=3",
         "Fruit"),
        ("https://www.delunchbus.nl/wp-content/uploads/2017/04/Appel-jg.png?versie=4",
         "Fruit")
    ]

    vegetable_images = [
        ("https://www.weightwatchers.com/nl/sites/nl/files/styles/wwvs_default_image/public/article_masthead/fruit_720x370_0.jpg?versie=1",
         "Vegetable"),
        ("https://www.weightwatchers.com/nl/sites/nl/files/styles/wwvs_default_image/public/article_masthead/fruit_720x370_0.jpg?versie=2",
         "Vegetable"),
        ("https://www.weightwatchers.com/nl/sites/nl/files/styles/wwvs_default_image/public/article_masthead/fruit_720x370_0.jpg?versie=3",
         "Vegetable"),
        ("https://www.weightwatchers.com/nl/sites/nl/files/styles/wwvs_default_image/public/article_masthead/fruit_720x370_0.jpg?versie=4",
         "Vegetable")
    ]

    for link in male_images:
        Image.create_image(link=link, description="Man",
                           attribute='man standing', c_id=c_male.id)

    for link in female_images:
        Image.create_image(link=link, description='Girl',
                           attribute='girl standing', c_id=c_female.id)

    create_images(programmer_images, c_programmer.id)
    create_images(writer_images, c_writer.id)
    create_images(gaming_images, c_gaming.id)
    create_images(tenis_images, c_tennis.id)
    create_images(alone_images, c_alone.id)
    create_images(fruit_images, c_fruit.id)
    create_images(vegetable_images, c_vegetable.id)

    # likert
    ## Demographics 1-5
    create_likert("Ik ben maak makkelijk vrienden en werk graag samen.")
    create_likert("Ik ben gek op computers")
    create_likert("Ik vind het leukst om te")
    create_likert("Als ik dat zou willen, zou ik later programmeur kunnen worden.")
    create_likert("Ik wil later programmeur worden")

    ## 6-10
    create_likert("Wie maakt het makkelijkst vrienden en werkt het liefst samen?")
    create_likert("Wie speelt er het liefste videospelletjes?")
    create_likert("Wie speelt er het liefste tennis?")
    create_likert("Welk beroep vind jij iets voor meisjes?")
    create_likert("Welk beroep vind jij iets voor jongens?")
    
    ## 10-14
    create_likert("Programmeurs maken makkelijk vrienden en werken graag samen.")
    create_likert("Programmeurs zijn gek op computers en hebben weinig andere hobby’s.")
    create_likert("Programmeur zijn, dat is een beroep voor")
    create_likert("Vraag 14")

    #15
    Question.create_question(
        q_type=QuestionType.open_question, text="Wat doet een programmeur?")

    video_female = Image.create_image(link="173d_-zTd1o", description='Role model intervention',
                                      attribute='Female')
    video_male = Image.create_image(link="hEMOMVZbSBE", description='Role model intervention',
                                    attribute='Male')

    # video_question 16
    Question.create_question(
        q_type=QuestionType.video,
        images=[video_female]
    )

    # demographics
    ## 17 18 19
    mc_1 = Question.create_question(q_type=QuestionType.mc_single_answer, text="Hoe oud ben je?",
                                    information=ParticipantInformationType.age)
    for i in range(6, 19):
        QuestionChoice.create_choice(
            choice_num=i - 5, q_id=mc_1.id, text=str(i))
    QuestionChoice.create_choice(choice_num=14, q_id=mc_1.id, text="Anders")

    mc_2 = Question.create_question(q_type=QuestionType.mc_multiple_answer,
                                    text="Waar zijn jouw ouders/verzorgers geboren? Er zijn meerdere antwoorden mogelijk.",
                                    information=ParticipantInformationType.ethnicity)
    for i, ethnicity in enumerate(Ethnicity.__iter__(), 1):
        QuestionChoice.create_choice(
            choice_num=i, q_id=mc_2.id, text=ethnicity.value)

    mc_3 = Question.create_question(q_type=QuestionType.mc_single_answer,
                                    text="Ik voel me een ...",
                                    information=ParticipantInformationType.gender)
    for i, gender in enumerate(Gender.__iter__(), 1):
        QuestionChoice.create_choice(
            choice_num=i, q_id=mc_3.id, text=gender.value)

    # 20
    Question.create_question(q_type=QuestionType.notes, text="Researcher notes",
                             information=ParticipantInformationType.researcher_notes)

    # video_question 21
    Question.create_question(
        q_type=QuestionType.video,
        images=[video_male]
    )

    # experience 
    ## 22 23
    mc_4 = Question.create_question(q_type=QuestionType.mc_single_answer,
                                    text="Heb je wel eens geprogrammeerd? Er zijn meerdere antwoorden mogelijk",
                                    information=ParticipantInformationType.experience)
    for i, experience in enumerate(Experience.__iter__(), 1):
        QuestionChoice.create_choice(
            choice_num=i, q_id=mc_4.id, text=experience.value)

    mc_5 = Question.create_question(q_type=QuestionType.mc_single_answer,
                                    text="Ken jij een programmeur? Er zijn meerdere antwoorden mogelijk",
                                    information=ParticipantInformationType.familiar)
    for i, familiar in enumerate(Familiar.__iter__(), 1):
        QuestionChoice.create_choice(
            choice_num=i, q_id=mc_5.id, text=familiar.value)

def create_images(link_array, c_id):
    """
    Inserts every image in the array with a category

    Parameters
    ----------
    link_array : array
        an array of links.
    c_id : int
        id of a category
    """
    for link in link_array:
        Image.create_image(link=link[0], description='',
                           attribute=link[1], c_id=c_id)


def create_likert(text):
    """
    Inserts a likert question with text

    Parameters
    ----------
    text : string
        text for the question.
    """
    Question.create_question(q_type=QuestionType.likert,
                             text=text)
