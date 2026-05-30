# SIMULASI SECRET LEAKAGE
# Ini adalah contoh kode yang menyimpan kredensial secara hardcoded

DB_PASSWORD = "super-secret-password-123"
API_KEY = "AIzaSyA-ContohApiKeyGCP-12345"

# Key panjang untuk simulai gitleaks
DATABASE_URL = "postgres://admin:p4ssw0rd_rahasia_banget@db.example.com:5432/mydb"

def login():
    print(f"Menghubungkan ke database dengan password: {DB_PASSWORD}")

if __name__ == "__main__":
    login()
