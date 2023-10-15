# app/routes/api/v1/chat.py

from flask import render_template, redirect, url_for, request, Blueprint

chat_api_v1 = Blueprint('chat_api_v1', __name__)