import uuid
import datetime

"""BaseModel"""


class BaseModel:

    """
        Base model class representing common attributes and methods
        for other classes.
    """

    def __init__(self):
        """
        Args:
            id: string - assign with an uuid when an instance is created
            created_at: datetime - assign with the current datetime when
            an instance is created
            updated_at:datetime - assign with the current datetime when
            an instance is created
            and it will be updated every time you change your object
        """
        self.id = str(uuid.uuid1())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        """
                updates the public instance attribute updated_at with the
                current datetime
        """
        self.updated_at = datetime.datetime.now()
        return self.updated_at

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        class_name = self.__class__.__name__
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)

    def to_dict(self):
        """
                Returns a dictionary representation of the BaseModel instance.
                Returns:
                    [dict]: [dictionary]
        """

        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
