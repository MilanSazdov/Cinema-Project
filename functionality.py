import menus
from tabulate import tabulate
from datetime import datetime, timedelta
from prettytable import PrettyTable
import registered_customer_functions
import manager_functions
import seller_functions


def is_username_unique_through_file(username):
    files = ["registered_customers.txt", "sellers.txt", "managers.txt"]
    for file_name in files:
        with open(file_name, "r") as file:
            for line in file:
                parts_of_line = line.strip().split("|")
                if parts_of_line[0] == username:
                    return False
    return True


def is_username_unique(username, registered_customers, sellers, managers):
    registered_customers_username_list = [registered_customer["username"] for registered_customer in
                                          registered_customers]
    sellers_username_list = [seller["username"] for seller in sellers]
    managers_username_list = [manager["username"] for manager in managers]

    if username in registered_customers_username_list or username in sellers_username_list or username in managers_username_list:
        return False
    return True


def check_password(password):
    return len(password) > 6 and any(c.isdigit() for c in password)


def login(registered_customers, sellers, managers):
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        registered_customer_exists = any(customer["username"] == username for customer in registered_customers)
        manager_exists = any(manager["username"] == username for manager in managers)
        seller_exists = any(seller["username"] == username for seller in sellers)

        if not registered_customer_exists and not manager_exists and not seller_exists:
            print("The user does not exist. Please enter an existing username!")
            user_decision = input("Do you want to continue logging in? (yes/no): ")
            if user_decision.lower() == "no":
                print("Login canceled.")
                return 0, None
            else:
                continue
        else:
            if registered_customer_exists:
                for customer in registered_customers:
                    if customer["username"] == username:
                        if customer["password"] == password:
                            print("You have successfully logged in!")
                            return 1, username
                        else:
                            print("Wrong password!")
                            break

            if manager_exists:
                for manager in managers:
                    if manager["username"] == username:
                        if manager["password"] == password:
                            print("You have successfully logged in!")
                            return 3, username
                        else:
                            print("Wrong password!")
                            break

            if seller_exists:
                for seller in sellers:
                    if seller["username"] == username:
                        if seller["password"] == password:
                            print("You have successfully logged in!")
                            return 2, username
                        else:
                            print("Wrong password!")
                            break


def logout(username):
    print(f"You {username} have successfully logged out ...")


def change_name(username, role, registered_customers, sellers, managers):
    if role == 1:
        user_list = registered_customers
    elif role == 2:
        user_list = sellers
    elif role == 3:
        user_list = managers
    else:
        print("Invalid role!")
        return

    found = False
    for user in user_list:
        if user['username'] == username:
            found = True
            break

    if not found:
        print("User not found.")
        return

    while True:
        flag = False
        new_name = input("Enter a new name: ")

        if new_name == next((user['name'] for user in user_list if user['username'] == username), None):
            print("The new name is the same as the old one.")
            continue

        if not new_name.strip() or '|' in new_name:
            print("The name cannot contain the '|' character.")
            continue

        for user in user_list:
            if user['username'] == username:
                user['name'] = new_name
                print(f"The name of the user with {username} has been changed to {new_name}!")
                flag = True
                break
        if flag:
            break

    # Ako je promena imena uspešna, ažuriraj originalne liste
    if role == 1:
        for i, user in enumerate(registered_customers):
            if user['username'] == username:
                registered_customers[i] = user_list[i]
                break
    elif role == 2:
        for i, user in enumerate(sellers):
            if user['username'] == username:
                sellers[i] = user_list[i]
                break
    elif role == 3:
        for i, user in enumerate(managers):
            if user['username'] == username:
                managers[i] = user_list[i]
                break


def change_last_name(username, role, registered_customers, sellers, managers):
    if role == 1:
        user_list = registered_customers
    elif role == 2:
        user_list = sellers
    elif role == 3:
        user_list = managers
    else:
        print("Invalid role!")
        return

    found = False
    for user in user_list:
        if user['username'] == username:
            found = True
            break

    if not found:
        print("User not found.")
        return

    while True:
        flag = False
        new_last_name = input("Enter a new last name: ")

        if new_last_name == next((user['last_name'] for user in user_list if user['username'] == username), None):
            change_decision = input(
                "The new last name is the same as the old one. Do you want to enter a new last name? (yes/no): ")
            if change_decision.lower() == 'yes':
                continue
            else:
                print("Last name change canceled.")
                return

        if not new_last_name.strip() or '|' in new_last_name:
            change_decision = input(
                "The last name cannot be empty or contain the '|' character. Do you want to enter a new last name? (yes/no): ")
            if change_decision.lower() == 'yes':
                continue
            else:
                print("Last name change canceled.")
                return

        for user in user_list:
            if user['username'] == username:
                user['last_name'] = new_last_name
                print(f"The last name of the user with {username} has been changed to {new_last_name}!")
                flag = True
                break
        if flag:
            break
    # Ako je promena prezimena uspešna, ažuriraj originalne liste
    if role == 1:
        for i, user in enumerate(registered_customers):
            if user['username'] == username:
                registered_customers[i] = user_list[i]
                break
    elif role == 2:
        for i, user in enumerate(sellers):
            if user['username'] == username:
                sellers[i] = user_list[i]
                break
    elif role == 3:
        for i, user in enumerate(managers):
            if user['username'] == username:
                managers[i] = user_list[i]
                break


def change_password(username, role, registered_customers, sellers, managers):
    if role == 1:
        user_list = registered_customers
    elif role == 2:
        user_list = sellers
    elif role == 3:
        user_list = managers
    else:
        print("Invalid role!")
        return

    found = False
    for user in user_list:
        if user['username'] == username:
            found = True
            break

    if not found:
        print("User not found.")
        return

    while True:
        flag = False
        new_password = input("Enter a new password (longer than 6 characters and contains at least one digit): ")

        if not check_password(new_password):
            print("The password does not meet the requirements.")
            continue

        if not new_password.strip() or '|' in new_password:
            change_decision = input(
                "The password cannot be empty or contain the '|' character. Do you want to enter a new password? (yes/no): ")
            if change_decision.lower() == 'yes':
                continue
            else:
                print("Password change canceled.")
                break

        old_password = next((user['password'] for user in user_list if user['username'] == username), None)

        if new_password == old_password:
            change_decision = input(
                "The new password is the same as the old one. Do you want to enter a new password? (yes/no): ")
            if change_decision.lower() == 'yes':
                continue
            else:
                print("Password change canceled.")
                break

        for user in user_list:
            if user['username'] == username:
                user['password'] = new_password
                print(f"The password of the user {username} has been changed!")
                flag = True
                break
        if flag:
            break
    # Ako je promena šifre uspešna, ažuriraj originalne liste
    if role == 1:
        for i, user in enumerate(registered_customers):
            if user['username'] == username:
                registered_customers[i] = user_list[i]
                break
    elif role == 2:
        for i, user in enumerate(sellers):
            if user['username'] == username:
                sellers[i] = user_list[i]
                break
    elif role == 3:
        for i, user in enumerate(managers):
            if user['username'] == username:
                managers[i] = user_list[i]
                break


# username je jedinstven pa zato preko toga trazimo, a role je da li je u pitanju registrovani_korisnik, prodavac ili
# menadzer, 1 - registrovani_korisnik, 2 - prodavac, 3 - menadzer
def modification_of_personal_data(username, role, registered_customers, sellers, managers):
    while True:
        menus.modification_of_personal_data_menu()
        try:
            option = int(input("Enter a number from the menu: "))
            if option == 1:
                change_name(username, role, registered_customers, sellers, managers)
                break
            elif option == 2:
                change_last_name(username, role, registered_customers, sellers, managers)
                break
            elif option == 3:
                change_password(username, role, registered_customers, sellers, managers)
                break
            else:
                print("Wrong input! Try again.")
        except ValueError:
            print("Wrong input! Please enter a number.")
            continue


def load_movies(file_name):
    movies = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                parts_of_line = line.strip().split("|")
                main_roles = parts_of_line[4].split(",") if "," in parts_of_line[4] else [parts_of_line[4]]
                movie = {
                    "name": parts_of_line[0],
                    "genre": parts_of_line[1],
                    "duration": parts_of_line[2],
                    "director": parts_of_line[3],
                    "main_roles": main_roles,
                    "country_origin": parts_of_line[5],
                    "production_year": parts_of_line[6],
                    "short_description": parts_of_line[7]
                }
                movies.append(movie)
    except FileNotFoundError:
        pass
    return movies


def overview_of_available_movies(movies):
    print("Available movies: ")
    headers = ["Name", "Genre", "Duration", "Director", "Main Roles", "Country of Origin", "Production Year",
               "Description"]
    rows = []

    for movie in movies:
        rows.append([
            movie["name"],
            movie["genre"],
            movie["duration"],
            movie["director"],
            movie["main_roles"],
            movie["country_origin"],
            movie["production_year"],
            movie["short_description"]
        ])

    print(tabulate(rows, headers=headers, tablefmt="pretty"))


def search_movie_by_name(movies):
    search_query = input("Enter movie name: ").lower()
    return [movie for movie in movies if search_query in movie['name'].lower()]


def search_movie_by_genre(movies):
    search_query = input("Enter movie genre: ").lower()
    return [movie for movie in movies if search_query in movie['genre'].lower()]


def search_movie_by_duration(movies):
    while True:
        try:
            duration = int(input("Enter duration (in minutes): "))
            if duration < 0 or duration > 600:
                print("Invalid input. Duration should be between 0 and 600 minutes.")
                decision = input("Do you want to try again? (yes/no): ")
                if decision.lower() == 'yes':
                    continue
                else:
                    return None
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        sign = input("Enter < or >: ")
        if sign == '<':
            return [movie for movie in movies if float(movie['duration']) < duration]
        elif sign == '>':
            return [movie for movie in movies if float(movie['duration']) > duration]
        else:
            print("Invalid input. Please enter < or >.")


def search_movie_by_director(movies):
    search_query = input("Enter director of a movie: ").lower()
    return [movie for movie in movies if search_query in movie['director'].lower()]


def search_movie_by_main_roles(movies):
    search_query = input("Enter main roles (separated by comma if multiple): ").lower().split(',')
    search_query = [role.strip() for role in search_query]

    found_movies = []
    for movie in movies:
        for role in search_query:
            if role in [r.lower() for r in movie['main_roles']]:
                found_movies.append(movie)
                break

    return found_movies


def search_movie_by_country_origin(movies):
    search_query = input("Enter country origin of a movie: ").lower()
    return [movie for movie in movies if search_query in movie['country_origin'].lower()]


def search_movie_by_production_year(movies):
    search_query = input("Enter production year of a movie: ").lower()
    return [movie for movie in movies if search_query in movie['production_year'].lower()]


# Pretraga filmova - obicna sa 1 kriterijom
def search_movies_by_criteria(movies):
    while True:
        menus.search_movie_by_criteria_menu()
        try:
            option = int(input("Enter option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            choice = input("Do you want to try again? (yes/no): ")
            if choice.lower() == 'yes':
                continue
            else:
                print("Exiting search.")
                return

        if option < 1 or option > 8:
            print("Invalid option. Please enter a number between 1 and 8.")
            choice = input("Do you want to try again? (yes/no): ")
            if choice.lower() == 'yes':
                continue
            else:
                print("Exiting search.")
                return

        if option == 1:
            found_movies = search_movie_by_name(movies)
        elif option == 2:
            found_movies = search_movie_by_genre(movies)
        elif option == 3:
            found_movies = search_movie_by_duration(movies)
        elif option == 4:
            found_movies = search_movie_by_director(movies)
        elif option == 5:
            found_movies = search_movie_by_main_roles(movies)
        elif option == 6:
            found_movies = search_movie_by_country_origin(movies)
        elif option == 7:
            found_movies = search_movie_by_production_year(movies)
        else:
            print("Exiting search.")
            return

        if found_movies:
            overview_of_available_movies(found_movies)
            break
        else:
            print("No movies found.")
            continue


def search_movies_by_multi_criteria(movies):
    search_criteria = {
        'name': '',
        'genre': '',
        'duration': '',
        'director': '',
        'main_roles': '',
        'country_origin': '',
        'production_year': ''
    }

    # Unos svih kriterijuma
    for key in search_criteria:
        while True:
            value = input(f"Enter {key.replace('_', ' ').title()} (leave blank if not applicable): ")

            if key == 'duration' and not value:  # Preskakanje pretrage ako je vrednost za dužinu trajanja prazna
                break

            if '|' in value:
                print("Character '|' is not allowed. Please enter again.")
                continue
            if key == 'duration':
                if value.startswith('<') or value.startswith('>'):
                    if len(value) > 1 and value[1:].isdigit():
                        break
                    else:
                        print("Invalid input for duration. Please enter < or > followed by a number.")
                        continue
                elif value.isdigit():
                    break
                else:
                    print("Invalid input for duration. Please enter a number or < or > followed by a number.")
                    continue
            elif key == 'main_roles':
                search_criteria[key] = [role.strip() for role in value.split(',') if role.strip()]
                break
            search_criteria[key] = value.lower()  # Dodatak za pretvaranje unosa u mala slova
            break

    # Pretraga
    found_movies = []
    for movie in movies:
        match = True
        for key, value in search_criteria.items():
            if value and key != 'duration' and key != 'main_roles':
                if value not in movie[key].lower():
                    match = False
                    break
            elif key == 'duration':
                if not value:  # Preskakanje pretrage ako je dužina trajanja prazna
                    continue
                try:
                    movie_duration = float(movie[key])
                    if search_criteria[key].startswith('<'):
                        duration_value = float(search_criteria[key][1:])
                        if movie_duration >= duration_value:
                            match = False
                            break
                    elif search_criteria[key].startswith('>'):
                        duration_value = float(search_criteria[key][1:])
                        if movie_duration <= duration_value:
                            match = False
                            break
                    else:
                        duration_value = float(search_criteria[key])
                        if movie_duration != duration_value:
                            match = False
                            break
                except ValueError:
                    match = False
                    break
            elif key == 'main_roles':
                if not value:  # Preskakanje pretrage ako glavne uloge nisu unete
                    continue
                entered_roles = [role.strip().lower() for role in value]
                movie_roles = [role.strip().lower() for role in movie[key]]
                match_found = any(role in movie_roles for role in entered_roles)
                if not match_found:
                    match = False
                    break
        if match:
            found_movies.append(movie)
    if not found_movies:
        print("No movies found with the specified criteria.")
        return
    overview_of_available_movies(found_movies)
    return found_movies


def load_cinema_projections(file_name):
    movie_projections = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts_of_line = line.strip().split('|')
                if len(parts_of_line) == 7:
                    projection = {
                        "id": parts_of_line[0],
                        "id_hall": parts_of_line[1],
                        "start_time": parts_of_line[2],
                        "end_time": parts_of_line[3],
                        "days": parts_of_line[4].split(','),
                        "movie_name": parts_of_line[5],
                        "ticket_price": float(parts_of_line[6])
                    }
                    movie_projections.append(projection)
                else:
                    print(f"Ignoring invalid line: {line.strip()}")
    except FileNotFoundError:
        print("File not found. Please provide a valid file name.")

    return movie_projections


def load_cinema_halls(file_name):
    cinema_halls = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts_of_line = line.strip().split('|')
                if len(parts_of_line) >= 3:
                    hall = {
                        "id_hall": parts_of_line[0],
                        "hall_name": parts_of_line[1],
                        "number_of_rows": int(parts_of_line[2]),
                        "seats_per_row": parts_of_line[3]
                    }
                    cinema_halls.append(hall)
                else:
                    print(f"Ignoring invalid line: {line.strip()}")
    except FileNotFoundError:
        print("File not found. Please provide a valid file name.")

    return cinema_halls


def write_projection_terms_with_seating_to_file(projection_terms, file_name):
    with open(file_name, 'w') as file:
        for term in projection_terms:
            file.write(
                f"Projection Code: {term['projection_code']}, Term Code: {term['term_code']}, Date: {term['date']}\n")

            # Dodavanje slova iznad matrice
            file.write('  ')
            for i in range(len(term['seat_matrix'][0])):
                file.write(f'{chr(65 + i)} ')
            file.write('\n')

            # Dodavanje numeracije sa leve strane matrice i samog sadržaja matrice
            for i, row in enumerate(term['seat_matrix'], start=1):
                file.write(f"{i} {' '.join(row)}\n")

            file.write('\n')


def generate_seating_matrix(cinema_projections, halls, projection_terms):
    for term in projection_terms:
        projection_code = term['projection_code']
        for projection in cinema_projections:
            if projection['id'] == projection_code:
                hall_id = projection['id_hall']
                for hall in halls:
                    if hall['id_hall'] == hall_id:
                        rows = hall['number_of_rows']  # Broj redova u sali
                        columns = hall['seats_per_row']  # Broj kolona u sali

                        # Provera tipova podataka za rows i columns
                        if not isinstance(rows, int) or not isinstance(columns, int):
                            print("Invalid data for rows or columns.")
                            return None

                        seat_matrix = [['O' for _ in range(columns)] for _ in range(rows)]
                        term['seat_matrix'] = seat_matrix
                        break
                break

    # Čitanje informacija iz fajla tickets.txt
    with open('tickets.txt', 'r') as file:
        lines = file.readlines()

        # Ažuriranje seat_matrix na osnovu informacija iz tickets.txt
    for line in lines:
        ticket_info = line.strip().split('|')
        term_code = ticket_info[1][-2:]  # Uzimanje poslednja dva karaktera kao term_code
        projection_code = ticket_info[1][:-2]  # Uzimanje prvih četiri karaktera kao projection_code
        seat_label = ticket_info[3]  # Oznaka sedišta iz fajla tickets.txt

        for term in projection_terms:
            if term['term_code'] == term_code and term['projection_code'] == projection_code:
                row = int(seat_label[:-1]) - 1  # Red u matrici
                column = ord(seat_label[-1]) - ord('A')  # Kolona u matrici
                term['seat_matrix'][row][column] = 'X'  # Oznaka za zauzeto mesto
                break

        # Upisivanje informacija u fajl projection_terms_with_seating.txt
    with open("projection_terms_with_seating.txt", "w") as file:
        for term in projection_terms:
            file.write(
                f"Projection Code: {term['projection_code']}, Term Code: {term['term_code']}, Date: {term['date']}\n")

            # Dodavanje slova iznad matrice
            file.write('  ')
            for i in range(len(term['seat_matrix'][0])):
                file.write(f'{chr(65 + i)} ')
            file.write('\n')

            # Dodavanje numeracije sa leve strane matrice i sadržaja matrice
            for i, row in enumerate(term['seat_matrix'], start=1):
                file.write(f"{i} {' '.join(row)}\n")

            file.write('\n')

    return projection_terms


def load_projection_terms(filename, tickets, halls, cinema_projections):
    projection_terms = []

    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split('|')
        projection_code = data[0][:4]
        term_code = data[0][-2:]
        date = data[1]

        for projection in cinema_projections:
            if projection['id'] == projection_code:
                hall_info = [hall for hall in halls if hall['id_hall'] == projection['id_hall']][0]
                rows = int(hall_info['number_of_rows'])
                columns = int(hall_info['seats_per_row'])
                break

        term = {
            'projection_code': projection_code,
            'term_code': term_code,
            'date': date,
            'seat_matrix': [['O' for _ in range(columns)] for _ in range(rows)]
        }
        projection_terms.append(term)

    for ticket in tickets:
        term_code = ticket['term_id'][-2:]
        projection_code = ticket['term_id'][:-2]

        for term in projection_terms:
            if term['term_code'] == term_code and term['projection_code'] == projection_code:
                row = int(ticket['seat_code'][:-1]) - 1
                column = ord(ticket['seat_code'][-1]) - ord('A')
                term['seat_matrix'][row][column] = 'X'
                break

    return projection_terms


def find_max_term_code(projection_terms, projection_code):
    filtered_terms = [term for term in projection_terms if term['projection_code'] == projection_code]
    if not filtered_terms:
        return None

    max_term_code = max(filtered_terms, key=lambda term: term['term_code'])['term_code']

    return max_term_code


# Funkcija koja generise termine bioskopske projekcije
def generate_projection_terms(cinema_projections, halls, projection_terms):
    today = datetime.today()
    two_weeks_later = today + timedelta(days=14)

    while today < two_weeks_later:
        for projection in cinema_projections:
            for day in projection['days']:
                if today.strftime('%A').lower() == day.lower():
                    projection_code = str(projection['id'])
                    date = today.strftime('%d.%m.%Y')

                    # Provera da li je već napravljena projekcija za ovaj datum
                    existing_projection = any(
                        term['date'] == date and term['projection_code'] == projection_code for term in
                        projection_terms)

                    if not existing_projection:
                        max_term_code = find_max_term_code(projection_terms, projection_code)

                        if max_term_code is None:
                            term_code = "AA"
                        else:
                            next_index = ord(max_term_code[1]) - ord('A') + 1
                            next_letter1 = max_term_code[0]
                            next_letter2 = chr((next_index % 26) + ord('A'))
                            term_code = next_letter1 + next_letter2

                        hall_info = [hall for hall in halls if hall['id_hall'] == projection['id_hall']][0]
                        rows = int(hall_info['number_of_rows'])
                        columns = int(hall_info['seats_per_row'])

                        # Pravim novi termin gde je raspored sedenja skroz prazan
                        term = {
                            'projection_code': projection_code,
                            'term_code': term_code,
                            'date': date,
                            'seat_matrix': [['O' for _ in range(columns)] for _ in range(rows)]
                        }
                        projection_terms.append(term)
                        with open("projection_terms.txt", "a") as file:
                            file.write(f"{term['projection_code']}{term['term_code']}|{term['date']}\n")

        today += timedelta(days=1)

    # write_projection_terms_to_file(projection_terms, "projection_terms.txt") -> ne treba svaki put upisivati ...
    return projection_terms


# generate_seating_matrix(cinema_projections, halls, projection_terms)


def generate_seating_arrangement(projection_terms):
    with open("seating_arrangement.txt", "w") as file:
        for term in projection_terms:
            file.write(
                f"Projection Code: {term['projection_code']}, Term Code: {term['term_code']}, Date: {term['date']}\n")

            # Kreiranje PrettyTable objekta
            table = PrettyTable()
            table.field_names = [''] + [chr(65 + i) for i in range(len(term['seat_matrix'][0]))]

            # Popunjavanje tabele slobodnim i zauzetim mestima
            for i, row in enumerate(term['seat_matrix'], start=1):
                table.add_row([i] + row)

            # Ispisivanje tabele u fajl
            file.write(str(table))
            file.write("\n\n")


def write_projection_terms_to_file(projection_terms, file_name):
    with open(file_name, 'a') as file:
        for term in projection_terms:
            line = f"{term['projection_code']}{term['term_code']}|{term['date']}\n"
            file.write(line)


# Ova funkcija se poziva kada se promene projection term da bi izbacio one koji vise ne postoje !!!
def write_projection_terms_to_file_update(projection_terms, file_name):
    with open(file_name, 'w') as file:
        for term in projection_terms:
            line = f"{term['projection_code']}{term['term_code']}|{term['date']}\n"
            file.write(line)


def search_for_terms_of_cinema_projections(cinema_projections, projection_terms):
    option = -1
    while True:
        menus.search_for_terms_of_cinema_projections_menu()
        try:
            option = int(input("Enter option from the menu: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            choice = input("Do you want to try again? (yes/no): ")
            if choice.lower() == 'yes':
                continue
            else:
                print("Exiting search.")
                return

        found_projections = []

        if option == 1:
            film_name = input("Enter the film name: ").lower()
            found_projections = [projection for projection in cinema_projections if
                                 projection['movie_name'].lower() == film_name]
            if not found_projections:
                print("No cinema projections found based on the specified film.")
                return
            else:
                print(f"Found cinema projections for film '{film_name}':")
                table = PrettyTable(["Film", "Hall", "Date", "Start Time", "End Time", "Term Code"])
                for projection in found_projections:
                    terms = [term for term in projection_terms if term['projection_code'] == projection['id']]
                    for term in terms:
                        term_code = term['projection_code'] + term['term_code']
                        table.add_row([projection['movie_name'], projection['id_hall'], term['date'],
                                       projection['start_time'], projection['end_time'], term_code])
                print(table)

        elif option == 2:
            hall_name = input("Enter the hall name: ").lower()
            found_projections = [projection for projection in cinema_projections if
                                 projection['id_hall'].lower() == hall_name]
            if not found_projections:
                print("No cinema projections found based on the specified hall.")
                return
            else:
                print(f"Found cinema projections for hall '{hall_name}':")
                table = PrettyTable(["Film", "Hall", "Date", "Start Time", "End Time", "Term Code"])
                for projection in found_projections:
                    terms = [term for term in projection_terms if term['projection_code'] == projection['id']]
                    for term in terms:
                        term_code = term['projection_code'] + term['term_code']
                        table.add_row([projection['movie_name'], projection['id_hall'], term['date'],
                                       projection['start_time'], projection['end_time'], term_code])
                print(table)

        elif option == 3:
            date = input("Enter the date (DD.MM.YYYY): ")
            found_terms = [term for term in projection_terms if term['date'] == date]
            if not found_terms:
                print("No cinema projections found based on the specified date.")
                return
            else:
                print(f"Found cinema projections for date '{date}':")
                table = PrettyTable(["Film", "Hall", "Date", "Start Time", "End Time", "Term Code"])
                for term in found_terms:
                    projection = next((proj for proj in cinema_projections if proj['id'] == term['projection_code']),
                                      None)
                    if projection:
                        term_code = term['projection_code'] + term['term_code']
                        table.add_row([projection['movie_name'], projection['id_hall'], term['date'],
                                       projection['start_time'], projection['end_time'], term_code])
                print(table)

        elif option == 4:
            start_time = input("Enter the start time (HH:MM): ")
            end_time = input("Enter the end time (HH:MM): ")
            found_projections = [projection for projection in cinema_projections if
                                 projection['start_time'] == start_time and projection['end_time'] == end_time]
            if not found_projections:
                print("No cinema projections found based on the specified time.")
                return
            else:
                print(f"Found cinema projections for start time '{start_time}' and end time '{end_time}':")
                table = PrettyTable(["Film", "Hall", "Date", "Start Time", "End Time", "Term Code"])
                for projection in found_projections:
                    terms = [term for term in projection_terms if term['projection_code'] == projection['id']]
                    for term in terms:
                        term_code = term['projection_code'] + term['term_code']
                        table.add_row([projection['movie_name'], projection['id_hall'], term['date'],
                                       projection['start_time'], projection['end_time'], term_code])
                print(table)

        elif option == 5:
            return
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


def load_tickets(file_name):
    tickets = []

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                ticket_data = line.strip().split('|')
                ticket = {
                    'username': ticket_data[0],
                    'term_id': ticket_data[1],
                    'term_date': ticket_data[2],
                    'seat_code': ticket_data[3],
                    'sale_date': ticket_data[4],
                    'seller_username': ticket_data[5],
                    'ticket_price': ticket_data[6],
                    'status': ticket_data[7]
                }
                tickets.append(ticket)
    except FileNotFoundError:
        print("File not found.")

    return tickets


def print_seat_matrix(term):
    print(f"Seat Matrix for Term Code {term['term_code']} ({term['projection_code']}), Date: {term['date']}:")
    table = PrettyTable()
    table.field_names = [''] + [chr(65 + i) for i in range(len(term['seat_matrix'][0]))]

    for i, row in enumerate(term['seat_matrix'], start=1):
        table.add_row([i] + row)

    print(table)


def write_tickets_in_file(file_name, tickets):
    with open(file_name, "w") as file:
        for ticket in tickets:
            line = line = f"{ticket['username']}|{ticket['term_id']}|{ticket['term_date']}|{ticket['seat_code']}|{ticket['sale_date']}|{ticket['seller_username']}|{ticket['ticket_price']}|{ticket['status']}\n"
            file.write(line)


def display_all_tickets(tickets, cinema_projections):
    table_data = []

    for ticket in tickets:
        term_id = ticket['term_id']
        projection_info = next(
            (projection for projection in cinema_projections if projection['id'] == term_id[:4]),
            None
        )

        if projection_info:
            ticket_info = [
                ticket['username'],
                term_id,
                ticket['term_date'],
                projection_info['movie_name'],
                projection_info['start_time'],
                projection_info['end_time'],
                ticket['seat_code'],
                ticket['sale_date'],
                ticket['seller_username'],
                ticket['ticket_price'],
                ticket['status']
            ]
            table_data.append(ticket_info)

    headers = ["Username", "Term Code", "Term Date", "Movie Name", "Start Time", "End Time", "Seat Code", "Sale Date", "Seller", "Price", "Status"]
    if table_data:
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    else:
        print("No tickets found in the system.")


def update_sold_tickets(tickets):
    sold_tickets = {}

    for ticket in tickets:
        username = ticket['username']
        status = ticket['status']
        ticket_info = f"{ticket['term_id']}|{ticket['term_date']}|{ticket['seat_code']}|{ticket['sale_date']}|{ticket['seller_username']}|{ticket['ticket_price']}|{ticket['status']}"

        if status == 'sold':
            if username in sold_tickets:
                sold_tickets[username].append(ticket_info)
            else:
                sold_tickets[username] = [ticket_info]

    return sold_tickets


def update_reserved_tickets(tickets):
    reserved_tickets = {}

    for ticket in tickets:
        username = ticket['username']
        status = ticket['status']
        ticket_info = f"{ticket['term_id']}|{ticket['term_date']}|{ticket['seat_code']}|{ticket['sale_date']}|{ticket['seller_username']}|{ticket['ticket_price']}|{ticket['status']}"
        if status == 'reserved':
            if username in reserved_tickets:
                reserved_tickets[username].append(ticket_info)
            else:
                reserved_tickets[username] = [ticket_info]

    return reserved_tickets


def update_sold_tickets_one(sold_tickets, new_ticket):
    username = new_ticket['username']
    ticket_info = '|'.join([
        new_ticket['term_id'],
        new_ticket['term_date'],
        new_ticket['seat_code'],
        new_ticket['sale_date'],
        new_ticket['seller_username'],
        str(new_ticket['ticket_price']),
        new_ticket['status']
    ])

    if username in sold_tickets:
        sold_tickets[username].append(ticket_info)
    else:
        sold_tickets[username] = [ticket_info]

    return sold_tickets


def write_projections_in_file(cinema_projections, file_name):
    try:
        with open(file_name, 'w') as file:
            for projection in cinema_projections:
                line = f"{projection['id']}|{projection['id_hall']}|{projection['start_time']}|{projection['end_time']}|{','.join(projection['days'])}|{projection['movie_name']}|{projection['ticket_price']}\n"
                file.write(line)
        print("Cinema projections successfully written to file.")
    except Exception as e:
        print(f"An error occurred while writing cinema projections to file: {e}")
