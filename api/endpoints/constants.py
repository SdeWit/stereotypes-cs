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


resp = {"questions": [
    {
        "type": 4,
        "title": "Information",
        "header": "Gender profession IAT",
        "body":
            "In the following minutes you will see several images with two words each. One on the right, and the other on the left. Please choose the word you consider aproppriate: Left word (key E), Right word (key I). Please click on Next when ready",
    },
    {
        "type": 1,
        "title": "Binary question",
        "textLeft": "Programmer",
        "textRight": "Writer",
        "image": "https://i.imgur.com/9GIFW9f.jpg",
    },
    {
        "type": 1,
        "title": "Binary question",
        "textLeft": "Male",
        "textRight": "Female",
        "image":
            "https://i.imgur.com/9GIFW9f.jpg",
    },
    {
        "type": 1,
        "title": "Binary question",
        "textLeft": "Programmer & Male",
        "textRight": "Writer & Female",
        "image":
            "https://i.imgur.com/9GIFW9f.jpg",
    },
    {
        "type": 4,
        "title": "Information",
        "header": "Explicit IAT",
        "body":
            "In the following minutes you will be shown several statements. Please indicate how much you agree with the statement",
    },
    {
        "type": 2,
        "title": "Likert Scale",
        "text": "Programming is a profession for men",
        "image": "https://i.imgur.com/9GIFW9f.jpg",
    },
    {
        "type": 2,
        "title": "Likert Scale 2",
        "text": "Writer is a profession for men",
        "image": "https://i.imgur.com/9GIFW9f.jpg",
    },
    {
        "type": 2,
        "title": "Likert Scale 2",
        "text": "Programmers like to work alone",
        "image": "https://i.imgur.com/9GIFW9f.jpg",
    },
    {
        "type": 3,
        "title": "Video",
        "text":
            "You are going to watch a video about stereotypes in Computer Science. Click play when ready.",
        "videoId": "7CVtTOpgSyY",
    },
    {
        "type": 4,
        "title": "Thank you for watching the movie!",
        "header": "In the following minutes you will see questions",
        "body": ""
    },
    {
        "type": 6,
        "title": "Multiple Choice",
        "text": "What is your age",
        "options": ["6", "7", "8", "9", "10"],
    },
    {
        "type": 6,
        "title": "Multiple choice",
        "text": "Gender identity",
        "options": ["Male", "Female", "Other"],
    },
    {
        "type": 5,
        "title": "Ending",
        "text": "Thank you for participating. Morbi elementum libero sem, vel rhoncus justo porta a. Proin ultricies sem urna, in iaculis massa pharetra a. Praesent suscipit arcu neque, et sollicitudin lacus interdum vel. Ut sagittis est non turpis ullamcorper, id laoreet dui scelerisque. Fusce mattis odio augue, vel iaculis odio porta et. Phasellus ullamcorper pellentesque magna, non placerat purus"
    },
]}
