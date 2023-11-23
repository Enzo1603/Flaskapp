from flask import render_template
from . import main
from .. import cache


@main.route("/")
@cache.cached()
def index():
    return render_template("main/home.html")
