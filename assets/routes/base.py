from flask import Blueprint, url_for, redirect, render_template


bp = Blueprint("base", __name__)


@bp.route("/")
def index() -> str:
    return render_template("index.html", css="landing-page.css")


@bp.route("/about")
def about() -> str:
    return render_template("about.html", css="about.css")
