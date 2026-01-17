import requests
import os

BASE_URL = "https://raw.githubusercontent.com/graphql-compose/graphql-compose-examples/master/examples/northwind/data/csv"
FILES = [
    "orders.csv",
    "order_details.csv",
    "customers.csv",
    "products.csv",
    "employees.csv"
]

RAW_PATH = r"C:\Users\Gabriela Zuppardo\OneDrive\Documentos\projetos_pessoais\northwind-spark-data-pipeline\data\raw\northwind"


def download_northwind():
    os.makedirs(RAW_PATH, exist_ok=True)

    for file in FILES:
        target_file = os.path.join(RAW_PATH, file)

        if os.path.exists(target_file):
            print(f"{file} já existe. Ignorado.")
            continue

        response = requests.get(f"{BASE_URL}/{file}")
        response.raise_for_status()

        with open(target_file, "wb") as f:
            f.write(response.content)

        print(f"{file} baixado com sucesso.")


if __name__ == "__main__":
    download_northwind()
