"""
Module that contains the audio object from the database
"""
# pylint: disable=invalid-name, too-many-arguments, too-few-public-methods, no-member, dangerous-default-value
from .helpers import db, add_to_db
from .category import Category


class Audio(db.Model):
    """
    Class that maps the Audio object to
     the corresponding database table ('audio' table).

    Attributes
    ----------
    id : int , optional
        Auto-generated object id.
    category_id : int
        The id of the category that this audio belongs to.
    link : str
        The link to the location where the audio is stored in the cloud.
    description : str
        A short description of the audio.
    attribute : str
        The attribute describing the audio. (Ex: pen)

    Methods
    -------
    create_audio(link, description="", attribute="", c_id=None)
        Method that creates a new audio and adds it into the database.

    """

    __tablename__ = 'audio'

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(
        db.Integer, db.ForeignKey(Category.id), nullable=True)
    link = db.Column(db.Text, nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    attribute = db.Column(db.String(40), nullable=False)

    @staticmethod
    def create_audio(link, description="", attribute="", c_id=None):
        """
        Creates an audio object and inserts it into the database

        Parameters
        ----------
        link : str
            Link to the audio location.
        description : str , optional
            A short description of the audio.
        attribute : str , optional
            The attribute describing the audio.
        c_id : int , optional
            The category that the audios belongs to. (can be assigned at a later time)

        Returns
        -------
        audio : audio
            The audio object that was created.

        """

        audio = Audio(category_id=c_id, link=link,
                    description=description, attribute=attribute)
        add_to_db(audio)
        return audio

    def __repr__(self):
        """The string representation of the object."""
        return str(self.link)
