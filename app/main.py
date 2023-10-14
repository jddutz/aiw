from app import app, db

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://johndutz:password@localhost/johndutz$mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False