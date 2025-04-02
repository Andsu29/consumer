import traceback
import time


def get_exception(f):
    print("Antes do try", flush=True)
    try:
        print("Antes da função", flush=True)
        time.sleep(5)
        f()
        print("Depois da função", flush=True)
    except Exception as e:
        print(f"Erro no consumer: {e}", flush=True)
        print(traceback.format_exc())


# Necessita tratar outros erros
