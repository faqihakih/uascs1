import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="kampus"
)
if db.is_connected():
  print("Berhasil terhubung ke database")
#Faqih Zada Ikhsan
def insert_data(db):
    NIM = input("Masukan nim: ")
    Nama = input("Masukan nama: ")
    Alamat = input("Masukan alamat: ")
    val = (NIM, Nama, Alamat)
    cursor = db.cursor()
    sql = "INSERT INTO mahasiswa (NIM, Nama, Alamat) VALUES (%s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM mahasiswa"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)

#Faqih Zada Ikhsan
def update_data(db):
    cursor = db.cursor()
    show_data(db)
    ID = input("pilih data> ")
    NIM = input("NIM Baru ")
    Nama = input("Nama baru: ")
    Alamat = input("Alamat baru: ")
    sql = "UPDATE mahasiswa SET Nim=%s, Nama=%s, Alamat=%s WHERE ID=%s"
    val = (NIM, Nama, Alamat, ID)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))


def delete_data(db):
    cursor = db.cursor()
    show_data(db)
    ID = input("pilih data yang akan di hapus> ")
    sql = "DELETE FROM mahasiswa WHERE ID=%s"
    val = (ID,)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))

#Faqih Zada Ikhsan
def show_menu(db):
    print("=== APLIKASI Data Mahasiswa ===")
    print("1. Menambah Data Mahasiswa")
    print("2. Mengubah Data Mahasiswa")
    print("3. Menghapus Data Mahasiswa")
    print("4. Melihat Seluruh Data Mahasiswa")
    print("5. Keluar")
    print("------------------")
    menu = input("Masukan Pilihan Anda : ")


    if menu == "1":
        insert_data(db)
    elif menu == "2":
        update_data(db)
    elif menu == "3":
        delete_data(db)
    elif menu == "4":
        show_data(db)
    elif menu == "5":
        exit()
    else:
        print("Menu salah!")

#Faqih Zada Ikhsan
if __name__ == "__main__":
    while (True):
        show_menu(db)