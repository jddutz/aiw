# app/routes/www/chat.py

from flask import Blueprint

from typing import Optional
from pydantic import BaseModel

story_blueprint = Blueprint("story", __name__)


@story_blueprint.route("/create", methods=["GET", "POST"])
async def create():
    pass
