# How to access global var on local scope > with "global"
# It's not recommended because very confusing when you revisiting again

# !!! Python tidak punya block scope (pada if/else/for/while), artinya semua yang dioperasikan didalam 4 statement tadi bisa diakses diluar scopenya

# Scope pada Python yakni diluar dan didalam function saja

enemies = "Green Goblin"

def whos_enemy():
    global enemies
    print(f"on local scope {enemies}")

whos_enemy()
print(f"on global scope {enemies}")

# The other way to manipulate variable on global scope without using "global":

number = 1

def multiply():
    print(f"on local : {number}")
    return number+1

number = multiply()
print(f"on global : {number}")

# Gunakan huruf besar jika kita ingin membuat Constant. Memang bukan rules dari Python, tapi setidaknya menjadi standar baku untuk selalu mengingatkan
# kita agar tidak mengubah nilainya di kemudian hari

USERNAME = "syarif"
PRIVATE_EMAIL = "syarif6@gamil.com"