import tkinter as tk
import mysql.connector
import getpass

from sourcecode.main import init_database


def notMainStuff():
    # Eltárolja a játékos nevét, bejelentkezés után ez megváltozik
    current_player = "guest"


    # inicializálja az adatbázist, bejelentkezés szükséges hozzá
    def init_database():
        database_username = input("Database username: ")
        database_password = getpass.getpass("Database password: ")

        my_database = mysql.connector.connect(
            host="localhost",
            user=database_username,
            passwd=database_password
        )

        my_cursor = my_database.cursor()
        my_cursor.execute("CREATE DATABASE IF NOT EXISTS loginSystem;")

        my_database = mysql.connector.connect(
            host="localhost",
            user=database_username,
            passwd=database_password,
            database="loginSystem"
        )

        my_cursor = my_database.cursor()

        my_cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id MEDIUMINT NOT NULL AUTO_INCREMENT,
            username VARCHAR(30) NOT NULL,
            password VARCHAR(30) NOT NULL,
            email VARCHAR(30) NOT NULL,
            PRIMARY KEY (id, username),
            UNIQUE (id),
            UNIQUE (username),
            UNIQUE(email)
        );""")

        return my_database, my_cursor


    # regisztrál egy felhasználót az adatbázisba (még nincs titkosítva a jelszó)
    def register():
        try:
            my_cursor.execute("SELECT MAX(id + 1) FROM users")
            id = my_cursor.fetchall()[0][0]
            if not id:
                id = 1
            my_cursor.execute(f"""
            INSERT INTO users (id, username, password, email)
            VALUES ({id}, '{r1.get()}', '{r2.get()}', '{r3.get()}')
            """)
            my_database.commit()
            print("Successfully registered.")
        except mysql.connector.errors.IntegrityError:
            print("The username or email is already taken.")
            my_database.rollback()


    # Megnézi, hogy a bejelentkezéshez megadott felhasználónév-jelszó páros létezik-e, ha igen akkor bejelentkezik.
    def login():
        my_cursor.execute(f"SELECT password FROM users WHERE username = '{e1.get()}'")
        result = my_cursor.fetchall()
        if len(result) == 0:
            print("This username does not exist.")
        else:
            if result[0][0] == e2.get():
                current_player = e1.get()
                print("Login successful")
            else:
                print("Invalid username or password")

def mainStuff():
    window = tk.Tk()
    window.title('Hello Python')
    window.geometry("600x600")

    # Rendkívül kezdetleges GUI a bejelentkezéshez.
    try:
        my_database, my_cursor = init_database()
    except mysql.connector.errors.ProgrammingError:
        print("Invalid username or password.")
        exit()
    tk.Label(window, text="Username").pack()
    e1 = tk.Entry(window)
    e1.pack()
    tk.Label(window, text="Password").pack()
    e2 = tk.Entry(window, show="*")
    e2.pack()
    tk.Button(window, text="Login", command=login).pack()
    tk.Label(window, text="").pack()
    tk.Label(window, text="Username").pack()
    r1 = tk.Entry(window)
    r1.pack()
    tk.Label(window, text="Password").pack()
    r2 = tk.Entry(window, show="*")
    r2.pack()
    tk.Label(window, text="Email").pack()
    r3 = tk.Entry(window)
    r3.pack()
    tk.Button(window, text="Register", command=register).pack()
    tk.Label(window, text="").pack()
    tk.Button(window, text="Play", command=window.destroy).pack()
    window.mainloop()
