from booking.bookings import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='INR')
        bot.select_place_to_go(input("Where do you want to go ?"))
        bot.select_dates(check_in_date=input("What is the check in date ?"),
                         check_out_date=input("What is the check out date ?"))
        bot.select_adults(int(input("Enter the number of people:")))
        bot.click_search()
        bot.apply_filtrations()
        bot.refresh()
        bot.report_results()

except Exception as e:
    if 'in PATH' in str(e):
        print("Error"
        )
    else:
        raise