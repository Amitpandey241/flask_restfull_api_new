from newProject import app
from project1.views import blueprint_resister
# from newProject.project1.flask_celery import  make_celery

app.register_blueprint(blueprint_resister)

if __name__ == "__main__":
    app.run(debug=True)
