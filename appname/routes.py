from flask import Blueprint, render_template

from .db import Session


bp = Blueprint('routes', __name__)


@bp.route('/')
def index():
    return render_template('index.html')