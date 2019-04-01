import app
import routes


app.register_all_blueprints()
app.flask_app.run(port=5000)
