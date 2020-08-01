# pylint: disable=line-too-long
"""
This module defines commonly-used constants
"""
# Define error messages
ANSWERS = {200: "200 OK",
           201: "201 Created",
           204: "204 No Content",
           400: "400 Bad Request",
           401: "401 Unauthorized",
           403: "403 Forbidden",
           404: "404 Not found",
           500: "500 An internal server error occurred",
           501: "501 Not implemented",
           502: "502 Bad gateway"
           }

COLUMNS_RESULTS = ["Participant Name", "Question ID", "Question Type", "Question Text",
                   "Participant Answers", "Image", "Response Time", "Before Video"]

BLOCK_START_TEXT = [

    {"text0": "Je gaat zo verschillende plaatjes zien die je naar links of naar rechts moet verplaatsen. Doe dit zo "
              "snel mogelijk en probeer zo min mogelijk fouten te maken. Mocht je toch een foutje maken, geen "
              "probleem! Je mag het dan nog een keer proberen.",

     "text1": "Hieronder zie je plaatjes van een {}. Deze ga je zo naar links verplaatsen. Dit doe je door op "
              "de ‘e’ te tikken op het toetsenbord.",

     "text2": "Ook ga je plaatjes zien van een {}. Deze ga je zo naar rechts verplaatsen. Dit doe je door op "
              "de ‘i’ te tikken op het toetsenbord."
     },

    {"text0": "Goed gedaan! We gaan het nog een keer doen, maar nu met nieuwe plaatjes.",

     "text1": "Hieronder zie je plaatjes van een {}. Deze ga je zo naar links verplaatsen. Dit doe je door op "
              "de ‘e’ te tikken op het toetsenbord.",

     "text2": "Ook ga je plaatjes zien van een {}. Deze ga je zo naar rechts verplaatsen. Dit doe je door op "
              "de ‘i’ te tikken op het toetsenbord."
     },

    {"text0": "Nu gaan we plaatjes combineren.",

     "text1": "Wanneer je een plaatje ziet van een {} of {} verplaats je deze naar links door op de ‘e’ "
              "te tikken op het toetsenbord. Dat zijn dus deze plaatjes.",

     "text2": "Wanneer je een plaatje ziet van een {} of {} verplaats je deze naar rechts door op de "
              "‘i’ te tikken op het toetsenbord. Dat zijn dus deze plaatjes."
     },

    {"text0": "Goed gedaan! We gaan het nog een keer doen, maar draaien nu links en rechts om.",

     "text1": "Hieronder zie je plaatjes van een {}. Deze ga je zo naar links verplaatsen. Dit doe je door op de "
              "‘e’ te tikken op het toetsenbord.",

     "text2": "Ook ga je plaatjes zien van een {}. Deze ga je zo naar rechts verplaatsen. Dit doe je door op de "
              "‘i’ te tikken op het toetsenbord."
     },

    {"text0": "Nog een set met plaatjes te gaan! Je doet het heel goed.",

     "text1": "Wanneer je een plaatje ziet van een {} of {} verplaats je deze naar links door op de ‘e’ "
              "te tikken op het toetsenbord. Dat zijn dus deze plaatjes.",

     "text2": "Wanneer je een plaatje ziet van een {} of {} verplaats je deze naar rechts door op de "
              "‘i’ te tikken op het toetsenbord. Dat zijn dus deze plaatjes."
     },
]

# audio file begins with left category
BLOCK_START_AUDIO = [
    {"programmeur_schrijver" : "https://res.cloudinary.com/hwutobbxz/video/upload/v1596284785/audio/IAT-1-profession-programmer-writer_tcnceo.m4a"
    },

    {
    "programmeur_schrijver" : "",    
    "jongen_meisje": "https://res.cloudinary.com/hwutobbxz/video/upload/v1596284785/audio/IAT-2-gender-jongen-meisje_gr2drx.m4a",
    "meisje_jongen": "https://res.cloudinary.com/hwutobbxz/video/upload/v1596284785/audio/IAT-2-gender-meisje-jongen_nj70nx.m4a",

    "videospelletjes spelen_tennissen":"https://res.cloudinary.com/hwutobbxz/video/upload/v1596286605/audio/IAT-2-hobby-spel-tennis_prhzzg.m4a",
    "tennissen_videospelletjes spelen":"https://res.cloudinary.com/hwutobbxz/video/upload/v1596286834/audio/IAT-2-tennis-spel_qvpxuy.m4a",

    "alleen_samen": "https://res.cloudinary.com/hwutobbxz/video/upload/v1596286603/audio/IAT-2-social-alleen-samen_ukbvnd.m4a",
    "samen_alleen": "https://res.cloudinary.com/hwutobbxz/video/upload/v1596286604/audio/IAT-2-social-samen-alleen_1_ydkqxf.m4a"
    },

    {
    "programmeur_schrijver" : "",   
    "jongen_meisje": "https://res.cloudinary.com/hwutobbxz/video/upload/v1596286604/audio/IAT-3-gender-jongen-meisje_1_qmh5z6.m4a",
    "meisje_jongen": "https://res.cloudinary.com/hwutobbxz/video/upload/v1596286605/audio/IAT-3-gender-meisje-jongen_s86hzl.m4a",

    "videospelletjes spelen_tennissen":"https://res.cloudinary.com/hwutobbxz/video/upload/v1596286605/audio/IAT-3-hobby-spel-tennis_mga5dh.m4a",
    "tennissen_videospelletjes spelen":"https://res.cloudinary.com/hwutobbxz/video/upload/v1596286604/audio/IAT-3-hobby-tennis-spel_xfzsbz.m4a",

    "alleen_samen": "https://res.cloudinary.com/hwutobbxz/video/upload/v1596286604/audio/IAT-3-social-alleen-samen_wlp5ja.m4a",
    "samen_alleen": "https://res.cloudinary.com/hwutobbxz/video/upload/v1596286604/audio/IAT-3-social-samen-alleen_imcskt.m4a"
    },

    {
    "programmeur_schrijver" : "",   
    "jongen_meisje": "https://res.cloudinary.com/hwutobbxz/video/upload/v1596286605/audio/IAT-4-gender-jongen-meisje_b5xejt.m4a",
    "meisje_jongen": "https://res.cloudinary.com/hwutobbxz/video/upload/v1596286605/audio/IAT-4-gender-meisje-jongen_1_m45pzu.m4a",

    "videospelletjes spelen_tennissen":"https://res.cloudinary.com/hwutobbxz/video/upload/v1596286606/audio/IAT-4-hobby-spel-tennis_v7gs5a.m4a",
    "tennissen_videospelletjes spelen":"https://res.cloudinary.com/hwutobbxz/video/upload/v1596286607/audio/IAT-4-hobby-tennis-spel_oemkfc.m4a",

    "alleen_samen": "https://res.cloudinary.com/hwutobbxz/video/upload/v1596286606/audio/IAT-4-social-alleen-samen_ifahca.m4a",
    "samen_alleen": "https://res.cloudinary.com/hwutobbxz/video/upload/v1596286607/audio/IAT-4-social-samen-alleen_uplozf.m4a"
    },

    {
    "programmeur_schrijver" : "",   
    "jongen_meisje": "https://res.cloudinary.com/hwutobbxz/video/upload/v1596286607/audio/IAT-5-gender-jongen-meisje_dzcggb.m4a",
    "meisje_jongen": "https://res.cloudinary.com/hwutobbxz/video/upload/v1596287115/audio/IAT-5-gender-meisje-jongen_qbzxyd.m4a",

    "videospelletjes spelen_tennissen":"https://res.cloudinary.com/hwutobbxz/video/upload/v1596286607/audio/IAT-5-hobby-spel-tennis_hmgaan.m4a",
    "tennissen_videospelletjes spelen":"https://res.cloudinary.com/hwutobbxz/video/upload/v1596286607/audio/IAT-5-hobby-tennis-spel_eheia4.m4a",

    "alleen_samen": "https://res.cloudinary.com/hwutobbxz/video/upload/v1596286606/audio/IAT-5-social-alleen-samen_qjmonj.m4a",
    "samen_alleen": "https://res.cloudinary.com/hwutobbxz/video/upload/v1596286606/audio/IAT-5-social-samen-alleen_y6gekz.m4a"
    },
]

BLOCK_END_TEXT = "Tip: Zet je linker wijsvinger op de ‘e’, en je rechter wijsvinger op de ‘i’, zo kun je " \
                 "snel plaatjes verplaatsen! Ben je er klaar voor? Druk dan op volgende."

FINAL_BLOCK_TEXT = {

    "text": "Super goed gedaan! We willen je graag ook wat vragen stellen. "
            "Er zijn geen goede of foute antwoorden op deze vragen!"
}

COLLECTION_QUIZ_BEGINNING_TEXT = "Leuk dat je mee doet aan dit onderzoek! Vind je het fijn als de tekst wordt voorgelezen? Klik dan onderaan op de knop 'Voorlezen'. " \
                      "Als je iets niet begrijpt tijdens het onderzoek, of als je wilt " \
                      "stoppen, steek dan je hand op. We komen dan zo snel mogelijk naar je toe om je te helpen. "

COLLECTION_QUIZ_BEGINNING_AUDIO = "https://res.cloudinary.com/hwutobbxz/video/upload/v1596206106/audio/collection-intro_sjdsq8.m4a"

COLLECTION_QUIZ_END_TEXT = "Bedankt voor het meedoen aan dit onderzoek! We willen je vragen om niet te verklappen" \
                "wat je precies gedaan hebt aan andere kinderen die misschien nog mee willen doen.\n" \
                "Steek je hand op, dan komt er zo snel mogelijk iemand naar je toe."

INTERVENTION_VIDEO_TEXT = "Wat goed gedaan! Je hebt alle vragen gehad. " \
                          "Je mag nog een korte video kijken waarin we je vertellen wat een programmeur eigenlijk is."

INTERVENTION_VIDEO_AUDIO = "https://res.cloudinary.com/hwutobbxz/video/upload/v1596203599/audio/control-video_ofvne3.m4a"

CONTROL_VIDEO_TEXT = "Allereerst ga je naar een video kijken waarin we je uitleg geven over het beroep ‘programmeur’."

CONTROL_VIDEO_AUDIO = "https://res.cloudinary.com/hwutobbxz/video/upload/v1596203599/audio/intervention-video_otawa1.m4a"

DISSEMINATION_RESULT_MALE = "Volgens deze test associeert u programmeren met mannen."

DISSEMINATION_RESULT_FEMALE = "Volgens deze test associeert u programmeren met vrouwen."

DISSEMINATION_NO_ASSOCIATION = "Volgens deze test heeft u geen associatie tussen programmeren met gender."

DISSEMINATION_QUIZ_END_TEXT = "Bedankt voor het afleggen van de test. Druk op de knop om uw resultaten te zien."
