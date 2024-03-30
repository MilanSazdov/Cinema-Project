def menu_for_all():
    print("\n  *----------------------------------------------------------------------------*")
    print("  | Enter 1. for Login:                                                        |")
    print("  | Enter 2. for Exit:                                                         |")
    print("  | Enter 3. for Overview of available movies:                                 |")
    print("  | Enter 4. for Movie search:                                                 |")
    print("  | Enter 5. for Multi-criteria movie search:                                  |")
    print("  | Enter 6. for Search for the dates of cinema screenings:                    |")
    print("  | Enter 7. for Register:                                                     |")
    print("  *----------------------------------------------------------------------------*\n\n")


def registered_customers_menu():
    print("\n  *----------------------------------------------------------------------------*")
    print("  | Enter 1. for Logout:                                                       |")
    print("  | Enter 2. for Modification of personal data:                                |")
    print("  | Enter 3. for Overview of available movies:                                 |")
    print("  | Enter 4. for Movie search:                                                 |")
    print("  | Enter 5. for Multi-criteria movie search:                                  |")
    print("  | Enter 6. for Search for the dates of cinema screenings:                    |")
    print("  | Enter 7. for Ticket reservation:                                           |")
    print("  | Enter 8. for Overview of reserved tickets:                                 |")
    print("  | Enter 9. for Cancellation of ticket reservation:                           |")
    print("  *----------------------------------------------------------------------------*\n\n")


def seller_menu():
    print("\n  *----------------------------------------------------------------------------*")
    print("  | Enter 1. for Logout:                                                       |")
    print("  | Enter 2. for Modification of personal data:                                |")
    print("  | Enter 3. for Overview of available movies:                                 |")
    print("  | Enter 4. for Movie search:                                                 |")
    print("  | Enter 5. for Multi-criteria movie search:                                  |")
    print("  | Enter 6. for Search for the dates of cinema screenings:                    |")
    print("  | Enter 7. for Ticket reservation:                                           |")
    print("  | Enter 8. for Overview of reserved tickets:                                 |")
    print("  | Enter 9. for Cancellation of reserved/sold tickets:                        |")
    print("  | Enter 10. for Search for tickets:                                          |")
    print("  | Enter 11. for Direct ticket sales:                                         |")
    print("  | Enter 12. for Sale of reserved tickets:                                    |")
    print("  | Enter 13. for Changing the ticket:                                         |")
    print("  | Enter 14. for Cancellation of reservation 30 minutes before the start:     |")
    print("  *----------------------------------------------------------------------------*\n\n")


def manager_menu():
    print("\n  *----------------------------------------------------------------------------*")
    print("  | Enter 1. for Logout:                                                       |")
    print("  | Enter 2. for Modification of personal data:                                |")
    print("  | Enter 3. for Registration of new sellers:                                  |")
    print("  | Enter 4. for Overview of available movies:                                 |")
    print("  | Enter 5. for Movie search:                                                 |")
    print("  | Enter 6. for Multi-criteria movie search:                                  |")
    print("  | Enter 7. to Add a New Movie:                                               |")
    print("  | Enter 8. for Search for the dates of cinema screenings:                    |")
    print("  | Enter 9. to get the Report:                                                |")
    print("  | Enter 10. for Display Royal Customers:                                     |")
    print("  | Enter 11. for Representation of seats in the form of a matrix:             |")
    print("  | Enter 12. to to Change Ticket Price:                                       |")
    print("  | Enter 13. to Modify the Movies:                                            |")
    print("  | Enter 14. to Delete the Movies:                                            |")
    print("  | Enter 15. to Add a New Projection:                                         |")
    print("  | Enter 16. to Modify the Projection:                                        |")
    print("  | Enter 17. to Delete the Projection:                                        |")
    print("  | Enter 18. to Displaying Balances on Customers Accounts:                    |")
    print("  *----------------------------------------------------------------------------*\n\n")


def modification_of_personal_data_menu():
    print("\n  *----------------------------------------------------------------------------*")
    print("  | Enter 1. to change the Name:                                               |")
    print("  | Enter 2. to change the Last name:                                          |")
    print("  | Enter 3. to change the Password:                                           |")
    print("  *----------------------------------------------------------------------------*\n\n")


def search_movie_by_criteria_menu():
    print("\n  *----------------------------------------------------------------------------*")
    print("  | Search movies by criteria:                                                 |")
    print("  | 1. Movie title:                                                            |")
    print("  | 2. Genre:                                                                  |")
    print("  | 3. Duration:                                                               |")
    print("  | 4. Director:                                                               |")
    print("  | 5. Main actors:                                                            |")
    print("  | 6. Country of origin:                                                      |")
    print("  | 7. Production year:                                                        |")
    print("  | 8. For exit from search:                                                   |")
    print("  *----------------------------------------------------------------------------*\n\n")


def search_for_terms_of_cinema_projections_menu():
    print("\n  *----------------------------------------------------------------------------*")
    print("  | Choose the search option:                                                  |")
    print("  | 1. Search by movie name:                                                   |")
    print("  | 2. Search by cinema hall:                                                  |")
    print("  | 3. Search by date:                                                         |")
    print("  | 4. Search by start and end time:                                           |")
    print("  | 5. Exit:                                                                   |")
    print("  *----------------------------------------------------------------------------*\n\n")


def reservation_tickets_registered_customer_menu():
    print("\n  *----------------------------------------------------------------------------*")
    print("  | Reservation Menu:                                                          |")
    print("  | 1. Search Projection Term:                                                 |")
    print("  | 2. Directly Enter Projection Code:                                         |")
    print("  | 0. Exit:                                                                   |")
    print("  *----------------------------------------------------------------------------*\n\n")


def display_tickets_seller_menu():
    print("\n  *----------------------------------------------------------------------------*")
    print("  | Display Menu:                                                              |")
    print("  | 1. Display tickets by Term Code:                                           |")
    print("  | 2. Enter the username to Display tickets for:                              |")
    print("  | 3. For all tickets in the system:                                          |")
    print("  | 0. Exit:                                                                   |")
    print("  *----------------------------------------------------------------------------*\n\n")


def sell_reserved_tickets_menu():
    print("\n  *----------------------------------------------------------------------------*")
    print("  | Sell Reserved Ticket Menu:                                                 |")
    print("  | 1. Display reserved tickets by Term Code:                                  |")
    print("  | 2. Display reserved tickets by Username:                                   |")
    print("  | 0. Exit:                                                                   |")
    print("  *----------------------------------------------------------------------------*\n\n")


def search_tickets_menu():
    print("\n  *----------------------------------------------------------------------------*")
    print("  | Search Ticket Menu:                                                        |")
    print("  | 1. Search by Term Code:                                                    |")
    print("  | 2. Search by Name and Last Name:                                           |")
    print("  | 3. Search by Date:                                                         |")
    print("  | 4. Search by Start Time:                                                   |")
    print("  | 5. Search by End Time:                                                     |")
    print("  | 6. Search by Status:                                                       |")
    print("  | 0. Exit:                                                                   |")
    print("  *----------------------------------------------------------------------------*\n\n")


def update_ticket_menu():
    print("\n  *----------------------------------------------------------------------------*")
    print("  | What would you like to update:                                             |")
    print("  | 1. Change the Term of Projection:                                          |")
    print("  | 2. Change the Account (name and last name):                                |")
    print("  | 3. Change the Seat:                                                        |")
    print("  | 0. Exit:                                                                   |")
    print("  *----------------------------------------------------------------------------*\n\n")


def report_menu():
    print(
        "\n  *------------------------------------------------------------------------------------------------------------------*")
    print(
        "  | Report Menu:                                                                                                     |")
    print(
        "  | 1. List of sold tickets for selected sale date (Report A):                                                       |")
    print(
        "  | 2. List of sold tickets for the selected term date (Report B):                                                   |")
    print(
        "  | 3. List of sold tickets for selected date of sale and selected seller (Report C):                                |")
    print(
        "  | 4. Total number and total price of tickets sold for the selected day (weekly) sales (Report D):                  |")
    print(
        "  | 5. Total number and total price of tickets sold for the selected day (weekly) terms (Report E):                  |")
    print(
        "  | 6. The total price of tickets sold for a given film in all cinema projections (Report F):                        |")
    print(
        "  | 7. Total number and total price of tickets sold for the selected day of sale and selected seller (Report G):     |")
    print(
        "  | 8. Total number and total price of sold tickets by sellers in the last 30 days (Report H):                       |")
    print(
        "  | 0. Exit                                                                                                          |")
    print(
        "  *--------------------------------------------------------------------------------------------------------------------*\n\n")


def cancel_ticket_reservation_menu():
    print("\n  *----------------------------------------------------------------------------*")
    print("  | Cancel Ticket Reservation Menu:                                            |")
    print("  | 1. Display tickets by Term ID:                                             |")
    print("  | 2. Enter the username to Display tickets for:                              |")
    print("  | 0. Exit:                                                                   |")
    print("  *----------------------------------------------------------------------------*\n\n")


def modify_cinema_projection():
    print("\n  *----------------------------------------------------------------------------*")
    print("  | Modify Cinema Projection Menu:                                             |")
    print("  | 1. Change Cinema Hall:                                                     |")
    print("  | 2. Change Days of Cinema Projection:                                       |")
    print("  | 3. Change Base Ticket Price:                                               |")
    print("  | 0. Exit:                                                                   |")
    print("  *----------------------------------------------------------------------------*\n\n")


def direct_ticket_sales_menu():
    print("\n  *----------------------------------------------------------------------------*")
    print("  | Direct Ticket Sales Menu:                                                  |")
    print("  | 1. Display terms by Search:                                                |")
    print("  | 2. Enter the Term ID directly:                                             |")
    print("  | 0. Exit:                                                                   |")
    print("  *----------------------------------------------------------------------------*\n\n")



