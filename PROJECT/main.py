from flask import Flask
from data import db_session

app = Flask(__name__)


def main():
    db_session.global_init("db/database.db")
    app.run()


@app.route('/')
def first_page():
    return "Hello world"


if __name__ == "__main__":
    main()
