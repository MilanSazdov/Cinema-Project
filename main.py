import menus
import registered_customer_functions
import seller_functions
import manager_functions
import functionality

file_name = "registered_customers.txt"
file_name_sellers = "sellers.txt"
file_name_managers = "managers.txt"
file_name_movies = "movies.txt"
file_name_projections = "projections.txt"
file_name_cinema_halls = "halls.txt"
file_name_projection_terms = "projection_terms.txt"
file_name_tickets = "tickets.txt"

# Ucitavanje registrovanih kupaca iz fajla
registered_customers = registered_customer_functions.load_registered_customers(file_name)

# Ucitavanje prodavaca iz fajla
sellers = seller_functions.load_sellers(file_name_sellers)

# Ucitavanje menadzera iz fajla
managers = manager_functions.load_managers(file_name_managers)

# Ucitavanje filmova iz fajla
movies = functionality.load_movies(file_name_movies)

# Ucitavanje bioskopskih projekcija iz fajla
cinema_projections = functionality.load_cinema_projections(file_name_projections)

# Ucitavanje bioskopskih sala iz fajla
cinema_halls = functionality.load_cinema_halls(file_name_cinema_halls)

# Generisanje termina bioskopskih projekcija i upisivanje u fajl


# Ucitavanje bioskopskih karata iz fajla
tickets = functionality.load_tickets(file_name_tickets)

reserved_tickets = registered_customer_functions.load_reserved_tickets(file_name_tickets)
sold_tickets = registered_customer_functions.load_sold_tickets(file_name_tickets)

# Karte koje je prodao taj i taj prodavac ...
sold_tickets_by_sellers = seller_functions.load_sold_tickets_by_sellers("sold_tickets_by_sellers.txt")


total_spent_per_user = {}

seller_functions.calculate_total_spent(tickets, registered_customers, total_spent_per_user)

projection_terms = functionality.load_projection_terms(file_name_projection_terms, tickets, cinema_halls, cinema_projections)

projection_terms = functionality.generate_projection_terms(cinema_projections, cinema_halls, projection_terms)
functionality.generate_seating_arrangement(projection_terms)

if __name__ == '__main__':

    while True:
        menus.menu_for_all()
        try:
            x = int(input("Enter a number from the menu: "))
            if x < 1 or x > 7:
                print("\n\nYou entered an incorrect number !!!\n")
                continue
            elif x == 1:
                role_after_login, username = functionality.login(registered_customers, sellers, managers)
                if role_after_login == 1:
                    while True:
                        try:
                            menus.registered_customers_menu()
                            y = int(input("Enter a number from the menu: "))
                            if y < 1 or y > 9:
                                print("\n\nYou entered an incorrect number !!!\n")
                                continue
                            elif y == 1:
                                functionality.logout(username)
                                manager_functions.write_managers_in_file(file_name_managers, managers)
                                seller_functions.write_sellers_in_file(file_name_sellers, sellers)
                                registered_customer_functions.write_registered_customers_in_file(file_name, registered_customers)
                                functionality.write_tickets_in_file(file_name_tickets, tickets)
                                functionality.write_projections_in_file(cinema_projections, file_name_projections)
                                break
                            elif y == 2:
                                functionality.modification_of_personal_data(username, role_after_login, registered_customers, sellers, managers)
                                continue
                            elif y == 3:
                                functionality.overview_of_available_movies(movies)
                                continue
                            elif y == 4:
                                functionality.search_movies_by_criteria(movies)
                                continue
                            elif y == 5:
                                functionality.search_movies_by_multi_criteria(movies)
                                continue
                            elif y == 6:
                                functionality.search_for_terms_of_cinema_projections(cinema_projections, projection_terms)
                                continue
                            elif y == 7:
                                registered_customer_functions.reserve_tickets(username, cinema_projections, projection_terms, tickets, reserved_tickets)
                                sold_tickets = functionality.update_sold_tickets(tickets)
                                reserved_tickets = functionality.update_reserved_tickets(tickets)
                                total_spent_per_user = seller_functions.reset_total_spent_per_user(total_spent_per_user)
                                seller_functions.calculate_total_spent(tickets, registered_customers, total_spent_per_user)
                                continue
                            elif y == 8:
                                registered_customer_functions.display_reserved_tickets(username, reserved_tickets, cinema_projections, projection_terms)
                                continue
                            elif y == 9:
                                registered_customer_functions.cancel_ticket_reservation(username, reserved_tickets, tickets, projection_terms)
                                sold_tickets = functionality.update_sold_tickets(tickets)
                                reserved_tickets = functionality.update_reserved_tickets(tickets)
                                total_spent_per_user = seller_functions.reset_total_spent_per_user(total_spent_per_user)
                                seller_functions.calculate_total_spent(tickets, registered_customers, total_spent_per_user)
                                continue
                        except ValueError:
                            print("\n\nInvalid input! Please enter a valid number.TESTTESTTEST\n")
                            continue
                elif role_after_login == 2:
                    while True:
                        try:
                            menus.seller_menu()
                            seller_menu_option = int(input("Enter a number from the menu: "))
                            if seller_menu_option < 1 or seller_menu_option > 14:
                                print("\n\nYou entered an incorrect number !!!\n")
                                continue
                            elif seller_menu_option == 1:
                                functionality.logout(username)
                                manager_functions.write_managers_in_file(file_name_managers, managers)
                                seller_functions.write_sellers_in_file(file_name_sellers, sellers)
                                registered_customer_functions.write_registered_customers_in_file(file_name, registered_customers)
                                functionality.write_tickets_in_file(file_name_tickets, tickets)
                                functionality.write_projections_in_file(cinema_projections, file_name_projections)
                                break
                            elif seller_menu_option == 2:
                                functionality.modification_of_personal_data(username, role_after_login, registered_customers, sellers, managers)
                                continue
                            elif seller_menu_option == 3:
                                functionality.overview_of_available_movies(movies)
                                continue
                            elif seller_menu_option == 4:
                                functionality.search_movies_by_criteria(movies)
                                continue
                            elif seller_menu_option == 5:
                                functionality.search_movies_by_multi_criteria(movies)
                                continue
                            elif seller_menu_option == 6:
                                functionality.search_for_terms_of_cinema_projections(cinema_projections, projection_terms)
                                continue
                            elif seller_menu_option == 7:
                                seller_functions.reserve_tickets_seller(registered_customers, cinema_projections, projection_terms, tickets, reserved_tickets, username)
                                reserved_tickets = functionality.update_reserved_tickets(tickets)
                                sold_tickets = functionality.update_sold_tickets(tickets)
                                total_spent_per_user = seller_functions.reset_total_spent_per_user(total_spent_per_user)
                                seller_functions.calculate_total_spent(tickets, registered_customers, total_spent_per_user)
                                continue
                            elif seller_menu_option == 8:
                                seller_functions.display_reserved_tickets(cinema_projections, projection_terms, reserved_tickets, sold_tickets, tickets, registered_customers, movies)
                                continue
                            elif seller_menu_option == 9:
                                seller_functions.cancel_ticket_reservation_seller(reserved_tickets, sold_tickets, tickets, cinema_projections, projection_terms)
                                reserved_tickets = functionality.update_reserved_tickets(tickets)
                                sold_tickets = functionality.update_sold_tickets(tickets)
                                total_spent_per_user = seller_functions.reset_total_spent_per_user(total_spent_per_user)
                                seller_functions.calculate_total_spent(tickets, registered_customers, total_spent_per_user)
                                continue
                            elif seller_menu_option == 10:
                                seller_functions.search_tickets(tickets, cinema_projections, projection_terms, registered_customers, reserved_tickets, sold_tickets)
                                continue
                            elif seller_menu_option == 11:
                                seller_functions.direct_ticket_sales(reserved_tickets, sold_tickets, tickets, cinema_projections, projection_terms, username, total_spent_per_user, registered_customers)
                                sold_tickets = functionality.update_sold_tickets(tickets)
                                reserved_tickets = functionality.update_reserved_tickets(tickets)
                                total_spent_per_user = seller_functions.reset_total_spent_per_user(total_spent_per_user)
                                seller_functions.calculate_total_spent(tickets, registered_customers, total_spent_per_user)
                                continue
                            elif seller_menu_option == 12:
                                seller_functions.sell_reserved_tickets(tickets, reserved_tickets, sold_tickets, username, total_spent_per_user)
                                sold_tickets = functionality.update_sold_tickets(tickets)
                                reserved_tickets = functionality.update_reserved_tickets(tickets)
                                total_spent_per_user = seller_functions.reset_total_spent_per_user(total_spent_per_user)
                                seller_functions.calculate_total_spent(tickets, registered_customers, total_spent_per_user)
                                continue
                            elif seller_menu_option == 13:
                                seller_functions.update_ticket(tickets, registered_customers, projection_terms, cinema_projections, reserved_tickets, sold_tickets, sellers, managers)
                                reserved_tickets = functionality.update_reserved_tickets(tickets)
                                sold_tickets = functionality.update_sold_tickets(tickets)
                                total_spent_per_user = seller_functions.reset_total_spent_per_user(total_spent_per_user)
                                seller_functions.calculate_total_spent(tickets, registered_customers, total_spent_per_user)
                                continue
                            elif seller_menu_option == 14:
                                #tickets, reserved_tickets = seller_functions.cancel_reservation_before_start(cinema_projections, projection_terms, tickets, reserved_tickets)
                                seller_functions.cancel_unclaimed_reservations(reserved_tickets, tickets, cinema_projections, projection_terms)
                                reserved_tickets = functionality.update_reserved_tickets(tickets)
                                sold_tickets = functionality.update_sold_tickets(tickets)
                                total_spent_per_user = seller_functions.reset_total_spent_per_user(total_spent_per_user)
                                seller_functions.calculate_total_spent(tickets, registered_customers, total_spent_per_user)
                                continue
                        except ValueError:
                            print("\n\nInvalid input! Please enter a valid number.\n")
                            continue
                elif role_after_login == 3:
                    while True:
                        try:
                            menus.manager_menu()
                            manager_menu_option = int(input("Enter a number from the menu: "))
                            if manager_menu_option < 1 or manager_menu_option > 18:
                                print("\n\nYou entered an incorrect number !!!\n")
                                continue
                            elif manager_menu_option == 1:
                                functionality.logout(username)
                                manager_functions.write_managers_in_file(file_name_managers, managers)
                                seller_functions.write_sellers_in_file(file_name_sellers, sellers)
                                registered_customer_functions.write_registered_customers_in_file("registered_customers.txt", registered_customers)
                                functionality.write_projections_in_file(cinema_projections, file_name_projections)
                                functionality.write_tickets_in_file(file_name_tickets, tickets)
                                manager_functions.write_movies_to_file(movies, file_name_movies)
                                break
                            elif manager_menu_option == 2:
                                functionality.modification_of_personal_data(username, role_after_login, registered_customers, sellers, managers)
                                continue
                            elif manager_menu_option == 3:
                                manager_functions.registration_of_seller_or_manager(registered_customers, sellers, managers)
                                continue
                            elif manager_menu_option == 4:
                                functionality.overview_of_available_movies(movies)
                                continue
                            elif manager_menu_option == 5:
                                functionality.search_movies_by_criteria(movies)
                                continue
                            elif manager_menu_option == 6:
                                functionality.search_movies_by_multi_criteria(movies)
                                continue
                            elif manager_menu_option == 7:
                                manager_functions.add_new_movie(movies)
                                continue
                            elif manager_menu_option == 8:
                                functionality.search_for_terms_of_cinema_projections(cinema_projections, projection_terms)
                                continue
                            elif manager_menu_option == 9:
                                manager_functions.get_reports(sold_tickets, tickets, cinema_projections, sellers, projection_terms, username)
                                continue
                            elif manager_menu_option == 10:
                                manager_functions.display_loyal_customer(total_spent_per_user, registered_customers)
                                continue
                            elif manager_menu_option == 11:
                                manager_functions.display_seating_arrangement(cinema_projections, projection_terms)
                                continue
                            elif manager_menu_option == 12:
                                manager_functions.change_ticket_prices(tickets)
                                sold_tickets = functionality.update_sold_tickets(tickets)
                                reserved_tickets = functionality.update_reserved_tickets(tickets)
                                total_spent_per_user = seller_functions.reset_total_spent_per_user(total_spent_per_user)
                                seller_functions.calculate_total_spent(tickets, registered_customers, total_spent_per_user)
                                continue
                            elif manager_menu_option == 13:
                                movies, cinema_projections = manager_functions.modify_movie(movies, cinema_projections)
                                continue
                            elif manager_menu_option == 14:
                                movies, cinema_projections, projection_terms,  tickets = manager_functions.delete_movie(movies, cinema_projections, projection_terms, tickets)
                                sold_tickets = functionality.update_sold_tickets(tickets)
                                reserved_tickets = functionality.update_reserved_tickets(tickets)
                                total_spent_per_user = seller_functions.reset_total_spent_per_user(total_spent_per_user)
                                seller_functions.calculate_total_spent(tickets, registered_customers,
                                                                       total_spent_per_user)
                                continue
                            elif manager_menu_option == 15:
                                cinema_projections = manager_functions.add_cinema_projection(movies, cinema_halls, cinema_projections, projection_terms)
                                continue
                            elif manager_menu_option == 16:
                                #cinema_projections, projection_terms, tickets = manager_functions.modify_cinema_projection(cinema_projections, projection_terms, tickets, cinema_halls, movies)
                                cinema_projections, projection_terms, tickets = manager_functions.modify_cinema_projection_better(cinema_projections, projection_terms, tickets, cinema_halls, movies)
                                sold_tickets = functionality.update_sold_tickets(tickets)
                                reserved_tickets = functionality.update_reserved_tickets(tickets)
                                total_spent_per_user = seller_functions.reset_total_spent_per_user(total_spent_per_user)
                                seller_functions.calculate_total_spent(tickets, registered_customers,
                                                                       total_spent_per_user)
                                continue
                            elif manager_menu_option == 17:
                                cinema_projections, projection_terms, tickets = manager_functions.delete_cinema_projection(cinema_projections, projection_terms, tickets)
                                reserved_tickets = functionality.update_reserved_tickets(tickets)
                                sold_tickets = functionality.update_sold_tickets(tickets)
                                total_spent_per_user = seller_functions.reset_total_spent_per_user(total_spent_per_user)
                                seller_functions.calculate_total_spent(tickets, registered_customers,
                                                                       total_spent_per_user)
                                continue
                            elif manager_menu_option == 18:
                                manager_functions.display_customer_info(total_spent_per_user, registered_customers)
                                continue
                        except ValueError:
                            print("\n\nInvalid input! Please enter a valid number.\n")
                            continue
                elif role_after_login == 0:
                    manager_functions.write_managers_in_file(file_name_managers, managers)
                    seller_functions.write_sellers_in_file(file_name_sellers, sellers)
                    registered_customer_functions.write_registered_customers_in_file(file_name, registered_customers)
                    functionality.write_tickets_in_file(file_name_tickets, tickets)
                    functionality.write_projections_in_file(cinema_projections, file_name_projections)
                    manager_functions.write_movies_to_file(movies, file_name_movies)
                    continue
                else:
                    print("Error !!!")
                    break
            elif x == 2:
                print("Closing the application ...")
                manager_functions.write_managers_in_file(file_name_managers, managers)
                seller_functions.write_sellers_in_file(file_name_sellers, sellers)
                registered_customer_functions.write_registered_customers_in_file(file_name, registered_customers)
                functionality.write_tickets_in_file(file_name_tickets, tickets)
                functionality.write_projections_in_file(cinema_projections, file_name_projections)
                manager_functions.write_movies_to_file(movies, file_name_movies)
                break
            elif x == 3:
                functionality.overview_of_available_movies(movies)
                continue
            elif x == 4:
                functionality.search_movies_by_criteria(movies)
                continue
            elif x == 5:
                functionality.search_movies_by_multi_criteria(movies)
                continue
            elif x == 6:
                functionality.search_for_terms_of_cinema_projections(cinema_projections, projection_terms)
                continue
            elif x == 7:
                while True:
                    new_username = input("Enter your username: ")

                    if not new_username.strip() or '|' in new_username or " " in new_username:
                        print("Invalid username ! Username cannot be empty or contain '|' character !")
                        continue

                    if not any(customer['username'] == new_username for customer in registered_customers) \
                            and not any(manager['username'] == new_username for manager in managers) \
                            and not any(seller['username'] == new_username for seller in sellers):
                        break
                    else:
                        print("Username already exists. Please enter a new username !!!")

                while True:
                    new_password = input(
                        "Enter your password (longer than 6 characters and contains at least one digit): ")
                    if len(new_password) == 0:
                        print("Password cannot be an empty string. Please enter a valid password!")
                        continue
                    elif '|' in new_password:
                        print("Password cannot contain the '|' character. Please enter a valid password!")
                        continue
                    elif not functionality.check_password(new_password):
                        print("The password does not meet the requirements. Enter a new password!")
                        continue
                    else:
                        break

                while True:
                    new_name = input("Enter your name: ")

                    if not new_name.strip() or '|' in new_name:
                        print("Invalid name ! Name cannot be empty or contain '|' character.")
                        continue
                    else:
                        break

                while True:
                    new_last_name = input("Enter your last name: ")

                    if not new_last_name.strip() or '|' in new_last_name:
                        print("Invalid last name! Last name cannot be empty or contain '|' character.")
                        continue
                    else:
                        break

                new_customer = {
                    "username": new_username,
                    "password": new_password,
                    "name": new_name,
                    "last_name": new_last_name,
                    "role": "registered_customer"
                }

                registered_customers.append(new_customer)
                print(f"User {new_username} added successfully !!!")
            else:
                print("Unknown option, please enter an option from the menu !")
                continue
        except ValueError:
            print("\n\nInvalid input! Please enter a number.\n")
            continue
