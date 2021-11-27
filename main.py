###########imports###########
import os
import time
try:
    import MySQLdb
    import json
    import sqlite3
    from rich import print as prrint
    from rich.console import Console
    from rich.progress import track
    from rich.text import Text
except:
    print("Import Error")
    if input("Do you want to install the required modules? (yes/no): ").lower() == "yes":
        try:
            os.system("pip install -r requirements.txt")
        except:
            for module in ["rich", "mysqlclient", "prettytable", "cryptography"]:
                os.system(f"pip install {module}")
    else:
        print("Ok... PLease re/install them yourself.")
##########functions##########
inp = Text(f"root@{os.getlogin()}: ")
console = Console()
try:
    conf = open("databases.json")
except FileNotFoundError:
    conf = open("databases.json", "w")
    conf.write("{}")
finally:
    conf.close()


def clear():
    os.system("cls")


def ui(menu=""):
    clear()
    prrint(logo)
    console.print("                                                                                                                                                                                                                                                                                        ", style="white on blue")
    if menu != "":
        console.print(menu, justify="center")
        console.print("                                                                                                                                                                                                                                                                                        ", style="white on blue")
        return input(inp)


def connect_to_server(host, db, user, pw, port):
    try:
        for n in track(range(5), description="[greeb]Connecting"):
            conn = MySQLdb.connect(
            host=host, db=db, user=user, passwd=pw, port=port)
            curr = conn.cursor()
    except:
        ui()
        prrint(
            "[red]An Error occured, while connecting to the Database.\nMake sure the credentials are right.")
        time.sleep(3)
        return
    ui()
    console.print("[green] Connection established.", justify="center")
    time.sleep(2)
    while True:
        choice = ui(menu_connected)
        if choice == "1":
            ui()
            prrint("[yellow]Enter Query:")
            query = input("- ")
            try:
                curr.execute(query)
            except Exception as e:
                ui()
                console.print(f"[red] An Error occured:\n{e}", justify="center")
                input("Press enter to continue ")
            else:
                prrint(f"[green] Executed Query: {query}")
                time.sleep(3)
        elif choice == "2":
            ui()
            prrint("[yellow]Enter Query:")
            query = input("- ")
            try:
                curr.execute(query)
            except Exception as e:
                ui()
                console.print(f"[red] An Error occured:\n{e}", justify="center")
                input("Press enter to continue ")
            else:
                try:
                    data = curr.fetchall()[0]
                except:
                    ui()
                    console.print("[red]Query is empty")
                    time.sleep(2)
                else:
                    dats = ""
                    new_line = ""
                    if len(data) > 10:
                        new_line = "\n"
                    for item in data:
                        if item == ""or item == " ":
                            item = "Empty"
                        dats += str(item) + " " + new_line
                    ui()
                    prrint("[yellow] " + dats)
                    input("Press enter to continue ")
        elif choice == "3":
            conn.close()
            break
def connect_to_local(path):
    try:
        conn = sqlite3.connect(path)
        curr = conn.cursor()
    except:
        ui()
        prrint(
            "[red]An Error occured, while connecting to the Database.\nMake sure the credentials are right.")
        time.sleep(3)
        return
    ui()
    console.print("[green] Connection established.", justify="center")
    time.sleep(2)
    while True:
        choice = ui(menu_connected)
        if choice == "1":
            ui()
            prrint("[yellow]Enter Query:")
            query = input("- ")
            try:
                curr.execute(query)
            except Exception as e:
                ui()
                console.print(f"[red] An Error occured:\n{e}", justify="center")
                input("Press enter to continue")
            else:
                prrint(f"[green] Executed Query: {query}")
                time.sleep(3)
        elif choice == "2":
            ui()
            prrint("[yellow]Enter Query:")
            query = input("- ")
            try:
                curr.execute(query)
            except Exception as e:
                ui()
                console.print(f"[red] An Error occured:\n{e}", justify="center")
                input("Press enter to continue ")
            else:
                try:
                    data = curr.fetchall()[0]
                except:
                    ui()
                    console.print("[red]Query is empty")
                    time.sleep(2)
                else:
                    dats = ""
                    new_line = ""
                    if len(data) > 10:
                        new_line = "\n"
                    for item in data:
                        if item == ""or item == " ":
                            item = "Empty"
                        dats += str(item) + " " + new_line
                    ui()
                    prrint("[yellow] " + dats)
                    input("Press enter to continue ")
        elif choice == "3":
            conn.close()
            break

############vars#############
stop = False
logo = r"""[blue]
________  ________  ___                     ________  ___       ___  _______   ________   _________   
|\   ____\|\   __  \|\  \                   |\   ____\|\  \     |\  \|\  ___ \ |\   ___  \|\___   ___\ 
\ \  \___|\ \  \|\  \ \  \      ____________\ \  \___|\ \  \    \ \  \ \   __/|\ \  \\ \  \|___ \  \_| 
 \ \_____  \ \  \\\  \ \  \    |\____________\ \  \    \ \  \    \ \  \ \  \_|/_\ \  \\ \  \   \ \  \  
  \|____|\  \ \  \\\  \ \  \___\|____________|\ \  \____\ \  \____\ \  \ \  \_|\ \ \  \\ \  \   \ \  \ 
    ____\_\  \ \_____  \ \_______\             \ \_______\ \_______\ \__\ \_______\ \__\\ \__\   \ \__\
   |\_________\|___| \__\|_______|              \|_______|\|_______|\|__|\|_______|\|__| \|__|    \|__|
   \|_________|     \|__|                                                                    
"""
menu_st = r"""[blue]------------------------------------------------ 
|[yellow] [1] Connect to Server | [2] Connect to Local [blue]|
|[yellow] [3] Credits/Support   | [4] Exit             [blue]|
------------------------------------------------"""
menu_server = r"""[blue]------------------------------------------------
|[yellow] [1] Login Manually    | [2] Load Credentials [blue]|
|[yellow] [3] Exit                                     [blue]|
------------------------------------------------"""
menu_local = r"""[blue]------------------------------------------------
|[yellow] [1] Connect DB        | [2] Create DB        [blue]|
|[yellow] [3] Exit                                     [blue]|
------------------------------------------------"""
menu_connected = r"""[blue]------------------------------------------------
|[yellow] [1] Manual Query      | [2] SELECT           [blue]|
|[yellow] [3] Exit                                     [blue]|
------------------------------------------------"""
###########start#############
os.system("title SQL-Client V-0.1")
prrint(logo)
"""for n in track(range(10), description="[blue]Loading"):
    time.sleep(0.3)"""

while True:
    choice = ui(menu_st)
    if choice == "1":
        while True:
            choice = ui(menu_server)
            if choice == "1":
                ui()
                host = input("Host Url:")
                db = input("Database Name: ")
                user = input("Username: ")
                password = input("Password: ")
                port = input("Port: ")
                if input("Do you want to safe these credentials? [yes/no]: ").lower() == "yes":
                    name = ""
                    while name == "":
                        name = input(
                            "Under which name should the credentials be saved: ")
                    with open("databases.json", "r") as f:
                        data = json.load(f)
                        data[name] = {
                            "host": host,
                            "db": db,
                            "user": user,
                            "password": password,
                            "port": int(port)
                        }
                    with open("databases.json", "w") as f:
                        json.dump(data, f)
                    ui()
                    prrint(f"[green]Saved the Credentials under name: {name}")
                    time.sleep(2)
                connect_to_server(host, db, user, password, port)
            elif choice == "2":
                ui()
                database = input("Database Name: ")
                with open("databases.json") as f:
                    data = json.load(f)
                    if database in data.keys():
                        data = data[database]
                        host = data["host"]
                        db = data["db"]
                        user = data["user"]
                        password = data["password"]
                        port = data["port"]
                        connect_to_server(host, db, user, password, port)
                    else:
                        prrint("[red]Database doesnt exist")
                        time.sleep(3)
            elif choice == "3":
                break

    elif choice == "2":
        while True:
            choice = ui(menu_local)
            if choice == "1":
                ui()
                path = input("Input full path to the database: ")
                while not os.path.exists(path):
                    prrint("[red] Database doesnt exist")
                    path = input("Input full path to the database: ")
                connect_to_local(path)
            elif choice == "2":
                ui()
                name = input("Name of the Database: ")
                if name == "":
                    prrint("[red]Can't be empty.")
                    input("Name of the Database: ")
                file_end = input("Type of Database (db,db3,sdb,s3db,sqlite,sqlite3):\n")
                if file_end == "":
                    prrint("[red]Can't be empty.")
                    file_end = input("Type of Database (sqlite, db, ...):\n")
                conn = sqlite3.connect(f"{name}.{file_end}")
                conn.close()
                ui()
                console.print(f"[green]Succesfully created Database {name + '.' + file_end}, \nat path: {os.getcwd()}.", justify="center")
                time.sleep(3)
            elif choice == "3":
                break
    elif choice == "3":
        ui()
        console.print(
            "[blue_underline] https://github.com/screamz2k", justify="center")
        input("Press enter to continue.")
    elif choice == "4":
        console.print("[yellow]Goodbye...", justify="center")
        time.sleep(2)
        break
