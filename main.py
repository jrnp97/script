# main.py
import pandas as pd

if __name__ == "__main__":
    archivo = pd.read_excel("./Sample - Superstore.xls")
    print(archivo.profit_234)
    print("="*50)
    for row, dato in enumerate(archivo.quantity):
        pass #print(row, dato)