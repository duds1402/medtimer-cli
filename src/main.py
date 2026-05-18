from api_client import buscar_info_medicamento


def calcular_horarios(nome, hora_inicio, intervalo):
    if intervalo <= 0:
        raise ValueError("O intervalo deve ser maior que zero.")

    horarios = []
    for i in range(3):
        proxima_hora = (hora_inicio + (i * intervalo)) % 24
        horarios.append(f"{proxima_hora}:00")

    return f"Medicamento: {nome} | Próximas doses: {', '.join(horarios)}"


def main():
    print("--- MedTimer CLI ---")
    try:
        nome = input("Nome do remédio: ")
        inicio = int(input("Hora da primeira dose (0-23): "))
        intervalo = int(input("Intervalo em horas: "))

        resultado = calcular_horarios(nome, inicio, intervalo)
        print(f"\n✅ {resultado}")

        print("\n🔍 Buscando informações na base OpenFDA...")
        info = buscar_info_medicamento(nome)
        if info:
            print(f"✅ Encontrado: {info['nome']}")
            print(f"⚠️  Advertências: {info['advertencias']}")
        else:
            print("ℹ️  Nenhuma informação encontrada para este medicamento na base FDA.")

    except ValueError as e:
        print(f"\n❌ Erro: {e}")
    except Exception:
        print("\n❌ Entrada inválida.")


if __name__ == "__main__":
    main()