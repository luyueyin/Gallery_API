from main import ma
from marshmallow import fields
from schemas.exhibition_schema import ExhibitionSchema
from schemas.gallery_schema import GallerySchema

class TicketSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["ticket_id", "entry_date", "entry_time", "purchasing_date", "visitor", "gallery", "exhibition"]
        # load_only = ['artist_id']
    visitor = fields.Nested("VisitorSchema", only=("email",))
    exhibition = fields.Nested(ExhibitionSchema, only=("name", "start_date", "end_date",)) # exclude=("artist",) to avoid recursive calls between schemas
    gallery = fields.Nested(GallerySchema, only=("name","location",)) 

ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)


