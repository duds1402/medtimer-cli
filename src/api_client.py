import requests

OPENFDA_URL = "https://api.fda.gov/drug/label.json"


def buscar_info_medicamento(nome: str) -> dict | None:
    try:
        params = {"search": f"openfda.brand_name:{nome}", "limit": 1}
        response = requests.get(OPENFDA_URL, params=params, timeout=5)
        response.raise_for_status()
        dados = response.json()
        resultado = dados["results"][0]
        nome_encontrado = resultado.get(
            "openfda", {}
        ).get("brand_name", [nome])[0]
        advertencias = resultado.get(
            "warnings", ["Sem advertencias disponiveis."]
        )[0][:300]
        return {"nome": nome_encontrado, "advertencias": advertencias}
    except (requests.RequestException, KeyError, IndexError):
        return None