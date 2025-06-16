
from openpeygn.decorators import peygn_client, api_mapping

@peygn_client(base_url="http://google.com")
class TestClient:

    @api_mapping("GET", path="")
    def get_google(self): ...