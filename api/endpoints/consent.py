# pylint: disable=no-self-use
"""
Module that deals with all logic related to consent forms
"""
from flask import request, current_app
from flask_restful import Resource
from cloudinary.uploader import upload

import api.endpoints.validation as valid
from api.models import Consent, Participant
from api.models.helpers import add_to_db
from api.endpoints.constants import ANSWERS
from api.endpoints.sockets import red
from api import socketio


class ConsentForm(Resource):
    """Resource that deals with consent form logic"""

    def post(self):
        """
        On a post request on the /form endpoint we add the consent form to the database
        :return: If the request is valid, a 200 status code, otherwise a 400 code
        """

        validators = {
            'parent': valid.validate_person_data,
            'children': valid.validate_children_data,
            'signature': valid.validate_signature,
            'email': valid.validate_email
        }

        data = valid.validate(valid.read_form_data(request), validators)
        if not data:
            return ANSWERS[400], 400

        parent = data['parent']
        signature = data['signature']

        if not current_app.config['TESTING']:
            upload_result = upload(signature, folder="signatures")
            signature = upload_result["secure_url"]

        cons = Consent.create_consent(parent_first_name=parent['firstName'],
                                      parent_last_name=parent['lastName'],
                                      signature=signature, email=data['email'])

        for child in data['children']:
            participant = Participant(first_name=child['firstName'],
                                      last_name=child['lastName'],
                                      consent_id=cons.id)
            add_to_db(participant)
            obj = {"firstName": participant.first_name,
                   "lastName": participant.last_name,
                   "id": participant.id}
            red.rpush("queue", str(obj))

        socketio.emit("free-laptops")

        return ANSWERS[200], 200
