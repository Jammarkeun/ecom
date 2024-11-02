# website/views.py
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Seller
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
@login_required
def home():
    # Query all sellers
    sellers = Seller.query.all()
    return render_template("home.html", user=current_user, sellers=sellers)