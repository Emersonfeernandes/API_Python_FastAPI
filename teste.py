import pytest
from requests import get, post
from json import loads

class TestAPI:
    def setup(self):
        self.url = 'http://127.0.0.1:8000'

    def test_resposta(self):
        respo = get(self.url)
        assert respo.ok

    def test_msg_API(self):
        respo = get(self.url)
        msg = respo.text
        assert msg == '"Olá mundo!"'

    def test_POST(self):
        # pode testar as outras operações se quiser.
        respo = post(self.url + '/operacao'
                    , json = {})
        msg = loads(respo.text)
        resposta_Post = {
                        "valor1": 7,
                        "valor2": 7,
                        "operaçao": "adição",
                        "resultado": 14
                        }
