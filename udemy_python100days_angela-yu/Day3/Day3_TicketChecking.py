tinggiPengunjung = int(input("Berapakah tinggi anda? \n"))

if tinggiPengunjung >= 120:
    print("You can ride the rollercoaster")
    umur_pengunjung = int(input("Berapakah umur anda? \n"))
    harga_tiket = 0
    if umur_pengunjung <12:
        harga_tiket += 5
    elif umur_pengunjung <=18:
        harga_tiket += 7
    elif umur_pengunjung >=45 and umur_pengunjung <= 55:
        harga_tiket += 0
    else:
        harga_tiket += 12
    
    is_added_photo = input("Apakah tambah foto ? y/n >")
    if is_added_photo == "y" and umur_pengunjung >=45 and umur_pengunjung <= 45:
        harga_tiket += 3
    elif (is_added_photo == "y"):
        harga_tiket += 0
    
    print(f"Harga tiket anda : $ {harga_tiket}")
    
else:
    print("Maaf, anda tidak boleh naik rollercoaster")