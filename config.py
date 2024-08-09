token = 'input your token'
provider_token = ''  # @BotFather -> Bot Settings -> Payments
admin_chat = 0  # admin chat ID
database_name = 'bot.db'

# menu

menu_descr = """Hello, {}! Please choose dishes from our menu."""

menu_item_descr = \
"""Name: *{}*
Description: {}
Price: {} RUB"""

# basket

basket_empty = 'Your basket is empty! Check out the menu to select dishes.'

confirm_descr = \
"""Thank you, your order is being prepared! To pick up your order, present its number. You can pay now via Yandex.Kassa or upon collection.
Order number: *{}*
You ordered:"""

admin_notification = \
"""Order number: *{}* {}
Name: {}
----------------"""

user_notification = \
"""Order number *{}* is ready {}!"""

# payments

card_disclaimer = \
"""This is a demo payment, no actual money will be charged. Use the test card number: `4242 4242 4242 4242`. The CVV can be any three digits."""

checkout_error = \
"""Aliens tried to steal your CVV code, but we successfully protected your data.
Please give us a moment to recover."""
