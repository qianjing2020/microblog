# top-level python script that defines the flask application instance

from app import app, db
# import the app variable that is a member of the app package. can change to other names to avoid confusing

from app.models import User, Post

#creates a shell context that adds the database instance and models to the shell session, so instead of import db, we can just run 'flask shell'
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
