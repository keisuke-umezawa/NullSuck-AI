import settings
import responder
from handlers import (
    WineAttributeResource,
    PredictionResource,
)


api = responder.API(
    cors=True,
    allowed_hosts=["*"],
)

api.add_route('/api/wine_attributes', WineAttributeResource)
api.add_route('/api/predict', PredictionResource)


if __name__ == '__main':
    api.run()
