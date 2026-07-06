login = input()
parol = input()
natija = login == "admin" and len(parol) >= 6
print(natija)