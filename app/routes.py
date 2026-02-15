from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import URL
from app.utils import generate_short_code, is_valid_url

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        original_url = request.form["url"]

        if not is_valid_url(original_url):
            flash("Invalid URL")
            return redirect(url_for("main.home"))

        short_code = generate_short_code()

        new_url = URL(original_url=original_url, short_code=short_code)
        db.session.add(new_url)
        db.session.commit()

        short_url = request.host_url + short_code
        return render_template("home.html", short_url=short_url)

    return render_template("home.html")


@main.route("/<short_code>")
def redirect_url(short_code):
    url = URL.query.filter_by(short_code=short_code).first_or_404()
    url.clicks += 1
    db.session.commit()
    return redirect(url.original_url)


@main.route("/history")
def history():
    urls = URL.query.order_by(URL.created_at.desc()).all()
    return render_template("history.html", urls=urls)
