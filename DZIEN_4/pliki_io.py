f = open("dane.txt","r",encoding="utf-8")
print(f.read())
f.close()

f = open(r"C:\Temp\message.txt","r",encoding="utf-8")
print(f.read())
f.close()

g = open("dane.txt","a",encoding="utf-8")
g.write("Nowy wiersz: dfhskdjksvnfkld756454w5")
g.close()

f = open("info.txt","w",encoding="utf-8")
f.write("Osoba: Anna Kot\n")
f.write("Data urodzenia: 14-01-1997\n")
f.write("Grupa: 10A")
f.close()

f = open("info.txt","a",encoding="utf-8")
f.write("\n a gdzie są poprzednie linie?")
