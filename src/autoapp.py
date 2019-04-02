import app
import routes
from services.config_service import ConfigService


app.register_all_blueprints()
app.flask_app.run(port=ConfigService.get_port())
