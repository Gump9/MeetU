from util import db, BaseModel


class password(BaseModel):
    __tablename__ = 'password'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)


class user(BaseModel):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    school = db.Column(db.String(100), nullable=False)
    # user_id = db.Column(db.Integer,db.Foreignkey("password.id"))
    # user = db.relationship("password", backref="users")
    # print(1)
