from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from schemas import ItemSchema, ItemUpdateSchema
from db import db
from models import ItemModel

ITEM_NOT_FOUND = "Item not found"

blp = Blueprint("items", __name__, description="Operations on items")

@blp.route('/item/<string:item_id>')
class ItemList(MethodView):
    def get(self, item_id):
        try:   
            item = ItemModel.query.get_or_404(item_id)
            return item
        except KeyError:
            abort(404, message=ITEM_NOT_FOUND)
    
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        #item = ItemModel.query.get_or_404(item_id)
        raise NotImplementedError("Updating an item is not implemented.")
      
    def delete(self, item_id):
       #item = ItemModel.query.get_or_404(item_id)
       raise NotImplementedError("Deleting an item is not implemented.")



@blp.route('/item')
class Item(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        item = ItemModel.query.get()
    
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred whilte inserting the item.")

        return item