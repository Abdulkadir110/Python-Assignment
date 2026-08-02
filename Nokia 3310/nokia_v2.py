is_running = True

while is_running:
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
Press 0: End
"""

    print(menu_functions)

    menu_functions_choice = int(input("Press a number: "))

    match menu_functions_choice:
        case 1:
            is_phone_book = True
            while is_phone_book:
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
                    Press 0 : Back to Main-menu
                """
                print(phone_book)
                
                phone_book_choice = int(input("Press a number: "))
                
                match phone_book_choice:
                    case 8:
                        is_options = True
                        while is_options:
                            print("Options")

                            options_choice = """
                                Press 1 : Type of view
                                Press 2 : Memory
                                Press 0 : Back
                            """
                            print(options_choice)
                            options_choice_pick = int(input("Press a number: "))

                            match options_choice_pick:
                                case 1:
                                    print("Type of view")
                                case 2:
                                    print("Memory")
                                case 0:
                                    is_options = False
                                case _:
                                    print("Invalid choice.")

                    case 0:
                        is_phone_book = False

                    case _:
                        print("Invalid choice.")

        case 2:
            is_messages = True
            while is_messages:
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
                    Press 0 : Back to Main-menu
                """
                print(messages)
                messages_settings_choice = int(input("Press a number: "))

                match messages_settings_choice:
                    case 7:
                        is_message_settings = True
                        while is_message_settings:
                            print("Message settings")

                            messages_settings = """
                                Press 1 : Set 1
                                Press 2 : Common
                                Press 0 : Back
                            """
                            print(messages_settings)
                            messages_settings_choice_choices = int(input("Press a number: "))

                            match messages_settings_choice_choices:
                                case 1:
                                    is_set_one = True
                                    while is_set_one:
                                        print("Set 1")

                                        messages_set_one_settings = """
                                            Press 1 : Message centre number
                                            Press 2 : Messages sent as
                                            Press 3 : Messages validity
                                            Press 0 : Back
                                        """
                                        print(messages_set_one_settings)
                                        set_one_pick = int(input("Press a number: "))

                                        match set_one_pick:
                                            case 1:
                                                print("Message centre number")
                                            case 2:
                                                print("Messages sent as")
                                            case 3:
                                                print("Messages validity")
                                            case 0:
                                                is_set_one = False
                                            case _:
                                                print("Invalid choice.")

                                case 2:
                                    is_common = True
                                    while is_common:
                                        print("Common")

                                        messages_common_settings = """
                                            Press 1 : Delivery reports
                                            Press 2 : Reply via same centre
                                            Press 3 : Character support
                                            Press 0 : Back
                                        """
                                        print(messages_common_settings)
                                        common_pick = int(input("Press a number: "))

                                        match common_pick:
                                            case 1:
                                                print("Delivery reports")
                                            case 2:
                                                print("Reply via same centre")
                                            case 3:
                                                print("Character support")
                                            case 0:
                                                is_common = False
                                            case _:
                                                print("Invalid choice.")

                                case 0:
                                    is_message_settings = False

                                case _:
                                    print("Invalid choice.")

                    case 0:
                        is_messages = False

                    case _:
                        print("Invalid choice.")

        case 3:
            print("Chat")

        case 4:
            is_call_register = True
            while is_call_register:
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
                    Press 0 : Back to Main-menu
                """
                print(call_register)
                call_register_choice = int(input("Press a number: "))

                match call_register_choice:
                    case 1:
                        print("Missed calls")

                    case 2:
                        print("Received calls")

                    case 3:
                        print("Dialed numbers")

                    case 4:
                        print("Erase recent call lists")

                    case 5:
                        is_call_duration = True
                        while is_call_duration:
                            print("Show call duration")
                            show_call_duration_choice = """
                                Press 1 : last call duration
                                Press 2 : All calls' duration
                                Press 3 : Received calls' duration
                                Press 4 : Dialled calls' duration
                                Press 5 : Clear timers
                                Press 0 : Back
                            """
                            print(show_call_duration_choice)
                            call_duration_pick = int(input("Press a number: "))

                            match call_duration_pick:
                                case 1:
                                    print("Last call duration")
                                case 2:
                                    print("All calls' duration")
                                case 3:
                                    print("Received calls' duration")
                                case 4:
                                    print("Dialled calls' duration")
                                case 5:
                                    print("Clear timers")
                                case 0:
                                    is_call_duration = False
                                case _:
                                    print("Invalid choice.")

                    case 6:
                        is_call_costs = True
                        while is_call_costs:
                            print("Show call costs")
                            show_call_costs_choice = """
                                Press 1 : last call cost
                                Press 2 : All calls' cost
                                Press 3 : Clear counters
                                Press 0 : Back
                            """
                            print(show_call_costs_choice)
                            call_costs_pick = int(input("Press a number: "))

                            match call_costs_pick:
                                case 1:
                                    print("Last call cost")
                                case 2:
                                    print("All calls' cost")
                                case 3:
                                    print("Clear counters")
                                case 0:
                                    is_call_costs = False
                                case _:
                                    print("Invalid choice.")

                    case 7:
                        is_call_cost_settings = True
                        while is_call_cost_settings:
                            print("Call cost settings")
                            call_cost_settings = """
                                Press 1 : Call cost limit
                                Press 2 : Show costs in
                                Press 0 : Back
                            """
                            print(call_cost_settings)
                            call_cost_settings_pick = int(input("Press a number: "))

                            match call_cost_settings_pick:
                                case 1:
                                    print("Call cost limit")
                                case 2:
                                    print("Show costs in")
                                case 0:
                                    is_call_cost_settings = False
                                case _:
                                    print("Invalid choice.")

                    case 8:
                        print("Prepaid credit")

                    case 0:
                        is_call_register = False

                    case _:
                        print("Invalid choice.")

        case 5:
            is_tones = True
            while is_tones:
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
                    Press 0 : Back to Main-menu
                """
                print(tones)
                tones_pick = int(input("Press a number: "))

                match tones_pick:
                    case 0:
                        is_tones = False
                    case _:
                        print("Invalid choice.")

        case 6:
            is_settings = True
            while is_settings:
                print("Settings")
                settings_choice = """
                    Press 1 : Call settings
                    Press 2 : Phone settings
                    Press 3 : Security settings
                    Press 4 : Restore factory settings
                    Press 0 : Back to Main-menu
                """
                print(settings_choice)
                settings_choice_choices = int(input("Press a number: "))

                match settings_choice_choices:
                    case 1:
                        is_call_settings = True
                        while is_call_settings:
                            print("Call settings")
                            call_settings = """
                                Press 1 : Automatic redial
                                Press 2 : Speed dialing
                                Press 3 : Call waiting options
                                Press 4 : Own number sending
                                Press 5 : Phone line in use
                                Press 6 : Automatic answer
                                Press 0 : Back
                            """
                            print(call_settings)
                            call_settings_pick = int(input("Press a number: "))

                            match call_settings_pick:
                                case 0:
                                    is_call_settings = False
                                case _:
                                    print("Invalid choice.")

                    case 2:
                        is_phone_settings = True
                        while is_phone_settings:
                            print("Phone settings")
                            phone_settings = """
                                Press 1 : Language
                                Press 2 : Cell info display
                                Press 3 : Welcome note
                                Press 4 : Network selection
                                Press 5 : Lights
                                Press 6 : Confirm SIM service actions
                                Press 0 : Back
                            """
                            print(phone_settings)
                            phone_settings_pick = int(input("Press a number: "))

                            match phone_settings_pick:
                                case 0:
                                    is_phone_settings = False
                                case _:
                                    print("Invalid choice.")

                    case 3:
                        is_security_settings = True
                        while is_security_settings:
                            print("Security settings")
                            security_settings = """
                                Press 1 : PIN code request
                                Press 2 : Call barring service
                                Press 3 : Fixed dialing
                                Press 4 : Closed user group
                                Press 5 : Phone security
                                Press 6 : Change access codes
                                Press 0 : Back
                            """
                            print(security_settings)
                            security_settings_pick = int(input("Press a number: "))

                            match security_settings_pick:
                                case 0:
                                    is_security_settings = False
                                case _:
                                    print("Invalid choice.")

                    case 4:
                        print("Restore factory settings")

                    case 0:
                        is_settings = False

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
            is_clock = True
            while is_clock:
                print("Clock")
                Clock = """
                    Press 1 : Alarm clock
                    Press 2 : Clock settings
                    Press 3 : Date settings
                    Press 4 : Stop watch
                    Press 5 : Countdown timer
                    Press 6 : Auto update of date and time
                    Press 0 : Back to Main-menu
                """
                print(Clock)
                clock_pick = int(input("Press a number: "))

                match clock_pick:
                    case 0:
                        is_clock = False
                    case _:
                        print("Invalid choice.")

        case 12:
            print("Profiles")

        case 13:
            print("SIM services")

        case 0:
            is_running = False
            print("---Loading...----Back To Home-------")

        case _:
            print("Invalid choice.")





