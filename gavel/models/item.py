from gavel.models import db
import gavel.crowd_bt as crowd_bt
from sqlalchemy.orm.exc import NoResultFound

view_table = db.Table('view',
    db.Column('item_id', db.Integer, db.ForeignKey('item.id')),
    db.Column('annotator_id', db.Integer, db.ForeignKey('annotator.id'))
)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    alias = db.Column(db.Text, nullable=True)
    category = db.Column(db.Text, nullable=False)
    technicalName = db.Column(db.Text, nullable=False)
    establishedBy = db.Column(db.Text, nullable=True)
    yearEstablished = db.Column(db.Text, nullable=True)
    linkToVideo = db.Column(db.Text, nullable=True)
    startPos = db.Column(db.Text, nullable=False)
    endPos = db.Column(db.Text, nullable=False)
    difficultyLevel = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=True)
    tips0 = db.Column(db.Text, nullable=True)
    tips1 = db.Column(db.Text, nullable=True)
    tips2 = db.Column(db.Text, nullable=True)
    tips3 = db.Column(db.Text, nullable=True)
    tips4 = db.Column(db.Text, nullable=True)
    tips5 = db.Column(db.Text, nullable=True)
    

    active = db.Column(db.Boolean, default=True, nullable=False)
    viewed = db.relationship('Annotator', secondary=view_table)
    prioritized = db.Column(db.Boolean, default=False, nullable=False)

    mu = db.Column(db.Float)
    sigma_sq = db.Column(db.Float)

    def __init__(self, alias, category, technicalName, establishedBy, yearEstablished, linkToVideo, startPos, endPos, difficultyLevel, description, tips0, tips1, tips2, tips3, tips4, tips5):
        if len(alias) > 1:
            self.alias = alias
        else:
            self.alias = technicalName
        self.category = category
        self.technicalName = technicalName
        self.establishedBy = establishedBy
        self.yearEstablished = yearEstablished
        self.linkToVideo = linkToVideo
        self.startPos = startPos
        self.endPos = endPos
        self.difficultyLevel = difficultyLevel
        self.description = description
        self.tips0 = tips0
        self.tips1 = tips1
        self.tips2 = tips2
        self.tips3 = tips3
        self.tips4 = tips4
        self.tips5 = tips5

        self.mu = crowd_bt.MU_PRIOR
        self.sigma_sq = crowd_bt.SIGMA_SQ_PRIOR

    @classmethod
    def by_id(cls, uid):
        if uid is None:
            return None
        try:
            item = cls.query.get(uid)
        except NoResultFound:
            item = None
        return item
