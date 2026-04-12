import pytest
from src.main import calcular_horarios


def test_caminho_feliz():
    # Teste de funcionamento normal
    res = calcular_horarios("Aspirina", 8, 8)
    assert "8:00, 16:00, 0:00" in res


def test_intervalo_invalido():
    # Teste de entrada indevida
    with pytest.raises(ValueError):
        calcular_horarios("Remédio", 10, 0)


def test_virada_de_dia():
    # Teste de caso limite (passando de 24h)
    res = calcular_horarios("Vitamina", 22, 4)
    assert "22:00, 2:00, 6:00" in res
