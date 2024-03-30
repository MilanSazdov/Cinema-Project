# Funkcija za ucitavanje postojecih prodavaca
import functionality
import menus
from tabulate import tabulate
from datetime import datetime, timedelta
from prettytable import PrettyTable

import registered_customer_functions


def load_sellers(file_name):
    sellers = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                parts_of_line = line.strip().split("|")
                seller = {
                    "username": parts_of_line[0],
                    "password": parts_of_line[1],
                    "name": parts_of_line[2],
                    "last_name": parts_of_line[3],
                    "role": parts_of_line[4]
                }
                sellers.append(seller)
    except FileNotFoundError:
        pass
    return sellers


def write_sellers_in_file(file_name, sellers):
    with open(file_name, "w") as file:
        for seller in sellers:
            line = f"{seller['username']}|{seller['password']}|{seller['name']}|{seller['last_name']}|{seller['role']}\n"
            file.write(line)


def reserve_tickets_seller(registered_customers, cinema_projections, projection_terms, tickets, reserved_tickets,
                           seller_user):
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
                        elif y == "yes":
                            continue
                        else:
                            print("Invalid input. Please try again.")
                            return
                    flag = 0  # da li je pronasao user u registrovanim korisnicima
                    while True:
                        choice_reg_or_unreg = int(
                            input("Enter 1 for registered users, 2 for unregistered users, or 0 to cancel: "))

                        if choice_reg_or_unreg == 0:
                            print("Exiting reservation.")
                            return
                        elif choice_reg_or_unreg == 1:
                            username = input("Enter customer's username: ")

                            # Proveravamo da li je username u registrovanim korisnicima
                            for customer in registered_customers:
                                if customer['username'] == username:
                                    flag = 1
                                    break

                            if flag == 1:
                                flag = 0
                                break
                            else:
                                print("User not found in registered customers.")
                                y = input("Do you want to continue? (yes/no): ").lower()
                                if y == "no":
                                    return
                                else:
                                    flag = 0
                                    continue

                        elif choice_reg_or_unreg == 2:
                            name = input("Enter customer's name: ")
                            last_name = input("Enter customer's last name: ")

                            if '|' in name or '|' in last_name:
                                print("Invalid characters '|' in name or last name. Please try again.")
                                continue
                            username = f"{name} {last_name}"
                            break

                        else:
                            print("Invalid choice. Please enter a valid option !!!")
                            continue

                    row = int(input("Enter the row number: ")) - 1
                    column = input("Enter the column letter: ").upper()

                    if row < 0 or row >= len(found_term['seat_matrix']) or ord(column) - ord('A') < 0 or ord(
                            column) - ord(
                            'A') >= len(found_term['seat_matrix'][0]):
                        print("Invalid seat selection. Please try again.")
                        continue

                    if found_term['seat_matrix'][row][ord(column) - ord('A')] == 'X':
                        print("Seat already taken. Please choose another seat.")
                        continue
                    # Ovde treba ažurirati matricu sedišta i dodati rezervaciju u listu i fajl
                    seat_label = f"{row + 1}{column}"
                    found_term['seat_matrix'][row][ord(column) - ord('A')] = 'X'
                    full_code = projection_code + term_code

                    projection = next((proj for proj in cinema_projections if proj['id'] == projection_code), None)
                    if projection:
                        date_string = found_term['date']
                        date_obj = datetime.strptime(date_string, '%d.%m.%Y')
                        term_day = date_obj.strftime('%A').lower()
                        print(date_obj)
                        if term_day == 'tuesday':
                            ticket_price = projection['ticket_price'] - 50
                        elif term_day in ['saturday', 'sunday']:
                            ticket_price = projection['ticket_price'] + 50
                        else:
                            ticket_price = projection['ticket_price']

                    else:
                        ticket_price = 'N/A'  # Ukoliko projekcija nije pronađena, cenu postavljamo na N/A

                    new_ticket = {
                        'username': username,
                        'term_id': full_code,
                        'term_date': found_term['date'],
                        'seat_code': seat_label,
                        'sale_date': date,
                        'seller_username': seller_user,
                        'ticket_price': ticket_price,
                        'status': "reserved"
                    }

                    tickets.append(new_ticket)

                    reservation_info = f"{projection_code}{term_code}|{found_term['date']}|{seat_label}|{date}|{seller_user}|{ticket_price}|reserved"
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
                    while True:
                        choice_reg_or_unreg = int(
                            input("Enter 1 for registered users, 2 for unregistered users, or 0 to cancel: "))

                        if choice_reg_or_unreg == 0:
                            print("Exiting reservation.")
                            return
                        elif choice_reg_or_unreg == 1:
                            username = input("Enter customer's username: ")
                            is_registered = any(customer['username'] == username for customer in registered_customers)
                            if not is_registered:
                                print("User not found in registered customers.")
                                y = input("Do you want to continue? (yes/no): ").lower()
                                if y == "no":
                                    return
                                else:
                                    continue
                            else:
                                break
                        elif choice_reg_or_unreg == 2:
                            name = input("Enter customer's name: ")
                            last_name = input("Enter customer's last name: ")

                            if '|' in name or '|' in last_name:
                                print("Invalid characters '|' in name or last name. Please try again.")
                                continue
                            username = f"{name} {last_name}"
                            break

                        else:
                            print("Invalid choice. Please enter a valid option !!!")
                            continue

                    row = int(input("Enter the row number: ")) - 1
                    column = input("Enter the column letter: ").upper()

                    if row < 0 or row >= len(found_term['seat_matrix']) or ord(column) - ord('A') < 0 or ord(
                            column) - ord(
                            'A') >= len(found_term['seat_matrix'][0]):
                        print("Invalid seat selection. Please try again.")
                        continue

                    if found_term['seat_matrix'][row][ord(column) - ord('A')] == 'X':
                        print("Seat already taken. Please choose another seat.")
                        continue

                    seat_label = f"{row + 1}{column}"
                    found_term['seat_matrix'][row][ord(column) - ord('A')] = 'X'
                    full_code = projection_code + term_code

                    projection = next((proj for proj in cinema_projections if proj['id'] == projection_code), None)
                    if projection:
                        date_string = found_term['date']
                        date_obj = datetime.strptime(date_string, '%d.%m.%Y')
                        term_day = date_obj.strftime('%A').lower()
                        if term_day == 'tuesday':
                            ticket_price = projection['ticket_price'] - 50
                        elif term_day in ['saturday', 'sunday']:
                            ticket_price = projection['ticket_price'] + 50
                        else:
                            ticket_price = projection['ticket_price']
                    else:
                        ticket_price = 'N/A'  # Ukoliko projekcija nije pronađena, cenu postavljamo na N/A

                    new_ticket = {
                        'username': username,
                        'term_id': full_code,
                        'term_date': found_term['date'],
                        'seat_code': seat_label,
                        'sale_date': date,
                        'seller_username': seller_user,
                        'ticket_price': ticket_price,
                        'status': "reserved"
                    }

                    tickets.append(new_ticket)

                    reservation_info = f"{projection_code}{term_code}|{found_term['date']}|{seat_label}|{date}|{seller_user}|{ticket_price}|reserved"
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


def display_reserved_tickets(cinema_projections, projection_terms, reserved_tickets, sold_tickets, tickets, registered_customers, movies):
    while True:
        menus.display_tickets_seller_menu()
        table_data = []
        try:
            choice = int(input("Enter your choice from menu: "))
            if choice == 0:
                print("Exiting ticket display ...")
                return
            elif choice == 1:
                term_code_input = input("Enter the Term Code: ")
                if len(term_code_input) != 6:
                    print("Invalid term code. Please enter a valid code !!!")
                    continue
                    # Prikaz svih rezervisanih karata
                for username, ticket_info in reserved_tickets.items():
                    for ticket in ticket_info:
                        if term_code_input in ticket:
                            projection_info = [projection for projection in cinema_projections if
                                               projection['id'] == term_code_input[:4]]
                            if projection_info:
                                projection_data = projection_info[0]
                                movie_name = projection_data['movie_name']
                                start_time = projection_data['start_time']
                                end_time = projection_data['end_time']
                                table_data.append([username, movie_name, start_time, end_time] + ticket.split('|'))

                    # Prikaz svih prodatih karata
                for username, ticket_info in sold_tickets.items():
                    for ticket in ticket_info:
                        if term_code_input in ticket:
                            projection_info = [projection for projection in cinema_projections if
                                               projection['id'] == term_code_input[:4]]
                            if projection_info:
                                projection_data = projection_info[0]
                                movie_name = projection_data['movie_name']
                                start_time = projection_data['start_time']
                                end_time = projection_data['end_time']
                                table_data.append([username, movie_name, start_time, end_time] + ticket.split('|'))

                headers = ["Username", "Movie Name", "Start Time", "End Time", "Term Code", "Term Date", "Seat Code",
                           "Purchase Date", "Seller", "Price", "Status"]
                print(tabulate(table_data, headers=headers, tablefmt="grid"))
            elif choice == 2:
                username = input("Enter the username to display their tickets: ")
                if username in reserved_tickets or username in sold_tickets:
                    table_data = []

                    if username in reserved_tickets:
                        for ticket in reserved_tickets[username]:
                            term_code = ticket[:4]
                            projection_info = next(
                                (projection for projection in cinema_projections if projection['id'] == term_code[:4]),
                                None)
                            if projection_info:
                                movie_name = projection_info['movie_name']
                                start_time = projection_info['start_time']
                                end_time = projection_info['end_time']
                                term_code_full = ticket[:6]
                                ticket_data = ticket.split('|')
                                term_date = ticket_data[1]
                                seat_code = ticket_data[2]
                                purchase_date = ticket_data[3]
                                seller_user = ticket_data[4]
                                price = ticket_data[5]
                                status = ticket_data[6]
                                table_data.append(
                                    [username, movie_name, start_time, end_time, term_code_full, term_date, seat_code,
                                     purchase_date, seller_user, price, status])

                    if username in sold_tickets:
                        for ticket in sold_tickets[username]:
                            term_code = ticket[:4]
                            projection_info = next(
                                (projection for projection in cinema_projections if projection['id'] == term_code[:4]),
                                None)
                            if projection_info:
                                movie_name = projection_info['movie_name']
                                start_time = projection_info['start_time']
                                end_time = projection_info['end_time']
                                term_code_full = ticket[:6]
                                ticket_data = ticket.split('|')
                                term_date = ticket_data[1]
                                seat_code = ticket_data[2]
                                purchase_date = ticket_data[3]
                                seller_user = ticket_data[4]
                                price = ticket_data[5]
                                status = ticket_data[6]
                                table_data.append(
                                    [username, movie_name, start_time, end_time, term_code_full, term_date, seat_code,
                                     purchase_date, seller_user, price, status])

                    headers = ["Username", "Movie Name", "Start Time", "End Time", "Term Code", "Term Date",
                               "Seat Code",
                               "Purchase Date", "Seller", "Price", "Status"]
                    print(tabulate(table_data, headers=headers, tablefmt="grid"))
                else:
                    print("There are no reserved tickets for this user... (or user not found)")
            elif choice == 3:
                functionality.display_all_tickets(tickets, cinema_projections)
            else:
                print("Invalid Input !!!")
                continue
        except ValueError:
            print("Invalid Input !!!")
            continue


def cancel_ticket_reservation_seller(reserved_tickets, sold_tickets, tickets, cinema_projections, projection_terms):
    while True:
        menus.cancel_ticket_reservation_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 0:
                print("Exiting cancellation.")
                return
            elif choice == 1:
                term_code_input = input("Enter the Term ID: ")
                term_tickets = []

                for username, user_tickets in reserved_tickets.items():
                    for ticket in user_tickets:
                        if term_code_input in ticket:
                            term_tickets.append([username] + ticket.split('|'))

                for username, user_tickets in sold_tickets.items():
                    for ticket in user_tickets:
                        if term_code_input in ticket:
                            term_tickets.append([username] + ticket.split('|'))

                if not term_tickets:
                    print("No tickets found for this Term ID.")
                    continue

                print("Tickets for the Term ID:")
                headers = ["Index", "Username", "Term ID", "Term Date", "Seat Code", "Sale Date", "Seller",
                           "Ticket Price", "Status"]
                table_data = []
                for index, ticket in enumerate(term_tickets, start=1):
                    table_data.append([index] + ticket)
                print(tabulate(table_data, headers=headers, tablefmt="grid"))

                try:
                    cancel_choice = int(input("Enter the number of the ticket you want to cancel: "))
                    if cancel_choice <= 0 or cancel_choice > len(term_tickets):
                        print("Invalid ticket number. Please try again.")
                        continue

                    selected_ticket = term_tickets[cancel_choice - 1]
                    term_id = selected_ticket[1]
                    date = selected_ticket[2]
                    seat = selected_ticket[3]
                    sale_date = selected_ticket[4]
                    seller_username = selected_ticket[5]
                    ticket_price = selected_ticket[6]
                    status = selected_ticket[-1]

                    for ticket in tickets:
                        if ticket['term_id'] == term_id and ticket['term_date'] == date and ticket[
                            'seat_code'] == seat and ticket['sale_date'] == sale_date and ticket['status'] == status:
                            tickets.remove(ticket)
                            break

                    selected_ticket_info = '|'.join(selected_ticket[1:])

                    if selected_ticket[0] in reserved_tickets:
                        if selected_ticket_info in reserved_tickets[selected_ticket[0]]:
                            reserved_tickets[selected_ticket[0]].remove(selected_ticket_info)
                    elif selected_ticket[0] in sold_tickets:
                        if selected_ticket_info in sold_tickets[selected_ticket[0]]:
                            sold_tickets[selected_ticket[0]].remove(selected_ticket_info)

                    for term in projection_terms:
                        if term['projection_code'] == term_id[-6:-2] and term['term_code'] == term_id[-2:]:
                            seat_row = int(seat[:-1]) - 1
                            seat_col = ord(seat[-1]) - ord('A')
                            term['seat_matrix'][seat_row][seat_col] = 'O'  # 'O' označava slobodno sedište

                    print("Ticket reservation canceled successfully!")

                    choice2 = input("Do you want to cancel more tickets? (yes/no): ").lower()
                    if choice2 == "no":
                        return
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    continue
            elif choice == 2:
                username = input("Enter the username to display their tickets: ")
                user_tickets = reserved_tickets.get(username, []) + sold_tickets.get(username, [])

                if not user_tickets:
                    print("No tickets found for this user.")
                    continue

                headers = ["Index", "Term Code", "Term Date", "Seat Code", "Sale Date", "Seller", "Ticket Price",
                           "Status"]
                table_data = []
                print(f"Tickets for User {username}:")
                for index, ticket in enumerate(user_tickets, start=1):
                    ticket_data = ticket.split('|')
                    table_data.append([index] + ticket_data)
                print(tabulate(table_data, headers=headers, tablefmt="grid"))
                try:
                    cancel_choice = int(input("Enter the number of the ticket you want to cancel: "))
                    if cancel_choice <= 0 or cancel_choice > len(user_tickets):
                        print("Invalid ticket number. Please try again.")
                        continue

                    selected_ticket = user_tickets[cancel_choice - 1]
                    ticket_info = selected_ticket.split('|')
                    term_id = ticket_info[0]
                    date = ticket_info[1]
                    seat = ticket_info[2]
                    sale_date = ticket_info[3]
                    seller_username = ticket_info[4]
                    ticket_price = ticket_info[5]
                    status = ticket_info[-1]

                    for ticket in tickets:
                        if ticket['term_id'] == term_id and ticket['term_date'] == date and ticket[
                            'seat_code'] == seat and ticket['sale_date'] == sale_date and ticket['status'] == status:
                            tickets.remove(ticket)
                            break

                    if selected_ticket in reserved_tickets.get(username, []):
                        reserved_tickets[username].remove(selected_ticket)
                    elif selected_ticket in sold_tickets.get(username, []):
                        sold_tickets[username].remove(selected_ticket)

                    for term in projection_terms:
                        if term['projection_code'] == term_id[-6:-2] and term['term_code'] == term_id[-2:]:
                            seat_row = int(seat[:-1]) - 1
                            seat_col = ord(seat[-1]) - ord('A')
                            term['seat_matrix'][seat_row][seat_col] = 'O'

                    print("Ticket reservation canceled successfully!")

                    choice2 = input("Do you want to cancel more tickets? (yes/no): ").lower()
                    if choice2 == "no":
                        return
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    continue
            else:
                print("Invalid choice. Please enter a valid option.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue


def sell_reserved_tickets(tickets, reserved_tickets, sold_tickets, seller_user, total_spent_per_user):
    while True:
        menus.sell_reserved_tickets_menu()

        choice = input("Enter choice from the menu: ")

        if choice == "0":
            print("Exiting sell reserved ticket menu ...")
            return
        elif choice == "1":
            term_id = input("Enter the Term ID: ")
            term_tickets = []
            for username, user_tickets in reserved_tickets.items():
                for ticket_info in user_tickets:
                    ticket_data = ticket_info.split('|')
                    print(ticket_info)
                    if term_id == ticket_data[0]:
                        ticket_data[5] = apply_discount(username, float(ticket_data[5]), total_spent_per_user)
                        ticket = {
                            'username': username,
                            'term_id': ticket_data[0],
                            'term_date': ticket_data[1],
                            'seat_code': ticket_data[2],
                            'sale_date': ticket_data[3],
                            'seller_username': ticket_data[4],
                            # Tek kasnije moramo da menjamo jer ako je korisnik sam rezervisao onda je none
                            'ticket_price': str(ticket_data[5]),
                            'status': ticket_data[6]
                        }
                        # print(ticket_data[6])
                        term_tickets.append(ticket)

            if not term_tickets:
                print("No reserved tickets found for this Term ID !!!")
                return

            print(f"Reserved tickets for Term ID {term_id}:")
            table_headers = ['Index', 'Username', 'Term ID', 'Term Date', 'Seat Code', 'Sale Date', 'Seller Username',
                             'Ticket Price', 'Status']
            table_data = []
            for index, ticket in enumerate(term_tickets, start=1):
                table_row = [index, ticket['username'], ticket['term_id'], ticket['term_date'], ticket['seat_code'],
                             ticket['sale_date'], ticket['seller_username'], ticket['ticket_price'], ticket['status']]
                table_data.append(table_row)

            print(tabulate(table_data, headers=table_headers, tablefmt="grid"))

            try:
                ticket_choice = int(input("Enter the number of the ticket you want to sell: "))
                if ticket_choice <= 0 or ticket_choice > len(term_tickets):
                    print("Invalid ticket number. Please try again.")
                    return

                selected_ticket = term_tickets[ticket_choice - 1]

                username = selected_ticket['username']

                # Pravimo string koji želimo da uklonimo iz liste rezervacija
                reservation_to_remove = '|'.join(
                    [selected_ticket['term_id'], selected_ticket['term_date'], selected_ticket['seat_code'],
                     selected_ticket['sale_date'], selected_ticket['seller_username'], selected_ticket['ticket_price'],
                     selected_ticket['status']])

                if reservation_to_remove in reserved_tickets[username]:
                    reserved_tickets[username].remove(reservation_to_remove)
                    selected_ticket['status'] = 'sold'
                    selected_ticket['seller_username'] = seller_user

                if username in sold_tickets:
                    sold_tickets[username].append('|'.join(
                        [selected_ticket['term_id'], selected_ticket['term_date'], selected_ticket['seat_code'],
                         selected_ticket['sale_date'], selected_ticket['seller_username'],
                         selected_ticket['ticket_price'], selected_ticket['status']]))

                else:
                    sold_tickets[username] = ['|'.join(
                        [selected_ticket['term_id'], selected_ticket['term_date'], selected_ticket['seat_code'],
                         selected_ticket['sale_date'], selected_ticket['seller_username'],
                         selected_ticket['ticket_price'], selected_ticket['status']])]

                for ticket in tickets:
                    if (
                            ticket['username'] == username
                            and ticket['term_id'] == selected_ticket['term_id']
                            and ticket['seat_code'] == selected_ticket['seat_code']  # Seat Code -> je jedinstven ...
                    ):
                        ticket['status'] = 'sold'

                print(f"Ticket sold successfully by {seller_user}!!!")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "2":
            username = input("Enter the username: ")
            user_reserved_tickets = reserved_tickets.get(username, [])

            if not user_reserved_tickets:
                print("No reserved tickets found for this username.")
                return
            print(f"Reserved tickets for username '{username}':")
            table_headers = ['Index', 'Term ID', 'Term Date', 'Seat Code', 'Sale Date', 'Seller Username',
                             'Ticket Price', 'Status']
            table_data = []
            for index, ticket_info in enumerate(user_reserved_tickets, start=1):
                ticket_data = ticket_info.split('|')
                table_row = [index, ticket_data[0], ticket_data[1], ticket_data[2], ticket_data[3], ticket_data[4],
                             ticket_data[5], ticket_data[6]]
                table_data.append(table_row)

            print(tabulate(table_data, headers=table_headers, tablefmt="grid"))

            try:
                ticket_choice = int(input("Enter the number of the ticket you want to sell: "))
                if ticket_choice <= 0 or ticket_choice > len(user_reserved_tickets):
                    print("Invalid ticket number. Please try again.")
                    return

                selected_ticket = user_reserved_tickets[ticket_choice - 1].split('|')

                reserved_tickets[username].remove('|'.join(selected_ticket))
                # ovaj deo nam treba samo zbog izmene karata, tickets => tu se nalaze sve karte, a to je lista recnika
                selected_ticket[5] = apply_discount(username, float(selected_ticket[5]), total_spent_per_user)
                ticket = {
                    'username': username,
                    'term_id': selected_ticket[0],
                    'term_date': selected_ticket[1],
                    'seat_code': selected_ticket[2],
                    'sale_date': selected_ticket[3],
                    'seller_username': seller_user,  # selected_ticket[4],
                    'ticket_price': str(selected_ticket[5]),
                    'status': selected_ticket[6]
                }

                for t in tickets:
                    if t['username'] == username and t['term_id'] == ticket['term_id']:
                        t['status'] = 'sold'
                # zato sto je sold tickets zapravo dictionary gde je username key a ostali podaci o karti string ...
                selected_ticket[6] = 'sold'

                if username in sold_tickets:
                    selected_ticket = [str(element) for element in selected_ticket]
                    sold_tickets[username].append('|'.join(selected_ticket))
                else:
                    selected_ticket = [str(element) for element in selected_ticket]
                    sold_tickets[username] = ['|'.join(selected_ticket)]

                print("Ticket sold successfully !!!")
                print(sold_tickets)
                print(reserved_tickets)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Invalid input. Please enter a valid number.")
            continue


def search_by_term_code(code, tickets):
    found_tickets = [ticket for ticket in tickets if ticket['term_id'] == code]
    return found_tickets


def search_by_date(date, projection_terms, tickets):
    found_terms = [term for term in projection_terms if term['date'] == date]
    found_tickets = [ticket for ticket in tickets if ticket['term_date'] == date]
    return found_terms, found_tickets


def search_by_status(reserved_tickets, sold_tickets, status):
    found_tickets = []
    if status == 'sold':
        found_tickets = sold_tickets
    elif status == 'reserved':
        found_tickets = reserved_tickets
    return found_tickets


def search_by_full_name(name, last_name, registered_customers, tickets):
    found_tickets = []
    for customer in registered_customers:
        if name in customer['name'] and last_name in customer['last_name']:
            for ticket in tickets:
                if ticket['username'] == customer['username']:
                    found_tickets.append(ticket)
    return found_tickets


def search_by_start_time(start_time, cinema_projections, tickets):
    found_tickets = []
    search_time = datetime.strptime(start_time, "%H:%M").time()

    for projection in cinema_projections:
        projection_start_time = datetime.strptime(projection['start_time'], "%H:%M").time()
        if projection_start_time >= search_time:
            for ticket in tickets:
                if ticket['term_id'][:-2] == projection['id']:
                    found_tickets.append(ticket)
    return found_tickets


def search_by_end_time(end_time, cinema_projections, tickets):
    found_tickets = []
    search_time = datetime.strptime(end_time, "%H:%M").time()

    for projection in cinema_projections:
        projection_end_time = datetime.strptime(projection['end_time'], "%H:%M").time()
        if projection_end_time <= search_time:
            for ticket in tickets:
                if ticket['term_id'][:-2] == projection['id']:
                    found_tickets.append(ticket)
    return found_tickets


def print_found_tickets(found_tickets):
    headers = ["Username", "Term Code", "Term Date", "Seat Code", "Sale Date", "Seller", "Price", "Status"]
    table_data = []

    for ticket in found_tickets:
        table_row = [ticket['username'], ticket['term_id'], ticket['term_date'], ticket['seat_code'],
                     ticket['sale_date'], ticket['seller_username'], ticket['ticket_price'], ticket['status']]
        table_data.append(table_row)

    print(tabulate(table_data, headers=headers, tablefmt="grid"))


# Funkcija za pretragu karata
def search_tickets(tickets, cinema_projections, projection_terms, registered_customers, reserved_tickets, sold_tickets):
    while True:
        menus.search_tickets_menu()
        choice = input("Enter choice from the menu: ")
        if choice == "0":
            print("Exiting Search ...")
            return
        elif choice == "1":
            term_code = input("Enter Term Code: ")
            found_tickets = search_by_term_code(term_code, tickets)
            if not found_tickets:
                print("There are no tickets for this code !!!")
                continue
            print(f"Tickets for given code {term_code}: ")
            print_found_tickets(found_tickets)
            continue
        elif choice == "2":
            name = input("Enter the Name: ")
            last_name = input("Enter the Last Name: ")
            found_tickets = search_by_full_name(name, last_name, registered_customers, tickets)
            if not found_tickets:
                print("There are no tickets for this user !!!")
                continue
            print(f"Tickets for {name} {last_name}: ")
            print_found_tickets(found_tickets)
            continue
        elif choice == "3":
            date = input("Enter the date (format: %d%d.%m%m.%Y%Y%Y%Y): ")
            found_terms, found_tickets = search_by_date(date, projection_terms, tickets)
            if not found_tickets:
                print("There are no tickets for this date !!!")
                continue
            print(f"Tickets for {date}: ")
            print_found_tickets(found_tickets)
            continue
        elif choice == "4":
            start_time = input("Enter the start time: %H:%M ")
            found_tickets = search_by_start_time(start_time, cinema_projections, tickets)
            if not found_tickets:
                print("There are no tickets for this start time !!!")
                continue
            print(f"Tickets for {start_time}: ")
            print_found_tickets(found_tickets)
            continue
        elif choice == "5":
            end_time = input("Enter the end time: %H:%M ")
            found_tickets = search_by_end_time(end_time, cinema_projections, tickets)
            if not found_tickets:
                print("There are no tickets for this end time !!!")
                continue
            print(f"Tickets for {end_time}: ")
            print_found_tickets(found_tickets)
            continue
        elif choice == "6":
            status = input("Enter status of tickets: (reserved, sold): ").lower()
            found_tickets = search_by_status(reserved_tickets, sold_tickets, status)
            if not found_tickets:
                print("There are no tickets for this status !!!")
                continue
            print(f"Tickets for {status}: ")
            headers = ["Username", "Term ID", "Term Date", "Seat Code", "Sale Date", "Seller", "Price", "Status"]
            table_data = []
            for username, user_tickets in found_tickets.items():
                for ticket_info in user_tickets:
                    ticket_data = ticket_info.split('|')
                    table_row = [username] + ticket_data
                    table_data.append(table_row)
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
            continue
        else:
            print("Invalid input. Try again !!!")
            continue


def find_ticket_by_username_and_seat(tickets, term_code, username, seat):
    return next(
        (ticket for ticket in tickets if ticket['term_id'] == term_code and ticket['username'] == username and
         ticket['seat_code'] == seat),
        None
    )


def find_ticket_by_full_name_and_seat(tickets, term_code, full_name, seat):
    return next(
        (ticket for ticket in tickets if ticket['term_id'] == term_code and ticket['username'] == full_name and
         ticket['seat_code'] == seat),
        None
    )

def update_ticket(tickets, registered_customers, projection_terms, cinema_projections, reserved_tickets, sold_tickets,
                  sellers, managers):
    term_code = input("Enter the Term Code: ")
    has_account = input("Do you have an account ? (yes/no): ").lower()
    found_ticket = None
    if has_account == "yes":
        username = input("Enter your username: ")
        seat = input("Enter your seat: ").upper()
        found = False
        found_ticket = find_ticket_by_username_and_seat(tickets, term_code, username, seat)
    elif has_account == "no":
        full_name = input("Enter the customer's full name (Name LastName): ")
        if " " not in full_name:
            print("Invalid format. Try again !!!")
            return
        else:
            seat = input("Enter your seat: ")
            found_ticket = find_ticket_by_full_name_and_seat(tickets, term_code, full_name, seat)
    else:
        print("Invalid input. Try again!!!")
        return
    if not found_ticket:
        print("Ticket not found for the given username or name and last name.")
        return

    print("Ticket found: ")
    headers = ["Username", "Term Code", "Term Date", "Seat", "Purchase Date", "Seller", "Price", "Status"]
    row = [str(found_ticket["username"]), str(found_ticket["term_id"]), str(found_ticket["term_date"]), str(found_ticket["seat_code"]),
           str(found_ticket["sale_date"]), str(found_ticket["seller_username"]), str(found_ticket["ticket_price"]),
           str(found_ticket["status"])]
    table = PrettyTable()
    table.field_names = headers
    table.add_row(row)
    print(table)
    seat_code_old = found_ticket['seat_code']

    matching_term = next(
        (term for term in projection_terms if term['projection_code'] + term['term_code'] == term_code), None)
    if not matching_term:
        print("Term not found !!!")
        return

    seat_matrix = matching_term['seat_matrix']

    menus.update_ticket_menu()
    choice = input("Enter choice from the menu: ")

    if choice == "0":
        print("Exiting update of ticket...")
        return
    elif choice == "1":
        projection_code = term_code[0:4]  # uzimamo prva 4 slova -> jer treba da ispisemo sve termine koje imaju taj kod
        matching_terms = [term for term in projection_terms if term['projection_code'] == projection_code]

        print("Available terms with the given code: ")

        term_data = [(term['projection_code'] + term['term_code'], term['date']) for term in matching_terms]
        table_headers = ["Index", "Term Code", "Date"]
        table_data = [(i + 1, term[0], term[1]) for i, term in enumerate(term_data)]

        print(tabulate(table_data, headers=table_headers, tablefmt="grid"))

        while True:

            change_term = int(input("Chose the new term index: ")) - 1

            selected_term = matching_terms[change_term]
            print("Selected Term: ")
            table_data = [
                ['Projection Code', 'Term Code', 'Date'],
                [selected_term['projection_code'], selected_term['term_code'], selected_term['date']]
            ]

            print(tabulate(table_data, headers="first-row", tablefmt="grid"))

            selected_term_full_code = selected_term['projection_code'] + selected_term['term_code']

            functionality.print_seat_matrix(selected_term)

            while True:

                if all(all(seat == 'X' for seat in row) for row in seat_matrix):
                    print("The hall is fully booked. You cannot choose a seat.")
                    break

                row = int(input("Enter the row number: ")) - 1
                column = input("Enter the column letter: ").upper()

                if row < 0 or row > len(selected_term['seat_matrix']) or ord(column) - ord('A') < 0 or ord(
                        column) - ord(
                        'A') > len(selected_term['seat_matrix'][0]):
                    raise ValueError("Invalid seat selection. Please try again.")

                if seat_matrix[row][ord(column) - ord('A')] == 'X':
                    raise ValueError("Seat already taken. Please choose another seat.")

                if found_ticket:
                    old_row, old_column = int(found_ticket['seat_code'][:-1]) - 1, found_ticket['seat_code'][-1]
                    seat_matrix[old_row][ord(old_column) - ord('A')] = 'O'

                # Ovde treba otici na novi termin i tu staviti X
                seat_label = f"{row + 1}{column}"
                selected_term['seat_matrix'][row][ord(column) - ord('A')] = 'X'
                print("Seat updated successfully !!!")

                for ticket in tickets:
                    if ticket['term_id'] == found_ticket['term_id'] and ticket['seat_code'] == seat_code_old:
                        ticket['term_id'] = selected_term_full_code
                        ticket['seat_code'] = seat_label
                        ticket['term_date'] = selected_term['date']
                        break

                reserved_tickets = functionality.update_reserved_tickets(tickets)
                sold_tickets = functionality.update_sold_tickets(tickets)
                break
            break
        return
    elif choice == "2":
        while True:
            has_account = input("Does the new user have an account? (yes/no): ").lower()

            if has_account == "yes":
                new_username = input("Enter the new username to transfer the ticket: ")
                if not functionality.is_username_unique(new_username, registered_customers, sellers, managers):
                    for ticket in tickets:
                        if ticket['term_id'] == found_ticket['term_id'] and ticket['seat_code'] == found_ticket[
                            'seat_code']:
                            ticket['username'] = new_username
                            break
                    reserved_tickets = functionality.update_reserved_tickets(tickets)
                    sold_tickets = functionality.update_sold_tickets(tickets)
                    print("Ticket transferred successfully to", new_username)
                    return
                else:
                    print("Invalid username. The specified account does not exist.")
                    continue
            elif has_account == "no":
                new_full_name = input("Enter the customer's full name (Name LastName): ").lower()
                if ' ' not in new_full_name:
                    print("Invalid input. Please enter the full name in this format Name space LastName.")
                    continue
                for ticket in tickets:
                    if ticket['term_id'] == found_ticket['term_id'] and ticket['seat_code'] == seat_code_old:
                        ticket['username'] = new_full_name
                        break
                reserved_tickets = functionality.update_reserved_tickets(tickets)
                sold_tickets = functionality.update_sold_tickets(tickets)
                print("Ticket transferred successfully to", new_full_name)
                return
            else:
                print("Invalid input. Try again.")
                continue
    elif choice == "3":
        while True:
            try:
                selected_term = None

                for term in projection_terms:
                    if term['projection_code'] + term['term_code'] == term_code:
                        selected_term = term
                        break

                if selected_term:
                    functionality.print_seat_matrix(selected_term)

                else:
                    print("Term not found.")
                    return

                if all(all(seat == 'X' for seat in row) for row in seat_matrix):
                    print("The hall is fully booked. You cannot choose a seat.")
                    break

                new_seat = input("Enter the new seat: (ex. 5A) ").upper()
                if len(new_seat) != 2 or not new_seat[0].isdigit() or not new_seat[1].isalpha():
                    print("Invalid seat format. Please enter in the format (e.g '2D').")
                    continue

                row = int(new_seat[:-1]) - 1
                column = ord(new_seat[-1]) - ord('A')

                if row < 0 or row >= len(seat_matrix) or column < 0 or column >= len(seat_matrix[0]):
                    print("Invalid seat !!! Please try again.")
                    continue

                if seat_matrix[row][column] == "X":
                    print("Seat already taken. Please choose another seat.")
                    continue

                old_row = int(found_ticket['seat_code'][:-1]) - 1
                old_column = ord(found_ticket['seat_code'][-1]) - ord('A')

                seat_matrix[row][column] = 'X'
                seat_matrix[old_row][old_column] = 'O'

                for ticket in tickets:
                    if ticket['term_id'] == found_ticket['term_id'] and ticket['seat_code'] == seat_code_old:
                        ticket['seat_code'] = new_seat
                        break

                reserved_tickets = functionality.update_reserved_tickets(tickets)
                sold_tickets = functionality.update_sold_tickets(tickets)

                print("Seat updated successfully !!!")
                break
            except ValueError:
                print("Invalid input. Please try again.")
                continue

        return
    else:
        print("Invalid input!!! Please try again !!!")
        return


def direct_ticket_sales(reserved_tickets, sold_tickets, tickets, cinema_projections, projection_terms, seller_user,
                        total_spent_per_user, registered_customers):
    while True:
        menus.direct_ticket_sales_menu()

        try:
            choice = int(input("Enter your choice: "))
            if choice == 0:
                print("Exiting cancellation.")
                return
            # Namesteno, radi perfektno, testirano !!!
            elif choice == 1:
                functionality.search_for_terms_of_cinema_projections(cinema_projections, projection_terms)
                term_code_input = input("Enter the Term ID: ")
                term_tickets = []

                selected_term = None
                for term in projection_terms:
                    if term['projection_code'] + term['term_code'] == term_code_input:
                        selected_term = term
                        break
                if not selected_term:
                    print("Term ID not found. Please try again.")
                    continue

                print("Selected Term: ")
                print(f"Projection Code: {selected_term['projection_code']}")
                print(f"Term Code: {selected_term['term_code']}")
                print(f"Date: {selected_term['date']}")

                while True:
                    seat_matrix = selected_term['seat_matrix']
                    '''
                    headers = [''] + [chr(65 + i) for i in range(len(seat_matrix[0]))]
                    table = [[i + 1] + row for i, row in enumerate(seat_matrix)]
                    print(tabulate(table, headers=headers, tablefmt="grid"))'''
                    functionality.print_seat_matrix(selected_term)

                    username = input("Enter username or full name (Name LastName): ")
                    if '|' in username:
                        print("Invalid character in username. Please try again.")
                        continue

                    found = False
                    if ' ' not in username:
                        for customer in registered_customers:
                            if customer['username'].lower() == username.lower():
                                found = True
                                break

                    if " " in username:
                        found = True

                    if not found:
                        print("Username does not exists !!!")
                        continue

                    row = int(input("Enter the row number: ")) - 1
                    column = input("Enter the column letter: ").upper()

                    if row < 0 or row >= len(seat_matrix) or ord(column) - ord('A') < 0 or ord(column) - ord(
                            'A') >= len(seat_matrix[0]):
                        print("Invalid seat selection. Please try again.")
                        continue

                    if seat_matrix[row][ord(column) - ord('A')] == 'X':
                        print("Seat already taken. Please choose another seat.")
                        continue

                    seat_code = f"{row + 1}{column}"
                    sale_date = datetime.today().strftime("%d.%m.%Y")

                    ticket_price = 100
                    for projection in cinema_projections:
                        if term_code_input.startswith(projection['id']):
                            date_string = selected_term['date']
                            date_obj = datetime.strptime(date_string, '%d.%m.%Y')
                            term_day = date_obj.strftime('%A').lower()
                            if term_day == 'tuesday':
                                ticket_price = projection['ticket_price'] - 50
                                break
                            elif term_day in ['saturday', 'sunday']:
                                ticket_price = projection['ticket_price'] + 50
                                break
                            else:
                                ticket_price = projection['ticket_price']
                                break

                    ticket_price = str(apply_discount(username, float(ticket_price), total_spent_per_user))

                    new_ticket = {
                        'username': username,
                        'term_id': term_code_input,
                        'term_date': selected_term['date'],
                        'seat_code': seat_code,
                        'sale_date': sale_date,
                        'seller_username': seller_user,
                        'ticket_price': ticket_price,
                        'status': 'sold'
                    }

                    print(new_ticket)

                    tickets.append(new_ticket)

                    # updejtovanje jedne prodane karte
                    sold_tickets = functionality.update_sold_tickets_one(sold_tickets, new_ticket)

                    seat_matrix[row][ord(column) - ord('A')] = 'X'
                    print("Ticket sold successfully!")

                    while True:
                        choice2 = input("Do you want to sell more tickets ? (yes/no): ").lower()
                        if choice2 != "yes" and choice2 != "no":
                            print("Invalid input. Please try again.")
                            continue
                        break
                    if choice2 == "no":
                        return

            # Ovaj deo radi kako treba -> testirano
            elif choice == 2:
                term_code_input = input("Enter the Term ID: ")
                term_tickets = []

                selected_term = None
                for term in projection_terms:
                    if term['projection_code'] + term['term_code'] == term_code_input:
                        selected_term = term
                        break
                if not selected_term:
                    print("Term ID not found. Please try again.")
                    continue

                print("Selected Term: ")
                print(f"Projection Code: {selected_term['projection_code']}")
                print(f"Term Code: {selected_term['term_code']}")
                print(f"Date: {selected_term['date']}")

                while True:

                    seat_matrix = selected_term['seat_matrix']
                    '''
                    headers = [''] + [chr(65 + i) for i in range(len(seat_matrix[0]))]
                    table = [[i + 1] + row for i, row in enumerate(seat_matrix)]
                    print(tabulate(table, headers=headers, tablefmt="grid"))'''
                    functionality.print_seat_matrix(selected_term)

                    username = input("Enter username or full name (Name LastName): ")
                    if '|' in username:
                        print("Invalid character in username. Please try again.")
                        continue

                    found = False
                    if ' ' not in username:
                        for customer in registered_customers:
                            if customer['username'].lower() == username.lower():
                                found = True
                                break

                    if " " in username:
                        found = True

                    if not found:
                        print("Username does not exists !!!")
                        continue

                    row = int(input("Enter the row number: ")) - 1
                    column = input("Enter the column letter: ").upper()

                    if row < 0 or row >= len(seat_matrix) or ord(column) - ord('A') < 0 or ord(column) - ord(
                            'A') >= len(seat_matrix[0]):
                        print("Invalid seat selection. Please try again.")
                        continue

                    if seat_matrix[row][ord(column) - ord('A')] == 'X':
                        print("Seat already taken. Please choose another seat.")
                        continue

                    seat_code = f"{row + 1}{column}"
                    sale_date = datetime.today().strftime("%d.%m.%Y")

                    ticket_price = 100
                    for projection in cinema_projections:
                        if term_code_input.startswith(projection['id']):
                            date_string = selected_term['date']
                            date_obj = datetime.strptime(date_string, '%d.%m.%Y')
                            term_day = date_obj.strftime('%A').lower()
                            if term_day == 'tuesday':
                                ticket_price = projection['ticket_price'] - 50
                                break
                            elif term_day in ['saturday', 'sunday']:
                                ticket_price = projection['ticket_price'] + 50
                                break
                            else:
                                ticket_price = projection['ticket_price']
                                break

                    ticket_price = str(apply_discount(username, float(ticket_price), total_spent_per_user))

                    new_ticket = {
                        'username': username,
                        'term_id': term_code_input,
                        'term_date': selected_term['date'],
                        'seat_code': seat_code,
                        'sale_date': sale_date,
                        'seller_username': seller_user,
                        'ticket_price': ticket_price,
                        'status': 'sold'
                    }

                    print(new_ticket)

                    tickets.append(new_ticket)

                    # updejtovanje jedne prodane karte
                    sold_tickets = functionality.update_sold_tickets_one(sold_tickets, new_ticket)

                    seat_matrix[row][ord(column) - ord('A')] = 'X'
                    print("Ticket sold successfully!")

                    while True:
                        choice2 = input("Do you want to sell more tickets ? (yes/no): ").lower()
                        if choice2 != "yes" and choice2 != "no":
                            print("Invalid input. Please try again.")
                            continue
                        break
                    if choice2 == "no":
                        return

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue


# Funkcija za ukidanje rezervacije 30 minuta pre pocetka projekcije ili ako je projekcija vec pocela a korisnik zaboravio ...
# 19. Funkcionalnost ...
def cancel_unclaimed_reservations(reserved_tickets, tickets, cinema_projections, projection_terms):
    current_date = datetime.now().strftime("%d.%m.%Y")
    current_time = datetime.now().strftime("%H:%M")

    for username, user_tickets in reserved_tickets.items():
        tickets_to_remove = []

        for ticket_info in user_tickets:
            ticket_data = ticket_info.split('|')
            term_id = ticket_data[0]
            term_date = ticket_data[1]
            projection_date = None

            for term in projection_terms:
                if term['date'] == current_date and term['projection_code'] + term['term_code'] == term_id:
                    projection_id = term_id[:-2]
                    for projection in cinema_projections:
                        if projection['id'] == projection_id:

                            projection_date = datetime.strptime(term['date'], "%d.%m.%Y")
                            projection_time = datetime.strptime(projection['start_time'], "%H:%M")
                            projection_datetime = datetime.combine(projection_date, projection_time.time())

                            if projection_datetime <= datetime.now():
                                tickets_to_remove.append((term_id, term_date, ticket_data[2]))

                            time_difference = (projection_datetime - datetime.now()).seconds // 60

                            if 0 <= time_difference <= 30:
                                tickets_to_remove.append((term_id, term_date, ticket_data[2]))

        for ticket_to_remove in tickets_to_remove:
            term_id, term_date, seat_code = ticket_to_remove
            for t_info in reserved_tickets[username]:
                t_data = t_info.split('|')
                if t_data[0] == term_id and t_data[1] == term_date and t_data[2] == seat_code:
                    reserved_tickets[username].remove(t_info)

                    for ticket in tickets:
                        if (ticket['term_id'] == term_id and ticket['term_date'] == term_date and
                                ticket['seat_code'] == seat_code and ticket['status'] == 'reserved'):
                            tickets.remove(ticket)

                    print(f"Reservation for user {username} has been automatically canceled due to non-claiming.")


# Funkcija koja racuna koliko je svaki registrovani korisnik potrosio para
def calculate_total_spent(tickets, registered_customers, total_spent_per_user):
    for ticket in tickets:
        if ticket['username'] in [customer['username'] for customer in registered_customers]:
            if ticket['status'] == "sold":
                username = ticket['username']
                ticket_price = float(ticket['ticket_price'])
                total_spent_per_user[username] = total_spent_per_user.get(username, 0) + ticket_price

    print("Calculated customer consumption !!!")


def apply_discount(username, ticket_price, total_spent_per_user):
    total_spent = total_spent_per_user.get(username, 0)
    if total_spent > 5000:
        ticket_price *= 0.9
        print("Thank you for being our loyal customer !!! Discount: 10% ")
    return ticket_price


def reset_total_spent_per_user(total_spent_per_user):
    total_spent_per_user = {}
    return total_spent_per_user


def load_sold_tickets_by_sellers(filename):
    sold_tickets_by_sellers = {}

    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        seller_username, ticket_info = line.strip().split('|', 1)
        if seller_username in sold_tickets_by_sellers:
            sold_tickets_by_sellers[seller_username].append(ticket_info)
        else:
            sold_tickets_by_sellers[seller_username] = [ticket_info]

    return sold_tickets_by_sellers
