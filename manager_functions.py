import menus
import functionality
from tabulate import tabulate
from datetime import datetime, timedelta


# Funkcija za ucitavanje postojecih menadzera
def load_managers(file_name):
    managers = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                parts_of_line = line.strip().split("|")
                manager = {
                    "username": parts_of_line[0],
                    "password": parts_of_line[1],
                    "name": parts_of_line[2],
                    "last_name": parts_of_line[3],
                    "role": parts_of_line[4]
                }
                managers.append(manager)
    except FileNotFoundError:
        pass
    return managers


def write_managers_in_file(file_name, managers):
    with open(file_name, "w") as file:
        for manager in managers:
            line = f"{manager['username']}|{manager['password']}|{manager['name']}|{manager['last_name']}|{manager['role']}\n"
            file.write(line)


# Funkcija koja pise filmove u fajl -> radi kako treba ...
def write_movies_to_file(movies, file_name):
    with open(file_name, 'w') as file:
        for movie in movies:
            if isinstance(movie['main_roles'], list):
                main_roles_formatted = ','.join(movie['main_roles'])
            else:
                main_roles_formatted = movie['main_roles']
            file.write(
                f"{movie['name']}|{movie['genre']}|{movie['duration']}|{movie['director']}|{main_roles_formatted}|{movie['country_origin']}|{movie['production_year']}|{movie['short_description']}\n")


def registration_of_seller_or_manager(registered_customers, sellers, managers):
    while True:
        new_username = input("Enter new username: ")
        if functionality.is_username_unique(new_username, registered_customers, sellers, managers):
            if not new_username.strip() or '|' in new_username or " " in new_username:
                print("Username cannot be empty or contain the '|' character. Please enter a new username !!!")
                continue
            else:
                break
        else:
            print("Username already exists. Please enter a new username !!!")
            continue

    while True:
        new_password = input("Enter password: ")
        if functionality.check_password(new_password) and '|' not in new_password:
            break
        else:
            if new_password.strip() == '' or '|' in new_password:
                print("Password cannot be empty or contain the '|' character. Please enter a new password !!!")
            else:
                print("The password does not meet the requirements. Enter a new password !!!")
            continue

    while True:
        new_name = input("Enter name: ")
        if new_name.strip() == '' or '|' in new_name:
            print("Name cannot contain the '|' character or be empty. Please enter a new name !!!")
            continue
        else:
            break

    while True:
        new_last_name = input("Enter last name: ")
        if new_last_name.strip() == '' or '|' in new_last_name:
            print("Last name cannot contain the '|' character or be empty. Please enter a new last name !!!")
            continue
        else:
            break

    while True:
        print("Enter 1. to make seller: ")
        print("Enter 2. to make manager: ")
        try:
            option = int(input("Enter option from the menu: "))
            if option == 1:
                role = "seller"
                break
            elif option == 2:
                role = "manager"
                break
            else:
                print("\n\nYou entered an incorrect number!!!\n")
                decision = input("Do you want to continue? (yes/no): ").lower()
                if decision == 'no':
                    return
        except ValueError:
            print("\n\nInvalid input! Please enter a number.\n")
            decision = input("Do you want to continue? (yes/no): ").lower()
            if decision == 'no':
                return

    new_user = {
        "username": new_username,
        "password": new_password,
        "name": new_name,
        "last_name": new_last_name,
        "role": role
    }

    if role == "seller":
        sellers.append(new_user)
        file_name = "sellers.txt"
        # upis u file
    elif role == "manager":
        managers.append(new_user)
        file_name = "managers.txt"
        # upis u file

    with open(file_name, "a") as file:
        new_line = f"{new_username}|{new_password}|{new_name}|{new_last_name}|{role}\n"
        file.write(new_line)

    print(f"You have successfully added a new {role} !")


# Funkcija za dodavanje novog filma ...
def add_new_movie(movies):
    new_movie = {}

    while True:
        flag = 0
        new_name = input("Enter movie name: ")
        if '|' in new_name or not new_name.strip():
            print("Movie name cannot contain '|' or be empty. Please enter a valid movie name.")
        else:
            for movie in movies:
                if movie['name'] == new_name:
                    print("Movie is already in cinema !!! Add new one.")
                    flag = 1
                    break
            if flag == 1:
                continue
            else:
                new_movie["name"] = new_name
            break

    while True:
        new_genre = input("Enter movie genre: ")
        if '|' in new_genre or not new_genre.strip():
            print("Genre cannot contain '|' or be empty. Please enter a valid genre.")
        else:
            new_movie["genre"] = new_genre
            break

    while True:
        try:
            new_duration = int(input("Enter movie duration (in minutes): "))
            if new_duration < 0 or new_duration > 600:
                print("Invalid input. Duration should be between 0 and 600 minutes.")
            else:
                new_movie["duration"] = new_duration
                break
        except ValueError:
            print("Invalid input. Please enter a number for duration.")

    while True:
        new_director = input("Enter movie director: ")
        if '|' in new_director or not new_director.strip():
            print("Movie Director cannot contain '|' or be empty. Please enter a valid movie director.")
        else:
            new_movie["director"] = new_director
            break

    while True:
        new_main_roles = input("Enter main roles separated by commas: ")
        if '|' in new_main_roles:
            print("Character '|' is not allowed. Please enter again.")
            continue
        if ',' in new_main_roles and new_main_roles.count(',') < 1:
            print("Please enter at least one main role or remove the comma.")
            continue
            # pravimo listu koju razdvajamo po , => jer je main_roles zapravo lista u samom recniku movie
        main_roles_list = [role.strip() for role in new_main_roles.split(',')]
        new_movie['main_roles'] = main_roles_list
        break

    while True:
        new_country_origin = input("Enter country origin: ")
        if '|' in new_country_origin or not new_country_origin.strip():
            print("Country origin cannot contain '|' or be empty. Please enter a valid country origin.")
        else:
            new_movie["country_origin"] = new_country_origin
            break

    while True:
        try:
            new_production_year = int(input("Enter production year: "))
            if new_production_year < 1800 or new_production_year > 2023:
                print("Invalid input. Please enter a production year between 1800 and 2023.")
            else:
                new_movie["production_year"] = new_production_year
                break
        except ValueError:
            print("Invalid input. Please enter a valid production year.")

    while True:
        new_short_description = input("Enter a short description (up to 100 characters): ")
        if '|' in new_short_description:
            print("Short description cannot contain '|'. Please enter a different description.")
        elif len(new_short_description) == 0:
            print("Short description cannot be empty. Please enter a description.")
        elif len(new_short_description) > 100:
            print("Short description cannot exceed 100 characters. Please enter a shorter description.")
        else:
            new_movie["short_description"] = new_short_description
            break

    movies.append(new_movie)
    write_movies_to_file(movies, "movies.txt")
    print(f"Movie '{new_name}' added successfully!")
    return movies


def display_seating_arrangement(cinema_projections, projection_terms):
    for term in projection_terms:
        projection_code = term['projection_code']
        term_code = term['term_code']
        date = term['date']

        print(f"Projection Code: {projection_code}, Term Code: {term_code}, Date: {date}")

        seat_matrix = term['seat_matrix']
        headers = [''] + [chr(65 + i) for i in range(len(seat_matrix[0]))]
        table = [[i + 1] + row for i, row in enumerate(seat_matrix)]
        print(tabulate(table, headers=headers, tablefmt="grid"))
        print()


# Izvestaj A - kompletno
def display_sold_tickets_for_date(sold_tickets, manager_username):
    while True:
        try:
            date_str = input("Enter the date for which you want to see sold tickets: (%d%d.%m%m.%Y%Y%Y%Y): ")
            date = datetime.strptime(date_str, "%d.%m.%Y")
            break  # Prekidamo ako je dobar format
        except ValueError:
            print("Invalid input. Please try again.")

    sold_tickets_for_date = []

    for tickets in sold_tickets.values():
        for ticket in tickets:
            ticket_info = ticket.split('|')
            sale_date = datetime.strptime(ticket_info[3], "%d.%m.%Y")
            if sale_date.date() == date.date():
                sold_tickets_for_date.append(ticket_info[0:])

    if not sold_tickets_for_date:
        print(f"No sold tickets found for the date: {date_str}")
        return
    print(f"Sold tickets for the date: {date_str}")
    headers = ["Term Code", "Term Date", "Seat Code", "Sale Date", "Seller", "Price", "Status"]
    print(tabulate(sold_tickets_for_date, headers=headers, tablefmt="grid"))

    while True:
        choice = input("Save this report to a file? (yes/no): ").lower()
        if choice == "yes":
            filename = "report_a.txt"
            with open(filename, "a") as file:
                file.write(f"Report by {manager_username} for date: {date_str}\n")
                file.write(tabulate(sold_tickets_for_date, headers=headers, tablefmt="grid"))
                file.write("\n\n")
            print(f"Report saved to '{filename}'")
            break
        elif choice == "no":
            break
        else:
            print("Please enter 'yes' or 'no'.")
            continue
    return


# Izvestaj B - kompletno
def display_sold_tickets_for_term_date(cinema_projections, projection_terms, sold_tickets, manager_username):
    while True:
        try:
            date_str = input("Enter the date for which you want to see sold tickets: (%d%d.%m%m.%Y%Y%Y%Y): ")
            date = datetime.strptime(date_str, "%d.%m.%Y")
            break  # Prekidamo ako je dobar format
        except ValueError:
            print("Invalid input. Please try again.")

    sold_tickets_for_date = []

    for tickets in sold_tickets.values():
        for ticket in tickets:
            ticket_info = ticket.split('|')
            term_date = datetime.strptime(ticket_info[1], "%d.%m.%Y")
            if term_date.date() == date.date():
                sold_tickets_for_date.append(ticket_info[0:])

    if not sold_tickets_for_date:
        print(f"No sold tickets found for the date: {date_str}")
        return
    print(f"Sold tickets for the date: {date_str}")
    headers = ["Term Code", "Term Date", "Seat Code", "Sale Date", "Seller", "Price", "Status"]
    print(tabulate(sold_tickets_for_date, headers=headers, tablefmt="grid"))

    while True:
        choice = input("Save this report to a file? (yes/no): ").lower()
        if choice == "yes":
            filename = "report_b.txt"
            with open(filename, "a") as file:
                file.write(f"Report by {manager_username} for date: {date_str}\n")
                file.write(tabulate(sold_tickets_for_date, headers=headers, tablefmt="grid"))
                file.write("\n\n")
            print(f"Report saved to '{filename}'")
            break
        elif choice == "no":
            break
        else:
            print("Please enter 'yes' or 'no'.")
            continue

    return


# Izvestaj C - kompletno
def display_sold_tickets_for_date_and_seller(tickets, manager_username):
    while True:
        try:
            date_str = input("Enter the sale date for which you want to see sold tickets (DD.MM.YYYY): ")
            sale_date = datetime.strptime(date_str, "%d.%m.%Y")
            break  # Prekidamo ako je dobar format datuma
        except ValueError:
            print("Invalid date format. Please try again.")

    seller_username = input("Enter the seller's username: ")

    headers = ['Username', 'Term ID', 'Term Date', 'Seat Code', 'Sale Date', 'Seller', 'Price', 'Status']
    table_data = []

    for ticket in tickets:
        ticket_sale_date = datetime.strptime(ticket['sale_date'], "%d.%m.%Y")
        if ticket['seller_username'] == seller_username and ticket_sale_date == sale_date:
            ticket_data = [
                ticket['username'],
                ticket['term_id'],
                ticket['term_date'],
                ticket['seat_code'],
                ticket['sale_date'],
                ticket['seller_username'],
                ticket['ticket_price'],
                ticket['status']
            ]
            table_data.append(ticket_data)

    if not table_data:
        print(f"No sold tickets found for seller: {seller_username} on this date: {date_str}.")
        return
    else:
        # print(table_data)
        print(f"Tickets that were sold by: {seller_username} on date: {date_str}")
        print(tabulate(table_data, headers=headers, tablefmt="pretty"))

        while True:
            choice = input("Save this report to a file? (yes/no): ").lower()
            if choice == "yes":
                filename = "report_c.txt"
                with open(filename, "a") as file:
                    file.write(
                        f"Report by {manager_username} for tickets sold by {seller_username} on date: {date_str}\n")
                    file.write(tabulate(table_data, headers=headers, tablefmt="pretty"))
                    file.write("\n\n")
                print(f"Report saved to '{filename}'")
                break
            elif choice == "no":
                break
            else:
                print("Please enter 'yes' or 'no'.")
                continue

    return


# Izvestaj D -> Ukupan broj i ukupna cena prodatih karata za izabran dan (u nedelji) prodaje -> kompletno
def calculate_sales_for_sell_day_week(tickets, manager_username):
    while True:
        try:
            day_of_week = input("Enter the day you want to search for number of tickets and total sales: ").lower()

            if day_of_week not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
                print("Invalid input. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please try again.")

    total_sales = 0
    counter = 0

    for ticket in tickets:
        sale_date = datetime.strptime(ticket['sale_date'], "%d.%m.%Y")  # Pretvaramo u datum
        if sale_date.strftime("%A").lower() == day_of_week and ticket[
            'status'] == "sold":  # Pretvaramo datum u dan i gledamo da li je sold
            total_sales += float(ticket['ticket_price'])
            counter += 1

    print(f"Total number of tickets sold on {day_of_week}: {counter}")
    print(f"Total sales on {day_of_week}: {total_sales}")

    while True:
        choice = input("Save this report to a file? (yes/no): ").lower()
        if choice == "yes":
            filename = "report_d.txt"
            with open(filename, "a") as file:
                file.write(f"Report by {manager_username} for tickets sold on {day_of_week}\n")
                file.write(f"Total number of tickets sold: {counter}\n")
                file.write(f"Total sales: {total_sales}\n")
                file.write("\n\n")
            print(f"Report saved to '{filename}'")
            break
        elif choice == "no":
            break
        else:
            print("Please enter 'yes' or 'no'.")
            continue

    return


# Izvestaj E -> Ukupan broj i ukupna cena prodatih karata za izabran dan (u nedelji) održavanja projekcije -> kompletno
def calculate_sales_for_term_day_week(tickets, manager_username):
    while True:
        try:
            day_of_week = input("Enter the day you want to search for number of tickets and total sales: ").lower()

            if day_of_week not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
                print("Invalid input. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please try again.")

    total_sales = 0
    counter = 0

    for ticket in tickets:
        term_date = datetime.strptime(ticket['term_date'], "%d.%m.%Y")
        if term_date.strftime("%A").lower() == day_of_week and ticket['status'] == "sold":
            total_sales += float(ticket['ticket_price'])
            counter += 1

    print(f"Total number of tickets sold for events on {day_of_week.capitalize()}: {counter}")
    print(f"Total sales for events on {day_of_week.capitalize()}: {total_sales}")

    while True:
        choice = input("Save this report to a file? (yes/no): ").lower()
        if choice == "yes":
            filename = "report_e.txt"
            with open(filename, "a") as file:
                file.write(f"Report by {manager_username} for events on {day_of_week.capitalize()}:\n")
                file.write(f"Total number of tickets sold: {counter}\n")
                file.write(f"Total sales: {total_sales}\n")
                file.write("\n\n")
            print(f"Report saved to '{filename}'")
            break
        elif choice == "no":
            break
        else:
            print("Please enter 'yes' or 'no'.")
            continue

    return


# Izvestaj G -> Ukupan broj i ukupna cena prodatih karata za izabran dan prodaje i odabranog prodavca -> kompletno
def calculate_sales_for_sell_day_and_seller(tickets, sellers, manager_username):
    while True:
        try:
            day_of_week = input(
                "Enter the day of the week you want to search for number of tickets and total sales: ").lower()

            if day_of_week not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
                print("Invalid input. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please try again.")

    seller_username = input("Enter the seller's username: ")

    seller_exists = any(seller['username'] == seller_username for seller in sellers)

    if not seller_exists:
        print("Seller username does not exists.")
        return

    total_sales = 0
    counter = 0

    for ticket in tickets:
        ticket_sale_date = datetime.strptime(ticket['sale_date'], "%d.%m.%Y")
        sale_day_of_week = ticket_sale_date.strftime('%A').lower()
        if sale_day_of_week == day_of_week and ticket['seller_username'] == seller_username and ticket[
            'status'] == 'sold':
            total_sales += float(ticket['ticket_price'])
            counter += 1

    if counter == 0:
        print(f"No sold tickets found for seller: {seller_username} on {day_of_week.capitalize()}.")
    else:
        print(f"Total number of tickets sold by {seller_username} on {day_of_week.capitalize()}: {counter}")
        print(f"Total sales by {seller_username} on {day_of_week.capitalize()}: {total_sales}")
        while True:
            choice = input("Save this report to a file? (yes/no): ").lower()
            if choice == "yes":
                filename = "report_g.txt"
                with open(filename, "a") as file:
                    file.write(
                        f"Report by {manager_username} for {day_of_week.capitalize()} sales by {seller_username}:\n")
                    file.write(f"Total tickets sold: {counter}\n")
                    file.write(f"Total sales: {total_sales}\n")
                    file.write("\n\n")
                print(f"Report saved to '{filename}'")
                break
            elif choice == "no":
                break
            else:
                print("Please enter 'yes' or 'no'.")
                continue

    return


# Izvestaj F -> Ukupna cena prodatih karata za zadati film u svim projekcijama -> kompletno
def calculate_total_sales_for_movie(cinema_projections, tickets, manager_username):
    print("Movies available:")
    for index, movie in enumerate(cinema_projections, start=1):
        print(f"{index}. {movie['movie_name']}")

    while True:
        try:
            choice = input("Enter the number of the movie to calculate total sales (or 'exit' to cancel): ")
            if choice.lower() == "exit":
                print("Operation canceled.")
                return

            choice = int(choice)
            if choice < 1 or choice > len(cinema_projections):
                print("Please enter a valid movie number.")
            else:
                chosen_movie = cinema_projections[choice - 1]['movie_name']
                break
        except ValueError:
            print("Invalid input. Please enter a valid movie number or 'exit' to cancel.")

    total_sales = 0

    for ticket in tickets:
        for projection in cinema_projections:
            if ticket['term_id'][:4] == projection['id'] and projection['movie_name'] == chosen_movie and ticket[
                'status'] == 'sold':
                total_sales += float(ticket['ticket_price'])

    print(f"Total sales for the movie '{chosen_movie}': {total_sales}")

    while True:
        choice = input("Save this report to a file? (yes/no): ").lower()
        if choice == "yes":
            filename = "report_f.txt"
            with open(filename, "a") as file:
                file.write(f"Report by {manager_username} for movie '{chosen_movie}':\n")
                file.write(f"Total sales: {total_sales}\n")
                file.write("\n\n")
            print(f"Report saved to '{filename}'")
            break
        elif choice == "no":
            break
        else:
            print("Please enter 'yes' or 'no'.")
            continue

    return


# Izvestaj H -> Ukupan broj i ukupna cena prodatih karata po prodavcima (za svakog prodavca) u poslednjih 30 dana -> kompletno
def display_sales_for_sellers_last_30_days(tickets, manager_username):
    today = datetime.now()
    thirty_days_ago = today - timedelta(days=30)

    # Inicijalizujemo rečnik za broj prodatih karata i ukupnu cenu po prodavcu
    sales_data = {}

    for ticket in tickets:
        sale_date = datetime.strptime(ticket['sale_date'], "%d.%m.%Y")

        # Provera da li je prodaja izvršena u poslednjih 30 dana
        if sale_date >= thirty_days_ago and sale_date <= today and ticket['status'] == 'sold':
            seller = ticket['seller_username']
            ticket_price = float(ticket['ticket_price'])

            if seller in sales_data:
                sales_data[seller]['total_tickets'] += 1
                sales_data[seller]['total_sales'] += ticket_price
            else:
                sales_data[seller] = {'total_tickets': 1, 'total_sales': ticket_price}

    print("Sales data for the last 30 days:\n")
    table_data = []
    headers = ['Seller', 'Total Tickets Sold', 'Total Sales']

    for seller, data in sales_data.items():
        table_data.append([seller, data['total_tickets'], data['total_sales']])

    print(tabulate(table_data, headers=headers, tablefmt="pretty"))

    while True:
        choice = input("Save this report to a file? (yes/no): ").lower()
        if choice == "yes":
            filename = "report_h.txt"
            with open(filename, "a") as file:
                file.write("Sales data for the last 30 days:\n")
                file.write(tabulate(table_data, headers=headers, tablefmt="pretty"))
                file.write("\n\n")
            print(f"Report saved to '{filename}'")
            break
        elif choice == "no":
            break
        else:
            print("Please enter 'yes' or 'no'.")
            continue

    return


# Svi izvestaji stavljeni pod jednu funkciju -> odakle se bira koji da se pozove ... -> sa opcionim upisom u fajl
def get_reports(sold_tickets, tickets, cinema_projections, sellers, projection_terms, manager_username):
    while True:
        menus.report_menu()
        choice = input("Enter your choice from the menu: ")
        if choice == "1":
            display_sold_tickets_for_date(sold_tickets, manager_username)
            continue
        elif choice == "2":
            display_sold_tickets_for_term_date(cinema_projections, projection_terms, sold_tickets, manager_username)
            continue
        elif choice == "3":
            display_sold_tickets_for_date_and_seller(tickets, manager_username)
            continue
        elif choice == "4":
            calculate_sales_for_sell_day_week(tickets, manager_username)
            continue
        elif choice == "5":
            calculate_sales_for_term_day_week(tickets, manager_username)
            continue
        elif choice == "6":
            calculate_total_sales_for_movie(cinema_projections, tickets, manager_username)
            continue
        elif choice == "7":
            calculate_sales_for_sell_day_and_seller(tickets, sellers, manager_username)
            continue
        elif choice == "8":
            display_sales_for_sellers_last_30_days(tickets, manager_username)
            continue
        elif choice == "0":
            print("Exiting reports ...")
            return
        else:
            print("Invalid input. Try again.")
            continue


# Funkcija za izmenu filma sa case slucajevima za ime filma i menjanje vreme, odnosno end_time u projekciji
def modify_movie(movies, cinema_projections):
    while True:
        print("Movies available for modification:")
        for index, movie in enumerate(movies, start=1):
            print(f"{index}. {movie['name']}")

        choice = input("Enter the number of the movie you want to modify (or 'exit' to cancel): ")

        if choice.lower() == 'exit':
            print("Modification canceled.")
            return movies

        try:
            choice = int(choice)
            if choice < 1 or choice > len(movies):
                print("Please enter a valid movie number.")
                continue

            chosen_movie = movies[choice - 1]

            new_name = input(f"Enter new movie name (press Enter to keep '{chosen_movie['name']}') or '*' to skip: ")
            if new_name != '*':
                if new_name != '':
                    if '|' in new_name:
                        print("Invalid input. Movie name cannot contain '|'.")
                        continue
                    if any(movie['name'].lower() == new_name.lower() for movie in movies if movie != chosen_movie):
                        print("Movie with that name already exists. Please choose a different name.")
                        continue
                    old_name = chosen_movie['name']
                    chosen_movie['name'] = new_name

                    for projection in cinema_projections:
                        if projection['movie_name'] == old_name:
                            projection['movie_name'] = new_name

            new_genre = input(f"Enter new genre (press Enter to keep '{chosen_movie['genre']}') or '*' to skip: ")
            if new_genre != '*':
                if new_genre != '':
                    if '|' in new_genre or new_genre.strip() == '':
                        print("Invalid input. Genre cannot contain '|' or be empty.")
                        continue
                    chosen_movie['genre'] = new_genre

            while True:
                new_duration = input(
                    f"Enter new duration in minutes (press Enter to keep '{chosen_movie['duration']}') or '*' to skip: ")
                if new_duration != '*':
                    if new_duration != '':
                        try:
                            duration = int(new_duration)
                            if duration < 0 or duration > int(chosen_movie['duration']):
                                print("Invalid input. Duration can be only lower than last one.")
                                continue
                            chosen_movie['duration'] = duration

                            for projection in cinema_projections:
                                if projection['movie_name'] == chosen_movie['name']:
                                    start_time = projection['start_time']
                                    end_time = projection['end_time']

                                    start_datetime = datetime.strptime(start_time, '%H:%M')
                                    end_datetime = datetime.strptime(end_time, '%H:%M')

                                    new_end_datetime = start_datetime + timedelta(minutes=duration)
                                    new_end_time = new_end_datetime.strftime('%H:%M')
                                    projection['end_time'] = new_end_time

                        except ValueError:
                            print("Invalid input. Please enter a valid number for duration.")
                            continue
                break

            new_director = input(
                f"Enter new director (press Enter to keep '{chosen_movie['director']}') or '*' to skip: ")
            if new_director != '*':
                if new_director != '':
                    if '|' in new_director or new_director.strip() == '':
                        print("Invalid input. Director cannot contain '|' or be empty.")
                        continue
                    chosen_movie['director'] = new_director

            new_main_roles = input(
                f"Enter new main roles separated by commas (press Enter to keep '{', '.join(chosen_movie['main_roles'])}') or '*' to skip: ")
            if new_main_roles != '*':
                if new_main_roles != '':
                    if '|' in new_main_roles:
                        print("Character '|' is not allowed.")
                        continue
                    main_roles_list = [role.strip() for role in new_main_roles.split(',')]
                    chosen_movie['main_roles'] = main_roles_list

            new_country_origin = input(
                f"Enter new country origin (press Enter to keep '{chosen_movie['country_origin']}') or '*' to skip: ")
            if new_country_origin != '*':
                if new_country_origin != '':
                    if '|' in new_country_origin or new_country_origin.strip() == '':
                        print("Invalid input. Country origin cannot contain '|' or be empty.")
                        continue
                    chosen_movie['country_origin'] = new_country_origin

            new_production_year = input(
                f"Enter new production year (press Enter to keep '{chosen_movie['production_year']}') or '*' to skip: ")
            if new_production_year != '*':
                if new_production_year != '':
                    try:
                        production_year = int(new_production_year)
                        if production_year < 1800 or production_year > 2023:
                            print("Invalid input. Production year should be between 1800 and 2023.")
                            continue
                        chosen_movie['production_year'] = production_year
                    except ValueError:
                        print("Invalid input. Please enter a valid production year.")
                        continue

            new_short_description = input(
                f"Enter new short description (up to 100 characters) (press Enter to keep '{chosen_movie['short_description']}') or '*' to skip: ")
            if new_short_description != '*':
                if new_short_description != '':
                    if '|' in new_short_description:
                        print("Short description cannot contain '|'.")
                        continue
                    if len(new_short_description) > 100:
                        print("Short description cannot exceed 100 characters.")
                        continue
                    chosen_movie['short_description'] = new_short_description

            print("Movie details updated successfully!")

            write_movies_to_file(movies, "movies.txt")

            return movies, cinema_projections

        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit' to cancel.")


# Funkcija za brisanje film koja pored filma brise i projekciju ako je projekcija na taj naziv filma
# brise i sve termine za tu projekciju i brise i sve karte za te termine
def delete_movie(movies, cinema_projections, projection_terms, tickets):
    while True:
        print("Movies available for deletion: ")
        headers = ["Index", "Movie Name", "Genre", "Duration", "Director", "Main Roles", "Country Origin",
                   "Production Year", "Short Description"]
        movie_data = [(i + 1, movie['name'], movie['genre'], movie['duration'], movie['director'],
                       ', '.join(movie['main_roles']), movie['country_origin'], movie['production_year'],
                       movie['short_description']) for i, movie in enumerate(movies)]
        print(tabulate(movie_data, headers=headers, tablefmt="grid"))

        choice = input("Enter the number of the movie you want to delete (or 'exit' to cancel): ")

        if choice.lower() == 'exit':
            print("Deletion canceled.")
            return movies, cinema_projections, projection_terms, tickets
        try:
            choice = int(choice)
            if choice < 1 or choice > len(movies):
                print("Please enter a valid movie number.")
                continue

            chosen_movie = movies[choice - 1]
            movie_name = chosen_movie['name']
            projection_ids = [projection['id'] for projection in cinema_projections if
                              projection['movie_name'] == movie_name]

            del movies[choice - 1]

            cinema_projections = [projection for projection in cinema_projections if
                                  projection['movie_name'] != movie_name]

            projection_terms = [term for term in projection_terms if
                                not term['projection_code'].startswith(tuple(projection_ids))]

            tickets = [ticket for ticket in tickets if not ticket['term_id'][:4] in tuple(projection_ids)]

            # Updejtovanje fajlova
            write_movies_to_file(movies, "movies.txt")
            functionality.write_projections_in_file(cinema_projections, "projections.txt")
            functionality.write_projection_terms_to_file_update(projection_terms, "projection_terms.txt")
            functionality.write_tickets_in_file("tickets.txt", tickets)

            return movies, cinema_projections, projection_terms, tickets

        except ValueError:
            print("Invalid input. Please try again.")
            continue


# Funkcija za dodavanje projekcije -> Brine o zauzetosti sale
def add_cinema_projection(movies, halls, cinema_projections, projection_terms):
    try:
        scheduled_movies = set(projection['movie_name'] for projection in cinema_projections)
        available_movies = [movie for movie in movies if movie['name'] not in scheduled_movies]

        if not available_movies:
            print("All movies are already scheduled for projections.")

            for movie_name in scheduled_movies:
                projections_for_movie = [projection for projection in cinema_projections if
                                         movie_name in projection['movie_name']]
                print(f"Projections for movie '{movie_name}':")
                if projections_for_movie:
                    headers = ["Projection ID", "Hall ID", "Start Time", "End Time", "Days", "Ticket Price"]
                    projection_data = [
                        (projection['id'], projection['id_hall'], projection['start_time'], projection['end_time'],
                         ', '.join(projection['days']), projection['ticket_price']) for projection in
                        projections_for_movie]
                    print(tabulate(projection_data, headers=headers, tablefmt="grid"))
                else:
                    print("No projections scheduled.")
            return

        print("Movies available for scheduling:")
        headers = ["Index", "Movie Name", "Genre", "Duration", "Director", "Main Roles", "Country Origin",
                   "Production Year", "Short Description"]
        movie_data = [(i + 1, movie['name'], movie['genre'], movie['duration'], movie['director'],
                       ', '.join(movie['main_roles']), movie['country_origin'], movie['production_year'],
                       movie['short_description']) for i, movie in enumerate(available_movies)]
        print(tabulate(movie_data, headers=headers, tablefmt="grid"))

        choice = input("Enter the number of the movie for the new projection (or 'exit' to cancel): ")
        if choice.lower() == "exit":
            print("Projection addition canceled.")
            return cinema_projections

        choice = int(choice)
        if choice < 1 or choice > len(available_movies):
            print("Please enter a valid movie number.")
            return cinema_projections

        chosen_movie = available_movies[choice - 1]
        print(f"Chosen movie: {chosen_movie['name']}")

        while True:
            chosen_hall = None
            print("Available Halls:")
            for index, hall in enumerate(halls, start=1):
                print(f"{index}. {hall['id_hall']}")

            hall_choice = input("Enter the number of the hall for the new projection: ")
            hall_choice = int(hall_choice) - 1

            if hall_choice < 0 or hall_choice >= len(halls):
                print("Please enter a valid hall number.")
                continue

            chosen_hall = halls[hall_choice]
            break

        valid_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

        while True:
            while True:
                days_input = input("Enter days for the projection (e.g., monday,tuesday): ").lower().split(',')
                if all(day in valid_days for day in days_input):
                    break
                else:
                    print("Invalid input for days. Please enter valid days.")
                    continue

            while True:
                try:
                    ticket_price = float(input("Enter ticket price for the projection: "))
                    if ticket_price < 50:
                        print("Invalid ticket price !!! Try again !!!")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for ticket price.")

            duration = int(chosen_movie['duration'])

            while True:
                try:
                    chosen_start_time = input("Enter start time for the projection (HH:MM format) or exit: ")
                    if chosen_start_time == "exit":
                        print("We are sorry but we don't have enough space for projection !!!")
                        return
                    time_format = "%H:%M"
                    start_time_obj = datetime.strptime(chosen_start_time, time_format)
                    end_time_obj = start_time_obj + timedelta(minutes=duration)
                    chosen_end_time = end_time_obj.strftime(time_format)

                    # Provera za konflikte za zauzetost sale
                    conflict = False
                    for projection in cinema_projections:
                        if (projection['id_hall'] == chosen_hall['id_hall']
                                and any(day in projection['days'] for day in days_input)):
                            existing_start_time = datetime.strptime(projection['start_time'], time_format)
                            existing_end_time = datetime.strptime(projection['end_time'], time_format)

                            # Konflikt
                            if (start_time_obj <= existing_start_time < end_time_obj) or \
                                    (start_time_obj < existing_end_time <= end_time_obj) or \
                                    (existing_start_time <= start_time_obj and end_time_obj <= existing_end_time):
                                print("Selected hall is already occupied at the chosen time or overlaps with existing "
                                      "projections. Please select another time. ")
                                conflict = True
                                break

                    if conflict:
                        continue

                    if not cinema_projections:
                        initial_projection_id = 1000
                    else:
                        max_projection_id = max(int(projection['id']) for projection in cinema_projections)
                        initial_projection_id = max_projection_id + 1

                    new_projection_code = str(initial_projection_id)
                    new_projection_id = new_projection_code

                    new_projection = {
                        "id": new_projection_id,
                        "id_hall": chosen_hall['id_hall'],
                        "start_time": chosen_start_time,
                        "end_time": chosen_end_time,
                        "days": days_input,
                        "movie_name": chosen_movie['name'],
                        "ticket_price": ticket_price
                        # nema potrebe da se gleda da li je utorak ili vikend jer je ovo base cena -> cena na kartama varira, a ova u projekciji je uvek ista
                    }

                    cinema_projections.append(new_projection)
                    print("New projection added successfully!")

                    # Generisanje novih termina ...
                    start_term = 'AA'
                    # konvertujemo u broj po modu 26
                    term_number = (ord(start_term[0]) - 65) * 26 + (ord(start_term[1]) - 65) - 1  # Initialize to 0

                    today = datetime.today()
                    two_weeks_later = today + timedelta(days=21)
                    dates = [today + timedelta(days=i) for i in range((two_weeks_later - today).days)]

                    for day in days_input:
                        for date in dates:
                            if date.strftime('%A').lower() == day.lower():
                                term_number += 1

                                term_code = chr(65 + (term_number // 26)) + chr(65 + (term_number % 26))
                                term_id = new_projection_id + term_code

                                hall_info = [hall for hall in halls if hall['id_hall'] == new_projection['id_hall']][0]
                                rows = int(hall_info['number_of_rows'])
                                columns = int(hall_info['seats_per_row'])

                                new_term = {
                                    'term_id': term_id,
                                    'projection_code': new_projection_id,
                                    'term_code': term_code,
                                    'date': date.strftime('%d.%m.%Y'),
                                    'seat_matrix': [['O' for _ in range(columns)] for _ in range(rows)]
                                }
                                projection_terms.append(new_term)
                                with open("projection_terms.txt", "a") as file:
                                    file.write(
                                        f"{new_term['projection_code']}{new_term['term_code']}|{new_term['date']}\n")
                    functionality.write_projections_in_file(cinema_projections, "projections.txt")

                    return cinema_projections

                except ValueError:
                    print("Invalid time format. Please enter time in HH:MM format.")
                    continue
    except ValueError:
        print("Invalid input. Please try again.")
        return cinema_projections


def delete_cinema_projection(cinema_projections, projection_terms, tickets):
    try:
        if not cinema_projections:
            print("No cinema projections available to delete.")
            return cinema_projections, projection_terms, tickets

        print("Cinema projections available for deletion: ")
        headers = ["Index", "Movie Name", "Start Time", "End Time", "Days", "Ticket Price"]
        projection_data = [(i + 1, projection['movie_name'], projection['start_time'], projection['end_time'],
                            ', '.join(projection['days']), projection['ticket_price']) for i, projection in
                           enumerate(cinema_projections)]
        print(tabulate(projection_data, headers=headers, tablefmt="grid"))

        while True:
            try:
                choice = int(input("Enter the number of the projection you want to delete (or 'exit' to cancel): "))
                if choice == 'exit':
                    print("Deletion canceled.")
                    return cinema_projections, projection_terms, tickets

                if choice < 1 or choice > len(cinema_projections):
                    print("Please enter a valid projection number.")
                    continue

                chosen_projection = cinema_projections[choice - 1]
                projection_id = chosen_projection['id']
                movie_name = chosen_projection['movie_name']

                del cinema_projections[choice - 1]

                projection_terms = [term for term in projection_terms if
                                    not term['projection_code'].startswith(projection_id)]
                tickets = [ticket for ticket in tickets if not ticket['term_id'][:4] == projection_id]

                print(f"Cinema projection '{movie_name}' deleted successfully!")
                functionality.write_projections_in_file(cinema_projections, "projections.txt")
                functionality.write_projection_terms_to_file_update(projection_terms, "projection_terms.txt")

                for projection in projection_terms:
                    print(projection['projection_code'])
                return cinema_projections, projection_terms, tickets

            except ValueError:
                print("Invalid input. Please enter a valid number or 'exit' to cancel.")
                continue

    except Exception as e:
        print(f"An error occurred during deletion: {e}")
        return cinema_projections, projection_terms, tickets


def change_projection_hall(chosen_projection, halls, cinema_projections, projection_terms, tickets):
    chosen_start_time = datetime.strptime(chosen_projection['start_time'], "%H:%M")
    chosen_end_time = datetime.strptime(chosen_projection['end_time'], "%H:%M")

    print("Available Halls:")
    available_halls = []

    for hall in halls:
        hall_is_available = True

        for projection in cinema_projections:
            if (projection['id_hall'] == hall['id_hall']
                    and any(day in projection['days'] for day in chosen_projection['days'])):
                existing_start_time = datetime.strptime(projection['start_time'], "%H:%M")
                existing_end_time = datetime.strptime(projection['end_time'], "%H:%M")

                if (chosen_start_time <= existing_start_time < chosen_end_time) or \
                        (chosen_start_time < existing_end_time <= chosen_end_time) or \
                        (existing_start_time <= chosen_start_time and chosen_end_time <= existing_end_time):
                    hall_is_available = False
                    break

        if hall_is_available:
            available_halls.append(hall)
            print(f"{len(available_halls)}. {hall['id_hall']}")

    if not available_halls:
        print("Currently, it is not possible to change the hall because all other halls are occupied.")
        return

    while True:
        hall_choice = input("Enter the number of the new hall for the projection (or exit for cancel): ")
        if hall_choice == "exit":
            return
        try:
            hall_choice = int(hall_choice) - 1
            if 0 <= hall_choice < len(available_halls):
                chosen_hall = available_halls[hall_choice]

                tickets = [ticket for ticket in tickets if ticket['term_id'][:4] != chosen_projection['id']]
                projection_terms = [term for term in projection_terms if
                                    term['projection_code'] != chosen_projection['id']]
                chosen_projection['id_hall'] = chosen_hall['id_hall']

                functionality.write_projections_in_file(cinema_projections, "projections.txt")
                functionality.write_tickets_in_file("tickets.txt", tickets)
                functionality.write_projection_terms_to_file_update(projection_terms,
                                                                    "projection_terms.txt")  # brisemo stare termine u fajlu
                functionality.generate_projection_terms(cinema_projections, halls,
                                                        projection_terms)  # generisemo termine koji fale u fajlu

                print(f"Hall successfully changed to {chosen_hall['id_hall']} for the projection.")
                break
            else:
                print("Please enter a valid hall number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def change_projection_price(chosen_projection, cinema_projections, tickets):
    while True:
        new_price_input = input("Enter the new ticket price for the projection (minimum 100), or 'exit' to cancel: ")

        if new_price_input.lower() == 'exit':
            print("Price change canceled.")
            return

        try:
            new_price = float(new_price_input)
            if new_price < 100:
                print("Invalid ticket price. Minimum is 100.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    chosen_projection['ticket_price'] = new_price

    for ticket in tickets:
        if ticket['term_id'][:4] == chosen_projection['id']:
            term_date = datetime.strptime(ticket['term_date'], "%d.%m.%Y")
            if term_date.strftime('%A').lower() == 'tuesday':
                ticket['ticket_price'] = new_price - 50
            elif term_date.strftime('%A').lower() in ['saturday', 'sunday']:
                ticket['ticket_price'] = new_price + 50
            else:
                ticket['ticket_price'] = new_price

    functionality.write_projections_in_file(cinema_projections, "projections.txt")
    functionality.write_tickets_in_file("tickets.txt", tickets)

    print(f"Ticket price for the projection updated to {new_price}.")


def change_projection_days(chosen_projection, cinema_projections, projection_terms, tickets, halls):
    available_days = []

    print("Available Days:")
    for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        hall_is_available = all(
            chosen_projection['id_hall'] != projection['id_hall'] or day not in projection['days']
            for projection in cinema_projections
        )

        if hall_is_available:
            available_days.append(day.lower())
            print(day.capitalize())
    while True:
        new_days_input = input(
            "Enter the new days for the projection (e.g., monday,tuesday), or 'exit' to cancel: ").lower().split(',')

        if new_days_input == chosen_projection['days']:
            print("No changes made. Please enter different days.")
            continue

        if new_days_input == ['exit']:
            print("Projection day change canceled.")
            return

        if all(day in available_days for day in new_days_input):
            break
        else:
            print("Invalid input for days. Please enter valid days.")
            continue

    tickets = [ticket for ticket in tickets if ticket['term_id'][:4] != chosen_projection['id']]
    projection_terms = [term for term in projection_terms if term['projection_code'] != chosen_projection['id']]

    chosen_projection['days'] = new_days_input

    functionality.write_projections_in_file(cinema_projections, "projections.txt")
    functionality.write_projection_terms_to_file_update(projection_terms, "projection_terms.txt")
    functionality.generate_projection_terms(cinema_projections, halls, projection_terms)
    functionality.write_tickets_in_file("tickets.txt", tickets)

    print(f"Projection days updated to {', '.join(new_days_input)}.")


def modify_cinema_projection_better(cinema_projections, projection_terms, tickets, halls, movies):
    while True:
        print(
            "Disclaimer -> Any change causes serious changes in the system, such as changes to term or tickets or their complete deletion, please be careful when using this function !!!")
        print("Thank you for your understanding. ")
        print("Available Projections: ")
        print("Cinema projections available for deletion: ")
        headers = ["Index", "Projection ID", "Hall ID", "Start Time", "End Time", "Days", "Movie Name", "Ticket Price"]
        projection_data = [
            (index, projection['id'], projection['id_hall'], projection['start_time'], projection['end_time'],
             ', '.join(projection['days']), projection['movie_name'], projection['ticket_price'])
            for index, projection in enumerate(cinema_projections, start=1)
        ]
        print(tabulate(projection_data, headers=headers, tablefmt="grid"))

        choice = input("Enter the number of the projection to edit (or 'exit' to cancel): ")
        if choice.lower() == "exit":
            print("Projection editing canceled.")
            return cinema_projections, projection_terms, tickets

        choice = int(choice)
        if choice < 1 or choice > len(cinema_projections):
            print("Please enter a valid projection number.")
            return cinema_projections, projection_terms, tickets

        chosen_projection = cinema_projections[choice - 1]

        print(f"Editing projection: {chosen_projection['movie_name']}")
        menus.modify_cinema_projection()

        modify_choice = input("Enter choice from the menu: ")
        if modify_choice == "0":
            print("Exiting modification of projection ...")
            return
        elif modify_choice == "1":
            change_projection_hall(chosen_projection, halls, cinema_projections, projection_terms, tickets)
            continue
        elif modify_choice == "2":
            change_projection_days(chosen_projection, cinema_projections, projection_terms, tickets, halls)
            continue
        elif modify_choice == "3":
            change_projection_price(chosen_projection, cinema_projections, tickets)
            continue
        else:
            print("Invalid input. Please try again.")
            continue


# Zahtev 24. Promena cene karte -> automatski se menja prilikom dodavanje nove projekcije ili prilikom izmene projekcije
# A na poziv od menadzera treba da menja postojeci ticket_price
def change_ticket_prices(tickets):
    today = datetime.now()

    table_data = []

    for ticket in tickets:
        projection_date = datetime.strptime(ticket['term_date'], "%d.%m.%Y")
        projection_day = projection_date.weekday()

        reason_for_change = ""
        ticket_info = ""

        if projection_day == 1:  # Utorak
            new_price = float(ticket['ticket_price']) - 50
            if new_price >= 50:
                ticket['ticket_price'] = str(new_price)
                reason_for_change = "Discount applied for Tuesday"
            else:
                reason_for_change = "Price remains unchanged, discount cannot be applied for Tuesday"

        elif projection_day in [5, 6]:  # Vikend
            ticket['ticket_price'] = str(float(ticket['ticket_price']) + 50)
            reason_for_change = "Price increased for the weekend"

        if reason_for_change:
            ticket_info = [
                ticket['username'],
                ticket['term_id'],
                ticket['term_date'],
                ticket['ticket_price'],
                ticket['seller_username'],
                ticket['sale_date'],
                reason_for_change,
                ticket['status']
            ]
            table_data.append(ticket_info)

    headers = ['Username', 'Term ID', 'Term Date', 'Ticket Price', 'Seller Username', 'Purchase Date',
               'Reason for Change', 'Status']
    if table_data:
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    else:
        print("No changes made to ticket prices.")


# Ovu funkciju pozivam pre same upotrebe aplikacije da lepo ispise vremena, a pozivam je i na poziv menadzera
def manually_change_ticket_price(cinema_projections):
    today = datetime.today()
    current_day = today.strftime('%A').lower()

    for projection in cinema_projections:
        ticket_price = projection['ticket_price']
        projection_days = projection['days']

        if current_day == 'tuesday' and 'tuesday' in projection_days:
            if ticket_price >= 50:
                projection['ticket_price'] -= 50
                print(f"Ticket prices for the {projection['movie_name']} reduced by 50 -> Tuesday")
                print(f"New price: {projection['ticket_price']}")
        elif current_day in ['saturday', 'sunday'] and any(day in ['saturday', 'sunday'] for day in projection_days):
            projection['ticket_price'] += 50
            print(f"Ticket prices for the {projection['movie_name']} increased by 50 -> Weekend ")
            print(f"New price: {projection['ticket_price']}")
        else:
            print(f"Ticket prices for {projection['movie_name']} did not change !!!")


def display_seat_matrix_for_term(projection_term):
    seat_matrix = projection_term['seat_matrix']
    for row in seat_matrix:
        formatted_row = ['X' if seat == 'X' else '-' for seat in row]  # '-' umesto 'O' za prazna sedišta
        print(" ".join(formatted_row))


def display_loyal_customer(total_spent_per_user, registered_customers):
    loyal_customers = [(username, total_spent) for username, total_spent in total_spent_per_user.items() if
                       total_spent > 5000]

    if loyal_customers:
        print("Loyal Customers:")
        headers = ["Username", "Total Spent", "Name", "Last Name", "Role"]
        for customer in registered_customers:
            for loyal_customer in loyal_customers:
                if customer['username'] == loyal_customer[0]:
                    # Ne ispisujemo šifru
                    customer_data = (
                    customer['username'], loyal_customer[1], customer['name'], customer['last_name'], customer['role'])
                    print(tabulate([customer_data], headers=headers, tablefmt="grid"))
    else:
        print("No loyal customers found.")

def display_customer_info(total_spent_per_user, registered_customers):
    if total_spent_per_user:
        print("Customer Information:")
        headers = ["Username", "Total Spent", "Name", "Last Name", "Role"]

        for customer in registered_customers:
            username = customer['username']
            total_spent = total_spent_per_user.get(username, 0)
            customer_data = (username, total_spent, customer['name'], customer['last_name'], customer['role'])
            print(tabulate([customer_data], headers=headers, tablefmt="grid"))
            print("\n\n")
    else:
        print("No customer information available.")