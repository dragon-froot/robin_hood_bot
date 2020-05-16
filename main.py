from argparse import ArgumentParser
from stocks import Stocks

# THis is where the script will get the user credentials
parser = ArgumentParser(description="You will include the email and password to login to this")
email = parser.add_argument("-e", "--email",
                            action="store_true", dest="rank", default=False,
                            help="This is where you will include your email ")
password = parser.add_argument("-p", "--password",
                            action="store_true", dest="rank", default=False,
                            help="This is where you will include your password")

        


if __name__ == "__main__":
    main = Stocks(email, password)
    main.login()
    while True:
        main.get_owned_stocks()
    


