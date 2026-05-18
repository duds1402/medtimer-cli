import requests
from unittest.mock import patch, MagicMock
from api_client import buscar_info_medicamento


class TestIntegracaoOpenFDA:

    def test_busca_retorna_dicionario_valido_com_mock(self):
        resposta_mock = {
            "results": [{
                "openfda": {"brand_name": ["Aspirin"]},
                "warnings": ["Nao exceder a dose recomendada."]
            }]
        }
        mock_response = MagicMock()
        mock_response.json.return_value = resposta_mock
        mock_response.raise_for_status = MagicMock()

        with patch("api_client.requests.get", return_value=mock_response):
            resultado = buscar_info_medicamento("Aspirin")

        assert resultado is not None
        assert resultado["nome"] == "Aspirin"
        assert "dose" in resultado["advertencias"]

    def test_retorna_none_quando_api_falha(self):
        with patch(
            "api_client.requests.get",
            side_effect=requests.RequestException
        ):
            resultado = buscar_info_medicamento("Qualquer")

        assert resultado is None

    def test_retorna_none_quando_medicamento_nao_encontrado(self):
        resposta_vazia = {"results": []}
        mock_response = MagicMock()
        mock_response.json.return_value = resposta_vazia
        mock_response.raise_for_status = MagicMock()

        with patch("api_client.requests.get", return_value=mock_response):
            resultado = buscar_info_medicamento("MedicamentoInexistente123")

        assert resultado is None
