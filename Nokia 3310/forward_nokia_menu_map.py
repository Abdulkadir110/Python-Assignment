menu_functions = """
    Welcome to the Menu functions

    Press 1 : Phone book
    Press 2 : Messages
    Press 3 : Chat
    Press 4 : Call register
    Press 5 : Tones
    Press 6 : Settings
    Press 7 : Call divert
    Press 8 : Games
    Press 9 : Calculator
    Press 10 : Remainders
    Press 11 : Clock
    Press 12 : Profiles
    Press 13 : SIM services
"""

print(menu_functions)

menu_functions_choice = int(input("Press a number: "))

match menu_functions_choice:
    case 1:
        print("Phone book")

        phone_book = """
            Press 1 : Search
            Press 2 : Service Nos
            Press 3 : Add name
            Press 4 : Erase
            Press 5 : Edit
            Press 6 : Assign
            Press 7 : Send b'card
            Press 8 : Options
            Press 9 : Speed dials
            Press 10 : Voice tags
        """
        print(phone_book)
        phone_book_choice = int(input("Press a number: "))

        match phone_book_choice:
            case 8:
                print("Options")

                options_choice = """
                    Press 1 : Type of view
                    Press 2 : Memory
                """
                print(options_choice)
            case _:
                print("Invalid choice.")

    case 2:
        print("Messages")

        messages = """
            Press 1 : Write messages
            Press 2 : Inbox
            Press 3 : Outbox
            Press 4 : Picture messages
            Press 5 : Templates
            Press 6 : Smileys
            Press 7 : Message settings
            Press 8 : Info service
            Press 9 : Voice mailbox number
            Press 10 : Service command editor
        """
        print(messages)
        messages_settings_choice = int(input("Press a number: "))

        match messages_settings_choice:
            case 7:
                print("Message settings")

                messages_settings = """
                    Press 1 : Set 1
                    Press 2 : Common
                """
                print(messages_settings)
                messages_settings_choice_choices = int(input("Press a number: "))

                match messages_settings_choice_choices:
                    case 1:
                        print("Set 1")

                        messages_set_one_settings = """
                            Press 1 : Message centre number
                            Press 2 : Messages sent as
                            Press 3 : Messages validity
                        """
                        print(messages_set_one_settings)

                    case 2:
                        print("Common")

                        messages_common_settings = """
                            Press 1 : Delivery reports
                            Press 2 : Reply via same centre
                            Press 3 : Character support
                        """
                        print(messages_common_settings)

                    case _:
                        print("Invalid choice.")
            case _:
                print("Invalid choice.")

    case 3:
        print("Chat")

    case 4:
        print("Call register")
        call_register = """
            Press 1 : Missed calls
            Press 2 : Received calls
            Press 3 : Dialed numbers
            Press 4 : Erase recent call lists
            Press 5 : Show call duration
            Press 6 : Show call costs
            Press 7 : Call cost settings
            Press 8 : Prepaid credits
        """
        print(call_register)
        show_call_duration = int(input("Press a number: "))

        match show_call_duration:
            case 5:
                print("Show call duration")
                show_call_duration_choice = """
                    Press 1 : last call duration
                    Press 2 : All calls' duration
                    Press 3 : Received calls' duration
                    Press 4 : Dialled calls' duration
                    Press 5 : Clear timers
                """
                print(show_call_duration_choice)

            case 6:
                print("Show call costs")
                show_call_costs_choice = """
                    Press 1 : last call cost
                    Press 2 : All calls' cost
                    Press 3 : Clear counters
                """
                print(show_call_costs_choice)

            case 7:
                print("Call cost settings")
                call_cost_settings = """
                    Press 1 : Call cost limit
                    Press 2 : Show costs in
                """
                print(call_cost_settings)

            case 8:
                print("Prepaid credit")

            case _:
                print("Invalid choice.")

    case 5:
        print("Tones")
        tones = """
            Press 1 : Ringing tone
            Press 2 : Ringing volume
            Press 3 : Incoming call alert
            Press 4 : Composer
            Press 5 : Message alert tone
            Press 6 : Keypad tones
            Press 7 : Warning and game tones
            Press 8 : Vibration alert
            Press 9 : Screen saver
        """
        print(tones)

    case 6:
        print("Settings")
        settings_choice = """
            Press 1 : Call settings
            Press 2 : Phone settings
            Press 3 : Security settings
            Press 4 : Restore factory settings
        """
        print(settings_choice)
        settings_choice_choices = int(input("Press a number: "))

        match settings_choice_choices:
            case 1:
                print("Call settings")
                call_settings = """
                    Press 1 : Automatic redial
                    Press 2 : Speed dialing
                    Press 3 : Call waiting options
                    Press 4 : Own number sending
                    Press 5 : Phone line in use
                    Press 6 : Automatic answer
                """
                print(call_settings)

            case 2:
                print("Phone settings")
                phone_settings = """
                    Press 1 : Language
                    Press 2 : Cell info display
                    Press 3 : Welcome note
                    Press 4 : Network selection
                    Press 5 : Lights
                    Press 6 : Confirm SIM service actions
                """
                print(phone_settings)

            case 3:
                print("Security settings")
                security_settings = """
                    Press 1 : PIN code request
                    Press 2 : Call barring service
                    Press 3 : Fixed dialing
                    Press 4 : Closed user group
                    Press 5 : Phone security
                    Press 6 : Change access codes
                """
                print(security_settings)

            case 4:
                print("Restore factory settings")

            case 7:
                print("Call divert")

            case _:
                print("Invalid choice.")

    case 7:
        print("Call divert")

    case 8:
        print("Games")

    case 9:
        print("Calculator")

    case 10:
        print("Remainders")

    case 11:
        print("Clock")
        Clock = """
            Press 1 : Alarm clock
            Press 2 : Clock settings
            Press 3 : Date settings
            Press 4 : Stop watch
            Press 5 : Countdown timer
            Press 6 : Auto update of date and time
        """
        print(Clock)

    case 12:
        print("Profiles")

    case 13:
        print("SIM services")

    case _:
        print("Invalid choice.")
