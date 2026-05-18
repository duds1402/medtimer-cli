from api_client import buscar_info_medicamento


def calcular_horarios(nome, hora_inicio, intervalo):
    if intervalo <= 0:
        raise ValueError("O intervalo deve ser maior que zero.")

    horarios = []
    for i in range(3):
        proxima_hora = (hora_inicio + (i * intervalo)) % 24
        horarios.append(f"{proxima_hora}:00")

    doses = ', '.join(horarios)
    return f"Medicamento: {nome} | Proximas doses: {doses}"


def main():
    print("--- MedTimer CLI ---")
    try:
        nome = input("Nome do remedio: ")
        inicio = int(input("Hora da primeira dose (0-23): "))
        intervalo = int(input("Intervalo em horas: "))

        resultado = calcular_horarios(nome, inicio, intervalo)
        print(f"\n{resultado}")

        print("\nBuscando informacoes na base OpenFDA...")
        info = buscar_info_medicamento(nome)
        if info:
            print(f"Encontrado: {info['nome']}")
            print(f"Advertencias: {info['advertencias']}")
        else:
            print("Nenhuma informacao encontrada para este medicamento.")

    except ValueError as e:
        print(f"\nErro: {e}")
    except Exception:
        print("\nEntrada invalida.")


if __name__ == "__main__":
    main()

