from flask import current_app
from digiez_api.extensions import db

class BaseModel:
    def __repr__(self):
        return self.__class__.__name__ + '[' + self.name + ']'

    def save(self, commit=True):
        try:
            if not self.id:
                db.session.add(self)
            if not commit:
                db.session.flush()
            else:
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(' | '.join(['Error on save', repr(e)]))
            # raise ModelPersistError(e, model=self.__class__.__name__)
