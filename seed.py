from app import app
from models import db, User

def seed():
    app.app_context().push()

    db.drop_all()
    db.create_all()

if __name__ == "__main__":
    seed()