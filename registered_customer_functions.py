import functionality
from tabulate import tabulate
from datetime import datetime, timedelta
from prettytable import PrettyTable

import menus


# Funkcija za proveru sifre

# Funkcija za ucitavanje postojecih korisnika iz fajla u recnik
def load_registered_customers(file_name):
    registered_customers = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                parts_of_line = line.strip().split("|")
                customer = {
                    "username": parts_of_line[0],
                    "password": parts_of_line[1],
                    "name": parts_of_line[2],
                    "last_name": parts_of_line[3],
                    "role": parts_of_line[4]
                }
                registered_customers.append(customer)
    except FileNotFoundError:
        pass  # Ako fajl ne postoji, nastavljamo sa praznom listom
    return registered_customers


# Funkcija za dodavanje novog korisnika u recnik
def registering_new_customer(registered_customers, new_username, new_password, new_name, new_last_name):
    if any(customer["username"] == new_username for customer in registered_customers):
        print("This username already exist !!!")
        return False
    if not functionality.check_password(new_password):
        print("Password does not meet the requirements !!!")
        return False

    new_customer = {
        "username": new_username,
        "password": new_password,
        "name": new_name,
        "last_name": new_last_name,
        "role": "registered_customer"
    }
    registered_customers.append(new_customer)
    # Korisnik je {new_username} je dodat u recnik !!!
    return True


# Funkcija za upisivanje registrovanih korisnika uz recnika u fajl
def write_registered_customers_in_file(file_name, registered_customers):
    with open(file_name, "w") as file:
        for customer in registered_customers:
            line = f"{customer['username']}|{customer['password']}|{customer['name']}|{customer['last_name']}|{customer['role']}\n"
            file.write(line)


def reserve_tickets(username, cinema_projections, projection_terms, tickets, reserved_tickets):
    while True:
        menus.reservation_tickets_registered_customer_menu()
        # datum kupovine karte
        today = datetime.today()
        date = today.strftime('%d.%m.%Y')
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 0:
            print("Exiting reservation.")
            return
        elif choice == 1:
            functionality.search_for_terms_of_cinema_projections(cinema_projections, projection_terms)
            while True:
                try:
                    choice2 = input("Enter the code for projection: ")
                    term_code = choice2[-2:]
                    projection_code = choice2[:-2]

                    found_term = {}
                    for term in projection_terms:
                        if term['term_code'] == term_code and term['projection_code'] == projection_code:
                            functionality.print_seat_matrix(term)
                            print("Occupied places are marked with the character X")
                            found_term = term
                            break

                    if len(found_term) == 0:
                        print("No term found !!!")
                        y = input("Do you want to continue? (yes/no): ").lower()
                        if y == "no":
                            return
                        else:
                            continue

                    row = int(input("Enter the row number: ")) - 1
                    column = input("Enter the column letter: ").upper()

                    if row < 0 or row >= len(found_term['seat_matrix']) or ord(column) - ord('A') < 0 or ord(column) - ord(
                            'A') >= len(found_term['seat_matrix'][0]):
                        print("Invalid seat selection. Please try again.")
                        continue

                    if found_term['seat_matrix'][row][ord(column) - ord('A')] == 'X':
                        print("Seat already taken. Please choose another seat.")
                        continue

                    # Ovde ažurirati matricu sedišta i dodati rezervaciju u listu i fajl
                    seat_label = f"{row + 1}{column}"
                    found_term['seat_matrix'][row][ord(column) - ord('A')] = 'X'

                    full_code = projection_code + term_code

                    ticket_price = 100
                    for projection in cinema_projections:
                        if projection['id'] == projection_code:
                            # Gledamo da za odredjenje dane menjamo cenu karata ...
                            date_string = found_term['date']
                            date_obj = datetime.strptime(date_string, '%d.%m.%Y')
                            term_day = date_obj.strftime('%A').lower()
                            if term_day == 'tuesday':
                                ticket_price = projection['ticket_price'] - 50
                            elif term_day in ['saturday', 'sunday']:
                                ticket_price = projection['ticket_price'] + 50
                            else:
                                ticket_price = projection['ticket_price']
                            break
                        else:
                            ticket_price = 100

                    new_ticket = {
                        'username': username,
                        'term_id': full_code,
                        'term_date': found_term['date'],
                        'seat_code': seat_label,
                        'sale_date': date,
                        'seller_username': "none",
                        'ticket_price': ticket_price,
                        'status': "reserved"
                    }

                    tickets.append(new_ticket)

                    reservation_info = f"{projection_code}{term_code}|{found_term['date']}|{seat_label}|{date}|none|{ticket_price}|reserved"
                    reserved_tickets[username] = reserved_tickets.get(username, [])
                    reserved_tickets[username].append(reservation_info)

                    print("Ticket reserved successfully!")

                    choice3 = input("Do you want to reserve more tickets? (yes/no): ").lower()
                    if choice3 == "no":
                        return
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter valid seat details.")
        elif choice == 2:
            while True:
                try:
                    choice2 = input("Enter the code for projection: ")
                    term_code = choice2[-2:]
                    projection_code = choice2[:-2]

                    found_term = {}
                    for term in projection_terms:
                        if term['term_code'] == term_code and term['projection_code'] == projection_code:
                            functionality.print_seat_matrix(term)
                            print("Occupied places are marked with the character X")
                            found_term = term
                            break

                    if len(found_term) == 0:
                        print("No term found !!!")
                        y = input("Do you want to continue? (yes/no): ").lower()
                        if y == "no":
                            return
                        else:
                            continue

                    row = int(input("Enter the row number: ")) - 1
                    column = input("Enter the column letter: ").upper()

                    if row < 0 or row >= len(found_term['seat_matrix']) or ord(column) - ord('A') < 0 or ord(column) - ord(
                            'A') >= len(found_term['seat_matrix'][0]):
                        print("Invalid seat selection. Please try again.")
                        continue

                    if found_term['seat_matrix'][row][ord(column) - ord('A')] == 'X':
                        print("Seat already taken. Please choose another seat.")
                        continue

                    # Ovde ažurirati matricu sedišta i dodati rezervaciju u listu i fajl
                    seat_label = f"{row + 1}{column}"
                    found_term['seat_matrix'][row][ord(column) - ord('A')] = 'X'

                    full_code = projection_code + term_code

                    ticket_price = 100
                    for projection in cinema_projections:
                        if projection['id'] == projection_code:
                            date_string = found_term['date']
                            date_obj = datetime.strptime(date_string, '%d.%m.%Y')
                            term_day = date_obj.strftime('%A').lower()
                            if term_day == 'tuesday':
                                ticket_price = projection['ticket_price'] - 50
                            elif term_day in ['saturday', 'sunday']:
                                ticket_price = projection['ticket_price'] + 50
                            else:
                                ticket_price = projection['ticket_price']
                            break
                        else:
                            ticket_price = 100

                    new_ticket = {
                        'username': username,
                        'term_id': full_code,
                        'term_date': found_term['date'],
                        'seat_code': seat_label,
                        'sale_date': date,
                        'seller_username': "none",
                        'ticket_price': ticket_price,
                        'status': "reserved"
                    }

                    tickets.append(new_ticket)

                    reservation_info = f"{projection_code}{term_code}|{found_term['date']}|{seat_label}|{date}|none|{ticket_price}|reserved"
                    reserved_tickets[username] = reserved_tickets.get(username, [])
                    reserved_tickets[username].append(reservation_info)
                    print(reserved_tickets[username])
                    print(tickets)
                    print("Ticket reserved successfully!")

                    choice3 = input("Do you want to reserve more tickets? (yes/no): ").lower()
                    if choice3 == "no":
                        return
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter valid seat details.")
        else:
            print("Invalid input !!!")


def load_reserved_tickets(filename):
    reserved_tickets = {}

    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        ticket_info = line.strip().split('|')
        username = ticket_info[0]  # Korisnicko ime
        status = ticket_info[-1]  # Status karte: reserved/sold
        ticket = '|'.join(ticket_info[1:])  # Informacije o karti

        # Dodavanje karata korisniku na njegov username
        if status == 'reserved':
            if username in reserved_tickets:
                reserved_tickets[username].append(ticket)
            else:
                reserved_tickets[username] = [ticket]

    return reserved_tickets


def load_sold_tickets(filename):
    sold_tickets = {}

    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        ticket_info = line.strip().split('|')
        username = ticket_info[0]  # Korisnicko ime
        status = ticket_info[-1]  # Status karte: reserved/sold
        ticket = '|'.join(ticket_info[1:])  # Informacije o karti

        # Dodavanje karata korisniku na njegov username
        if status == 'sold':
            if username in sold_tickets:
                sold_tickets[username].append(ticket)
            else:
                sold_tickets[username] = [ticket]

    return sold_tickets


def display_reserved_tickets(username, reserved_tickets, cinema_projections, projection_terms):
    print("Reserved tickets for user:", username)
    if username not in reserved_tickets:
        print("No reservations found for this user.")
        return

    user_tickets = reserved_tickets[username]
    table_data = []

    for ticket in user_tickets:
        ticket_info = ticket.split('|')
        projection_code = ticket_info[0][:4]  # 1112AE idemo od pocetka do 4 karaktera
        term_code = ticket_info[0][4:]
        seat = ticket_info[2]
        purchase_date = ticket_info[3]
        projection_date = ticket_info[1]

        # print(ticket_info, projection_code, term_code, seat, purchase_date)

        projection = next((projection for projection in cinema_projections if projection['id'] == projection_code),
                          None)
        term = next((term for term in projection_terms if
                     term['projection_code'] == projection_code and term['term_code'] == term_code), None)

        full_term_code = projection_code + term_code  # Da bi prikazali ceo kod projekcije

        if projection and term:
            if ticket_info[-1] == "sold":
                continue

        if projection and term:
            movie_name = projection['movie_name']
            start_time = projection['start_time']
            end_time = projection['end_time']
            ticket_price = projection['ticket_price']

            table_data.append([full_term_code, movie_name, seat, projection_date, start_time, end_time, purchase_date, "none", ticket_price])

    if table_data:
        headers = ["Term Code", "Movie", "Seat", "Projection Date", "Start Time", "End Time", "Purchase Date", "Seller", "Ticket Price"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    else:
        print("No reservations found for this user.")


def cancel_ticket_reservation(username, reserved_tickets, tickets, projection_terms):
    while True:
        print("Cancel Ticket Reservation Menu:")
        print("0. Exit")

        if username in reserved_tickets:
            user_tickets = reserved_tickets[username]
            if not user_tickets:
                print("No reservations found for this user.")
                return

            for index, ticket in enumerate(user_tickets, start=1):
                print(f"{index}. {ticket}")

            try:
                choice = int(input("Enter the number of the ticket you want to cancel: "))
                if choice == 0:
                    print("Exiting cancellation.")
                    return
                elif choice > len(user_tickets) or choice < 0:
                    print("Invalid ticket number. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            selected_ticket = user_tickets[choice - 1]  # Smanjili smo za 1 za pravi indeks

            print(selected_ticket)  # selected_ticket je u sustini string gde je kljuc username

            reserved_tickets[username].remove(selected_ticket)

            ticket_info = selected_ticket.split('|')
            projection_code = ticket_info[0][-6:-2]  # 1112AE idemo od pocetka do 4 karaktera
            term_code = ticket_info[0][-2:]
            full_code = projection_code + term_code
            date = ticket_info[1]
            seat = ticket_info[2]
            sale_date = ticket_info[3]
            status = ticket_info[-1]

            # ticket je recnik, a tickets je lista recnika
            for ticket in tickets:
                if ticket['term_id'] == full_code and ticket['term_date'] == date and ticket['seat_code'] == seat and \
                        ticket['sale_date'] == sale_date and ticket['status'] == status:
                    tickets.remove(ticket)
                    print(tickets)
                    print("Ticket removed from tickets !!!")
                    break

            # Oslobađanje mesta u matrici sedenja i brisanje iz rezervacija i karata
            ticket_info = selected_ticket.split('|')
            projection_code = ticket_info[0][-6:-2]  # 1112AE idemo od pocetka do 4 karaktera
            term_code = ticket_info[0][-2:]
            seat = ticket_info[2]

            for term in projection_terms:
                if term['projection_code'] == projection_code and term['term_code'] == term_code:
                    seat_row = int(seat[:-1]) - 1
                    seat_col = ord(seat[-1]) - ord('A')
                    term['seat_matrix'][seat_row][seat_col] = 'O'  # 'O' označava slobodno sedište

            print("Ticket reservation canceled successfully!")

            choice2 = input("Do you want to cancel more tickets? (yes/no): ").lower()
            if choice2 == "no":
                return
        else:
            print("No reservations found for this user.")
            return
