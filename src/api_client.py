import requests

OPENFDA_URL = "https://api.fda.gov/drug/label.json"


def buscar_info_medicamento(nome: str) -> dict | None:
    try:
        params = {"search": f"openfda.brand_name:{nome}", "limit": 1}
        response = requests.get(OPENFDA_URL, params=params, timeout=5)
        response.raise_for_status()
        dados = response.json()
        resultado = dados["results"][0]
        return {
            "nome": resultado.get("openfda", {}).get("brand_name", [nome])[0],
            "advertencias": resultado.get("warnings", ["Sem advertências disponíveis."])[0][:300],
        }
    except (requests.RequestException, KeyError, IndexError):
        return None