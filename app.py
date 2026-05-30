# app.py

# SIMULASI SECRET LEAKAGE
# Ini adalah contoh kode yang menyimpan kredensial secara hardcoded

AWS_ACCESS_KEY_ID = "AKIAIMZAMB1AEXAMPLE1"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DB_PASSWORD = "KIAIMZAMB1AEXAMPLE1"
API_KEY = "JalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Key panjang untuk simulai gitleaks
DATABASE_URL = "postgres://admin:p4ssw0rd_rahasia_banget@db.example.com:5432/mydb"

def login():
    print(f"Menghubungkan ke database dengan password: {DB_PASSWORD}")

if __name__ == "__main__":
    login()
