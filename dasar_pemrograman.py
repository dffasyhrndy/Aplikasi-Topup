from prettytable import PrettyTable

user_data = {
    "saldo": 1000,  
    "uc": 0,        
    "item": []  
}

items = {
    "M416 - The Fool": 500,
    "X-Suit Firaun Emas": 300,
    "M416 - Glacier": 300,
    "Avalanche X-Suit": 300,
    "M416 - Imperial Splendor": 300,
    "M416 - Techno Core": 300,
    "M416 - Shinobi Kami": 300,
    "Pharaoh": 100
}

def lihat_saldo():
    print(f"Saldo: {user_data['saldo']} | UC: {user_data['uc']}")

def tukar_saldo_ke_uc():
    rate = 10  
    jumlah_saldo = int(input("Masukkan jumlah saldo yang ingin ditukar: "))
    
    if jumlah_saldo > user_data["saldo"]:
        print("Saldo tidak mencukupi!")
    else:
        user_data["saldo"] -= jumlah_saldo
        user_data["uc"] += jumlah_saldo * rate
        print(f"{jumlah_saldo} saldo berhasil ditukar menjadi {jumlah_saldo * rate} UC.")

def tampilkan_item():
    table = PrettyTable()
    table.field_names = ["No", "Nama Item", "Harga (UC)"]
    
    for i, (item, harga) in enumerate(items.items(), start=1):
        table.add_row([i, item, harga])
    
    print(table)

def beli_item():
    tampilkan_item()
    pilihan = int(input("Masukkan nomor item yang ingin dibeli: ")) - 1
    item_list = list(items.keys())
    
    if pilihan < 0 or pilihan >= len(item_list):
        print("Nomor item tidak valid!")
        return

    item = item_list[pilihan]
    harga_item = items[item]

    if item in user_data["item"]:
        print(f"Anda sudah memiliki {item}.")
    elif user_data["uc"] < harga_item:
        print("UC tidak mencukupi!")
    else:
        user_data["uc"] -= harga_item
        user_data["item"].append(item)
        print(f"Anda berhasil membeli {item} seharga {harga_item} UC.")

def tambah_item():
    item_baru = input("Masukkan nama item: ")
    harga_baru = int(input("Masukkan harga item (dalam UC): "))

    if item_baru in items:
        print("Item sudah ada! Tidak bisa menambahkan item dengan nama yang sama")
    else:
        items[item_baru] = harga_baru
        print(f"Item '{item_baru}' seharga {harga_baru} UC berhasil ditambahkan.")

def hapus_item():
    item_hapus = input("Masukkan nama item yang ingin dihapus: ")
    if item_hapus in items:
        del items[item_hapus]
        print(f"Item '{item_hapus}' berhasil dihapus.")
    else:
        print("Item tidak ditemukan.")

def admin_menu():
    while True:
        table = PrettyTable()
        table.field_names = ["No", "Menu"]
        table.add_row(["1", "Tambah item"])
        table.add_row(["2", "Hapus item"])
        table.add_row(["3", "Tampilkan item"])
        table.add_row(["4", "Logout"])
        print(table)
        pilihan = input("Pilih opsi: ")
        
        if pilihan == "1":
            tambah_item()
        elif pilihan == "2":
            hapus_item()
        elif pilihan == "3":
            tampilkan_item()
        elif pilihan == "4":
            print("Keluar dari menu admin.")
            break
        else:
            print("Pilihan tidak valid!")

def user_menu():
    while True:
        table = PrettyTable()
        table.field_names = ["No", "Menu"]
        table.add_row(["1", "Lihat saldo"])
        table.add_row(["2", "Tukar Saldo"])
        table.add_row(["3", "Beli item"])
        table.add_row(["4", "Lihat item yang dimiliki"])
        table.add_row(["5", "Logout"])
        print(table)
        pilihan = input("Pilih opsi: ")
        
        if pilihan == "1":
            lihat_saldo()
        elif pilihan == "2":
            tukar_saldo_ke_uc()
        elif pilihan == "3":
            beli_item()
        elif pilihan == "4":
            lihat_item_dimiliki()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan toko game PUBG!")
            break
        else:
            print("Pilihan tidak valid!")

def lihat_item_dimiliki():
    if user_data["item"]:
        print("Item yang dimiliki:")
        for item in user_data["item"]:
            print(f"- {item}")
    else:
        print("Anda belum memiliki item apapun.")

def main():
    print("Selamat datang di Toko Game PUBG!")
    
    while True:
        table = PrettyTable()
        table.field_names = ["No", "Menu"]
        table.add_row(["1", "Admin"])
        table.add_row(["2", "User"])
        table.add_row(["3", "Logout"])
        print(table)
        pilihan = input("Pilih opsi: ")
        
        if pilihan == "1":
            password = input("Masukkan password admin: ")
            if password == "admin123":
                admin_menu()
            else:
                print("Password salah!")
        elif pilihan == "2":
            user_menu()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("Pilihan tidak valid!")

main()