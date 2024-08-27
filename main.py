from  Demographic_data_analyzer import datos

def main():

    result = datos()

    print("Resultados:")
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()