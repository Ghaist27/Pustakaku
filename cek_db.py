import sqlite3

db = sqlite3.connect("digipustaka.db")

tables = [
    "users",
    "books",
    "categories",
    "loans",
    "kunjungan",
    "user_action_requests"
]

for table in tables:
    print("\n================================")
    print("TABEL:", table)
    print("================================")

    columns = db.execute(f"PRAGMA table_info({table})").fetchall()

    for column in columns:
        print(
            "Nama:", column[1],
            "| Tipe:", column[2],
            "| PK:", column[5],
            "| Default:", column[4]
        )

    print("\nForeign Key:")
    foreign_keys = db.execute(
        f"PRAGMA foreign_key_list({table})"
    ).fetchall()

    if foreign_keys:
        for fk in foreign_keys:
            print(
                "Kolom:", fk[3],
                "->", fk[2] + "." + fk[4]
            )
    else:
        print("Tidak ada")

db.close()