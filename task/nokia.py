












def main_menu():
    print("""
    1. Phone book
    2. Messages
    3. Chat
    4. Call Register
    5. Tones
    6. Settings
    7. Call Divert
    8. Games
    9. Calculator
    10. Reminders
    11. Clock
    12. Profiles
    13. SIM services
    """)
    response = input()


    if response == '1':
        phone_book()
    elif response == '2':
        messages()
    elif response == '3':
        chat()
    elif response == '4':
        call_register()
    elif response == '5':
        tones()
    elif response == '6':
        settings()
    elif response == '7':
        call_divert()
    elif response == '8':
        games()
    elif response == '9':
        calculator()
    elif response == '10':
        reminders()
    elif response == '11':
        clock()
    elif response == '12':
        profile()
    elif response == '13':
        sim_services()

def sim_services():

        print("""
        Press 01 for SIM services
        Press 00 for Main Menu
        """)
        response = input()
        if response == '01':
            sim_services()
        elif response == '00':
            main_menu()
        else:
            main_menu()

def profile():
        print("""
        Press 01 for Profile
        Press 00 for Main Menu
        """)
        response = input()
        if response == '01':
            profile()
        elif response == '00':
            main_menu()
        else:
            main_menu()

def clock():
        print("""
        1. Alarm clock
        2. Clock settings
        3. Date setting
        4. Stopwatch
        5. Countdown timer
        6. Auto update of date and time
        """)
        response = input()
        if response == '1':
            alarm_clock()
        elif response == '2':
            clock_settings()
        elif response == '3':
            date_setting()
        elif response == '4':
            stopwatch()
        elif response == '5':
            countdown_timer()
        elif response == '6':
            auto_update_of_date_and_time()

def auto_update_of_date_and_time():
        print("""
        Press 01 for Clock
        Press 00 for Main Menu
        """)
        response = input()
        if response == '01':
            clock()
        elif response == '00':
            main_menu()
        else:
            main_menu()

def countdown_timer():
        print("""
        Press 01 for Clock
        Press 00 for Main Menu
        """)
        response = input()
        if response == '01':
            clock()
        elif response == '00':
            main_menu()
        else:
            main_menu()


def stopwatch():
    print("""
    Press 01 for Clock
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        clock()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def date_setting():
    print("""
    Press 01 for Clock
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        clock()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def clock_settings():
    print("""
    Press 01 for Clock
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        clock()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def alarm_clock():
    print("""
    Press 01 for Clock
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        clock()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def reminders():
    print("""
    Press 01 for Reminders
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        reminders()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def calculator():
    print("""
    Press 01 for Calculator
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        calculator()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def games():
    print("""
    Press 01 for Games
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        games()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def call_divert():
    print("""
    Press 01 for Call Divert
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        call_divert()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def settings():
    print("""
    1. Call Settings
    2. Phone Settings
    3. Security Settings
    4. Restore Factory Settings
    """)
    response = input()
    if response == '1':
        call_settings()
    elif response == '2':
        phone_settings()
    elif response == '3':
        security_settings()
    elif response == '4':
        restore_factory_settings()

def restore_factory_settings():
    print("""
    Press 01 for Settings
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        settings()
    elif response == '00':
        main_menu()
    else:
        main_menu()
def security_settings():
    print("""
    1. PIN code request
    2. Call barring service
    3. Fixed dialling
    4. Closed user group
    5. Phone security
    6. Change access codes
    """)
    response = input()
    if response == '1':
        pin_code_request()
    elif response == '2':
        call_barring_service()
    elif response == '3':
        fixed_dialling()
    elif response == '4':
        closed_user_group()
    elif response == '5':
        phone_security()
    elif response == '6':
        change_access_codes()

def change_access_codes():
    print("""
    Press 01 for Settings
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        settings()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def phone_security():
    print("""
    Press 01 for Settings
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        settings()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def closed_user_group():
    print("""
    Press 01 for Settings
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        settings()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def fixed_dialling():
    print("""
    Press 01 for Settings
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        settings()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def call_barring_service():
    print("""
    Press 01 for Settings
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        settings()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def pin_code_request():
    print("""
    Press 01 for Settings
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        settings()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def phone_settings():
    print("""
    1. Language
    2. Cell info display
    3. Welcome note
    4. Network selection
    5. Lights
    6. Confirm SIM service actions
    """)
    response = input()
    if response == '1':
        language()
    elif response == '2':
        cell_info_display()
    elif response == '3':
        welcome_note()
    elif response == '4':
        network_selection()
    elif response == '5':
        lights()
    elif response == '6':
        confirm_sim_service_action()

def confirm_sim_service_action():
    print("""
    Press 01 for Settings
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        settings()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def lights():
    print("""
    Press 01 for Settings
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        settings()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def network_selection():
    print("""
    Press 01 for Settings
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        settings()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def welcome_note():
    print("""
    Press 01 for Settings
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        settings()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def cell_info_display():
    print("""
    Press 01 for Settings
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        settings()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def language():
    print("""
    Press 01 for Settings
    Press 00 for Main Menu
    """)
    response = input()
    if response == '01':
        settings()
    elif response == '00':
        main_menu()
    else:
        main_menu()

def call_settings():
    print("""
    1. Automatic redial
    2. Speed dialling
    3. Call waiting options
    4. Own number sending
    5. Phone line in use
    6. Automatic answer
    """)
    response = input()
    if response == '1':
        automatic_redial()
    elif response == '2':
        speed_dialling()
    elif response == '3':
        call_waiting_options()
    elif response == '4':
        own_number_sending()
    elif response == '5':
        phone_line_in_use()
    elif response == '6':
        automatic_answer()

def automatic_answer():
    print("""
    Press 01 for Settings
    Press 00 for Main Menu
    """)
    response = input()
    if response == ' 01':
        settings()
    elif response == '00':
        main_menu()
    else:
        main_menu()


def phone_line_in_use():
    print("""
            press 1 for settings
            press 00 for main menu
            """)
    response = int(input())
    if response == 1:
        settings()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def own_number_sending():
    print("""
            press 1 for settings
            press 00 for main menu
            """)
    response = int(input())
    if response == 1:
        settings()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def call_waiting_options():
    print("""
            press 1 for settings
            press 00 for main menu
            """)
    response = int(input())
    if response == 1:
        settings()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def speed_dialling():
    print("""
            press 1 for settings
            press 00 for main menu
            """)
    response = int(input())
    if response == 1:
        settings()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def automatic_redial():
    print("""
            press 1 for settings
            press 00 for main menu
            """)
    response = int(input())
    if response == 1:
        settings()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def tones():
    print("""
            1. Ringing tone
            2. Ringing volume
            3. Incoming call alert
            4. Composer
            5. Message alert tone
            6. Keypad tones
            7. Warning and game tones
            8. Vibrating alert
            9. Screen saver
                 """)
    response = int(input())
    if response == 1:
        ringing_tone()
    elif response == 2:
        ringing_volume()
    elif response == 3:
        incoming_call_alert()
    elif response == 4:
        composer()
    elif response == 5:
        message_alert_tone()
    elif response == 6:
        keypad_tones()
    elif response == 7:
        warning_and_game_tones()
    elif response == 8:
        vibrating_alert()
    elif response == 9:
        screen_saver()


def screen_saver():
    print("""
            screen saver
            press 1 for tones
            press 00 for main menu
            """)
    response = int(input())
    if response == 1:
        tones()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def vibrating_alert():
    print("""
            vibrating alert
            press 1 for tones
            press 00 for main menu
            """)
    response = int(input())
    if response == 1:
        tones()
    elif response == 00:
        main_menu()
    else:
        main_menu()






def warning_and_game_tones():
    print("""
            warning and game tones
            press 1 for tones
            press 00 for main menu
            """)
    response = int(input())
    if response == 1:
        tones()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def keypad_tones():
    print("""
            keypad tones
            press 1 for tones
            press 00 for main menu
            """)
    response = int(input())
    if response == 1:
        tones()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def message_alert_tone():
    print("""
            message alert tone
            press 1 for tones
            press 00 for main menu
            """)
    response = int(input())
    if response == 1:
        tones()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def composer():
    print("""
            composer
            press 1 for tones
            press 00 for main menu
            """)
    response = int(input())
    if response == 1:
        tones()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def incoming_call_alert():
    print("""
            incoming call alert
            press 1 for tones
            press 00 for main menu
            """)
    response = int(input())
    if response == 1:
        tones()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def ringing_volume():
    print("""
           ringing volume
            press 1 for tones
            press 00 for main menu
            """)
    response = int(input())
    if response == 1:
        tones()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def ringing_tone():
    print("""
            ringing tone
            press 1 for tones
            press 00 for main menu
            """)
    response = int(input())
    if response == 1:
        tones()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def dialled_numbers():
    print("""
               dialled numbers
               press 1 for call register
               press 00 for main menu
               """)
    response = int(input())
    if response == 1:
        call_register()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def call_register():
    print("""
            1. Missed calls
            2. Received calls
            3. Dialled numbers
            4. Erase recent call lists
            5. Show call duration
            6. Show call costs
            7. Call cost settings
            8. Prepaid credit
            """)
    response = int(input())
    if response == 1:
        missed_calls()
    elif response == 2:
        received_calls()
    elif response == 3:
        dialled_numbers()
    elif response == 4:
        erase_recent_call_lists()
    elif response == 5:
        show_call_duration()
    elif response == 6:
        show_call_costs()
    elif response == 7:
        call_cost_settings()
    elif response == 8:
        prepaid_credit()


def prepaid_credit():
    print("""
           prepaid credit
           press 1 for call register
           press 00 for main menu
           """)
    response = int(input())
    if response == 1:
        call_register()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def call_cost_settings():
    print("""
            1. Call cost limit
            2. Show costs in
            """)
    response = int(input())
    if response == 1:
        call_cost_limit()
    elif response == 2:
        show_costs_in()


def show_costs_in():
    print("""
            show cost in
            press 1 for call register
            press 00 for main menu
            """)
    response = int(input())
    if response == 1:
        call_register()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def call_cost_limit():
    print("""
            call cost limit
            press 1 for call register
            press 00 for main menu
            """)
    response = int(input())
    if response == 1:
        call_register()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def show_call_costs():
    print("""
            1. Last call cost
            2. All calls’ cost
            3. Clear counters
            """)
    response = int(input())
    if response == 1:
        last_call_cost()
    elif response == 2:
        all_calls_cost()
    elif response == 3:
        clear_counters()


def clear_counters():
    print("""
           clear counters
            press 1 for call register
            press 00 for main menu
            """)
    response = int(input())
    if response == 1:
        call_register()
    elif response == 00:
        main_menu()
    else:
        main_menu()



def all_calls_cost():
    print("""
            all calls cost
            press 1 for call register
            press 00 for main menu
            """)
    response = int(input())
    if response == 1:
        call_register()
    elif response == 00:
        main_menu()
    else:
        main_menu()

def last_call_cost():
    print("""
            last call cost
            press 1 for call register
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        call_register()
    elif response == 00:
        main_menu()
    else:
        main_menu()

def show_call_duration():
    print("""
            1. Last call duration
            2. All calls’ duration
            3. Received calls’ duration
            4. Dialled calls’ duration
            5. Clear timers
            """)
    response = int(input())
    if response == 1:
        last_call_duration()
    elif response == 2:
        all_calls_duration()
    elif response == 3:
        received_calls_duration()
    elif response == 4:
        dialled_calls_duration()
    elif response == 5:
        clear_timer()

def clear_timer():
    print("""
             clear timer
            press 1 for call register
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        call_register()
    elif response == 00:
        main_menu()
    else:
        main_menu()

def dialled_calls_duration():
    print("""
             dialled calls duration
             press 01 for call register
             press 00 for mainMenu
             """)
    response = int(input())
    if response == 1:
        call_register()
    elif response == 00:
        main_menu()
    else:
        main_menu()

def received_calls_duration():
    print("""
            received calls duration
            press 1 for call register
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        call_register()
    elif response == 00:
        main_menu()
    else:
        main_menu()

def all_calls_duration():
    print("""
            all calls duration
            press 1 for call register
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        call_register()
    elif response == 00:
        main_menu()
    else:
        main_menu()

def last_call_duration():
    print("""
            last call duration
            press 1 for call register
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        call_register()
    elif response == 00:
        main_menu()
    else:
        main_menu()

def erase_recent_call_lists():
    print("""
             erase recent call lists
             press 1 for call register
             press 00 for mainMenu
             """)
    response = int(input())
    if response == 1:
        call_register()
    elif response == 00:
        main_menu()
    else:
        main_menu()

def dialled_number():
    print("""
             dialled number
             press 1 for call register
             press 00 for mainMenu
             """)
    response = int(input())
    if response == 1:
        call_register()
    elif response == 00:
        main_menu()
    else:
        main_menu()

def received_calls():
    print("""
            received calls
            press 1 for call register
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        call_register()
    elif response == 00:
        main_menu()
    else:
        main_menu()

def missed_calls():
    print("""
            missed calls
            press 1 for call register
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        call_register()
    elif response == 00:
        main_menu()
    else:
        main_menu()

def chat():
    print("""
            chat
            press 1 for chat
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        chat()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def messages():
    print("""
            1. Write messages
            2. Inbox
            3. Outbox
            4. Picture messages
            5. Templates
            6. Smileys
            7. Message settings
            8. Info service
            9. Voice mailbox number
            10. Service command editor
            """)
    response = int(input())
    if response == 1:
        write_messages()
    elif response == 2:
        inbox()
    elif response == 3:
        outbox()
    elif response == 4:
        picture_messages()
    elif response == 5:
        templates()
    elif response == 6:
        smileys()
    elif response == 7:
        message_settings()
    elif response == 8:
        info_service()
    elif response == 9:
        voice_mailbox_number()
    elif response == 10:
        service_command_editor()


def service_command_editor():
    print("""
            service command editor
            press 1 for messages
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        messages()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def voice_mailbox_number():
    print("""
            voice mailbox number
            press 1 for messages
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        messages()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def info_service():
    print("""
            info service 
             press 1 for messages
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        messages()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def message_settings():
    print("""
            press
            1. Set 1
            2. Common
            """)
    response = int(input())
    if response == 1:
        set1()
    elif response == 2:
        common()


def common():
    print("""
            1. Delivery reports
            2. Reply via same centre
            3. Character support
            """)
    response = int(input())
    if response == 1:
        delivery_reports()
    elif response == 2:
        reply_via_same_centre()
    elif response == 3:
        character_support()


def character_support():
    print("""
            character support
             press 1 for messages
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        messages()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def reply_via_same_centre():
    print("""
            reply via same centre
            press 1 for messages
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        messages()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def delivery_reports():
    print("""
            delivery reports
            press 1 for messages
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        messages()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def message_centre_number():
    print(""" message centre number
            press 1 for messages
            press 00 for mainMenu""")
    response = int(input())
    if response == 1:
        messages()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def message_sent_as():
    print("""message sent as
            press 1 for messages
            press 00 for mainMenu""")
    response = int(input())
    if response == 1:
        messages()
    elif response == 00:
        main_menu()
    else:
        main_menu()

def set1():
    print("""
            1. Message centre number
            2. Messages sent as
            3. Message validity
            """)
    response = int(input())
    if response == 1:
        message_centre_number()
    elif response == 2:
        message_sent_as()
    elif response == 3:
        message_validity()


def message_validity():
    print("""
            message validity
            press 1 for messages
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        messages()
    elif response == 00:
        main_menu()
    else:
        main_menu()





def phone_book_option():
    print("""
            1. Type of view
            2. Memory status
            """)
    response = int(input())
    if response == 1:
        type_of_view()
    elif response == 2:
        memory_status()


def memory_status():
    print("""
            memory status
            press 1 for phone book
            press 00 for MainMenu
            """)
    response = int(input())
    if response == 1:
        phone_book()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def type_of_view():
    print("""
            type of view
            press 1 for phone book
            press 00 for MainMenu
            """)
    response = int(input())
    if response == 1:
        phone_book()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def search():
    print("""
            search
            press 1 for phone book
            press 00 for MainMenu
            """)
    response = int(input())
    if response == 1:
        phone_book()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def service_nos():
    print("""
            service nos
            press 1 for phone book
            press 00 for MainMenu
            """)
    response = int(input())
    if response == 1:
        phone_book()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def add_name():
    print("""
            add name
            press 1 for phone book
            press 00 for MainMenu
            """)
    response = int(input())
    if response == 1:
        phone_book()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def erase():
    print("""
            erase
            press 1 for phone book
            press 00 for MainMenu
            """)
    response = int(input())
    if response == 1:
        phone_book()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def edit():
    print("""
            edit
            press 1 for phone book
            press 00 for MainMenu
            """)
    response = int(input())
    if response == 1:
        phone_book()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def assign_tone():
    print("""
            assign tone
            press 1 for phone book
            press 00 for MainMenu
            """)
    response = int(input())
    if response == 1:
        phone_book()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def send_b_card():
    print("""
            send b card 
            press 1 for phone book
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        phone_book()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def speed_dials():
    print("""
            speed dials
            press 1 for phone book
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        phone_book()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def voice_tags():
    print("""
            voice tags
            press 1 for phone book
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        phone_book()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def phone_book():
    print("""
            1. Search
            2. Service Nos. 1
            3. Add name
            4. Erase
            5. Edit
            6. Assign tone
            7. Send b’card
            8. Options
            9. Speed Dial
            10. Voice Tag
            """)
    response = int(input())
    if response == 1:
        search()
    elif response == 2:
        service_nos()
    elif response == 3:
        add_name()
    elif response == 4:
        erase()
    elif response == 5:
        edit()
    elif response == 6:
        assign_tone()
    elif response == 7:
        send_b_card()
    elif response == 8:
        phone_book_option()
    elif response == 9:
        speed_dials()
    elif response == 10:
        voice_tags()


def write_messages():
    print("""
            write messages
            press 1 for messages
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        messages()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def inbox():
    print("""
            inbox
            press 1 for messages
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        messages()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def outbox():
    print("""
            outbox
            press 1 for messages
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        messages()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def picture_messages():
    print("""
            picture messages
            press 1 for messages
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        messages()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def templates():
    print("""
            templates
            press 1 for messages
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        messages()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def smileys():
    print("""
            smiley
            press 1 for messages
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        messages()
    elif response == 00:
        main_menu()
    else:
        main_menu()





def common():
    print("""
            1. Delivery reports
            2. Reply via same centre
            3. Character support
            """)
    response = int(input())
    if response == 1:
        delivery_reports()
    elif response == 2:
        reply_via_same_centre()
    elif response == 3:
        character_support()


def character_support():
    print("""
            character support
            press 1 for messages
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        messages()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def reply_via_same_centre():
    print("""
            reply via same centre
            press 1 for messages
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        messages()
    elif response == 00:
        main_menu()
    else:
        main_menu()


def delivery_reports():
    print("""
            delivery reports
            press 1 for messages
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        messages()
    elif response == 00:
        main_menu()
    else:
        main_menu()





def message_validity():
    print("""
            message validity
            press 1 for messages
            press 00 for mainMenu
            """)
    response = int(input())
    if response == 1:
        messages()
    elif response == 00:
        main_menu()
    else:
        main_menu()





main_menu()
