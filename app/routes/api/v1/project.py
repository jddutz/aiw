# app/routes/api/v1/project.py

from flask import render_template, redirect, url_for, request, Blueprint

project_api_v1 = Blueprint("project_api_v1", __name__)
