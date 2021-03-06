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

    # User.create_user("admin", "admin")

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
        'https://res.cloudinary.com/hwutobbxz/image/upload/v1596306179/gender/boy-1_xbqkzy.png',
        'https://res.cloudinary.com/hwutobbxz/image/upload/v1596306179/gender/boy-2_smpd2z.png',
        'https://res.cloudinary.com/hwutobbxz/image/upload/v1596306179/gender/boy-3_r4ytga.png',
        'https://res.cloudinary.com/hwutobbxz/image/upload/v1596306179/gender/boy-4_nwlwjy.png'
    ]

    female_images = [
        'https://res.cloudinary.com/hwutobbxz/image/upload/v1596306179/gender/girl-1_kwkmrz.png',
        'https://res.cloudinary.com/hwutobbxz/image/upload/v1596306179/gender/girl-2_rhniuk.png',
        'https://res.cloudinary.com/hwutobbxz/image/upload/v1596306179/gender/girl-3_xe1a9u.png',
        'https://res.cloudinary.com/hwutobbxz/image/upload/v1596306180/gender/girl-4_xkvjjs.png'
    ]

    programmer_images = [
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306549/profession/programmer-1_ulwehs.png",
         "Website"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306550/profession/programmer-2_lof1xf.png",
         "App"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306550/profession/programmer-4_pidzdt.png",
         "Call"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306550/profession/programmer-3_eg4wkm.png",
         "Streaming")
    ]

    writer_images = [
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306550/profession/writer-1_eztpu9.png",
         "Newspaper"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306550/profession/writer-2_rkpv82.png",
         "Papers"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306550/profession/writer-3_irllf9.png",
         "Magazine"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306551/profession/writer-4_o7htgn.png",
         "Book")
    ]

    gaming_images = [
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306334/hobby/game-1_n9io3s.png",
         "Game Controller"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306334/hobby/game-2_aquxcc.png",
         "Game Controller"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306334/hobby/game-3_spykmr.png",
         "Game Controller"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306334/hobby/game-4_pauwrg.png",
         "Game Controller")
    ]

    tennis_images = [
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306334/hobby/tennis-1_smfocf.png", "Net"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306334/hobby/tennis-2_nfparh.png", "Racket"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306334/hobby/tennis-3_ezuh7s.png", "Shoe"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306334/hobby/tennis-4_wxlwze.png", "Ball")
    ]

    alone_images = [
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306654/social/alone-1_hvi8pd.png", "Alone"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306654/social/alone-2_pitedg.png", "Alone"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306654/social/alone-3_ez8euu.png", "Alone"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306654/social/alone-4_adw4ji.png", "Alone")
    ]

    together_images = [
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306655/social/together-1_y4i6i4.png",
         "Together"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306655/social/together-2_edkl5i.png",
         "Together"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306654/social/together-3_dwqijb.png",
         "Together"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306654/social/together-4_ai0lmg.png",
         "Together")
    ]

    fruit_images = [
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596305962/demo/fruit-1_evzbef.png",
         "Fruit"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306043/demo/fruit-2_xfiwal.png",
         "Fruit"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306043/demo/fruit-3_cozz4g.png",
         "Fruit"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306043/demo/fruit-4_sgdvu9.png",
         "Fruit")
    ]

    vegetable_images = [
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306043/demo/vegetable-1_u4jotx.png",
         "Vegetable"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306043/demo/vegetable-2_lwst5m.png",
         "Vegetable"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306043/demo/vegetable-3_h079fa.png",
         "Vegetable"),
        ("https://res.cloudinary.com/hwutobbxz/image/upload/v1596306046/demo/vegetable-4_xm9cyn.png",
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
    create_images(tennis_images, c_tennis.id)
    create_images(alone_images, c_alone.id)
    create_images(together_images, c_together.id)
    create_images(fruit_images, c_fruit.id)
    create_images(vegetable_images, c_vegetable.id)

    # likert
    ## Demographics 1-5
    create_likert("Ik maak makkelijk vrienden en werk graag samen.", 'https://res.cloudinary.com/hwutobbxz/video/upload/v1596200541/audio/1_ywbmuk.m4a')
    create_likert("Ik ben gek op computers", 'https://res.cloudinary.com/hwutobbxz/video/upload/v1596200541/audio/2_qty6fj.m4a')
    create_likert("Ik vind het het leukst om", 'https://res.cloudinary.com/hwutobbxz/video/upload/v1596200542/audio/3_e3qsyz.m4a')
    create_likert("Als ik dat zou willen, zou ik later programmeur kunnen worden.",'https://res.cloudinary.com/hwutobbxz/video/upload/v1596200542/audio/4_yxejoq.m4a')
    create_likert("Ik wil later programmeur worden", 'https://res.cloudinary.com/hwutobbxz/video/upload/v1596200542/audio/5_r7ghrl.m4a')

    ## 6-10
    create_likert("Wie maakt het makkelijkst vrienden en werkt het liefst samen?", 'https://res.cloudinary.com/hwutobbxz/video/upload/v1596200541/audio/6_tbouud.m4a')
    create_likert("Wie speelt er het liefste videospelletjes?", 'https://res.cloudinary.com/hwutobbxz/video/upload/v1596200541/audio/7_wiwrjx.m4a')
    create_likert("Wie speelt er het liefste tennis?", 'https://res.cloudinary.com/hwutobbxz/video/upload/v1596200541/audio/8_l9xs3q.m4a')
    create_likert("Welk beroep vind jij iets voor meisjes?", 'https://res.cloudinary.com/hwutobbxz/video/upload/v1596200541/audio/9_zqwjng.m4a')
    create_likert("Welk beroep vind jij iets voor jongens?", 'https://res.cloudinary.com/hwutobbxz/video/upload/v1596200542/audio/10_qjljyp.m4a')
    
    ## 11-14
    create_likert("Programmeurs maken makkelijk vrienden en werken graag samen.", 'https://res.cloudinary.com/hwutobbxz/video/upload/v1596200542/audio/11_g0dvmj.m4a')
    create_likert("Programmeurs zijn gek op computers en hebben weinig andere hobby’s.", 'https://res.cloudinary.com/hwutobbxz/video/upload/v1596200542/audio/12_nvbyjz.m4a')
    create_likert("Programmeur zijn, dat is een beroep voor", 'https://res.cloudinary.com/hwutobbxz/video/upload/v1596200542/audio/13_x4cjuw.m4a')
    create_likert("Vraag 14", '')

    #15
    Question.create_question(
        q_type=QuestionType.open_question, text="Wat doet een programmeur?", audio='https://res.cloudinary.com/hwutobbxz/video/upload/v1596200543/audio/15_kgj5ql.m4a')

    video_female = Image.create_image(link="B3600xjaz3Y", description='Role model intervention',
                                      attribute='Female')
    video_male = Image.create_image(link="SwISXzPoNUQ", description='Role model intervention',
                                    attribute='Male')

    # video_question 16
    Question.create_question(
        q_type=QuestionType.video,
        images=[video_female]
    )

    # demographics
    ## 17 18 19
    mc_1 = Question.create_question(q_type=QuestionType.mc_single_answer, text="Hoe oud ben je?",
                                    information=ParticipantInformationType.age, 
                                    audio='https://res.cloudinary.com/hwutobbxz/video/upload/v1596200542/audio/17_fcwq8f.m4a')
    for i in range(7, 19):
        QuestionChoice.create_choice(
            choice_num=i - 6, q_id=mc_1.id, text=str(i))
    QuestionChoice.create_choice(choice_num=13, q_id=mc_1.id, text="Anders")

    mc_2 = Question.create_question(q_type=QuestionType.mc_multiple_answer,
                                    text="Waar zijn jouw ouders/verzorgers geboren? Er zijn meerdere antwoorden mogelijk.",
                                    information=ParticipantInformationType.ethnicity,
                                    audio='https://res.cloudinary.com/hwutobbxz/video/upload/v1596200543/audio/18_etdcmb.m4a')
    for i, ethnicity in enumerate(Ethnicity.__iter__(), 1):
        QuestionChoice.create_choice(
            choice_num=i, q_id=mc_2.id, text=ethnicity.value)

    mc_3 = Question.create_question(q_type=QuestionType.mc_single_answer,
                                    text="Ik voel me een ...",
                                    information=ParticipantInformationType.gender,
                                    audio='https://res.cloudinary.com/hwutobbxz/video/upload/v1596200542/audio/19_iiqikw.m4a')
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
    mc_4 = Question.create_question(q_type=QuestionType.mc_multiple_answer,
                                    text="Heb je wel eens geprogrammeerd? Er zijn meerdere antwoorden mogelijk",
                                    information=ParticipantInformationType.experience,
                                    audio='https://res.cloudinary.com/hwutobbxz/video/upload/v1596200543/audio/22_jlrycd.m4a')
    for i, experience in enumerate(Experience.__iter__(), 1):
        QuestionChoice.create_choice(
            choice_num=i, q_id=mc_4.id, text=experience.value)

    mc_5 = Question.create_question(q_type=QuestionType.mc_multiple_answer,
                                    text="Ken jij een programmeur? Er zijn meerdere antwoorden mogelijk",
                                    information=ParticipantInformationType.familiar,
                                    audio='https://res.cloudinary.com/hwutobbxz/video/upload/v1596200543/audio/23_iicnjg.m4a')
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

def create_likert(text, link_audio):
    """
    Inserts a likert question with text and audio

    Parameters
    ----------
    text : string
        text for the question.
    """
    Question.create_question(q_type=QuestionType.likert,
                             text=text, audio=link_audio)
    