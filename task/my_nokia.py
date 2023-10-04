def nokia_function():
    print("""===list of menu function===
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
    response=int(input("Enter options:"))
    if response==1:
        print("""==Phonebook==
                1. Search
                2. Service Nos. 1
                3. Add name
                4. Erase
                5. Edit
                6. Assign tone
                7. Send b’card
                8. Options
                9. Speed dials
                10. Voice tags 
                11. Go back to main menu""")
        phonebook_response=int(input("Enter options"))
        if phonebook_response==1:
            print("search")
        elif phonebook_response==2:
            print("service Nos. 1")
        elif phonebook_response==3:
            print("Add name")
        elif phonebook_response==4:
            print("Erase")
        elif phonebook_response==5:
            print("Edit")
        elif phonebook_response==6:
            print("Assign tone")
        elif phonebook_response==7:
            print("Send b'card ")
        elif phonebook_response==8:
            print("""option 
            1.Type of view 
            2.Memory status""")
        option_response=int(input("Enter option:"))
        if option_response==1:
            print("Type of view")
        elif option_response==2:
            print("Memory status")
        elif phonebook_response ==9:
            print("Speed dials")
        elif phonebook_response == 10:
            print("Voice tags")
    if response==2:
        print("""
        ===Messages
         1.Write messages
         2.Inbox
         3.Outbox
         4.Picture messages
         5.Templates
         6.Smileys
         7.Message settings
         8.Info service
         9.voice mailbox number
         10.Service command editor
                                  """)
        message_response = int(input("Enter options"))
        if message_response==1:
            print("Write messages")
        elif message_response ==2:
            print("inbox")
        elif message_response==3:
            print("outbox")
        elif message_response==4:
            print("picture messages")
        elif message_response==5:
            print("Templates")
        elif message_response==6:
            print("Smiley")
        elif message_response==7:
            print("Message settings")
        elif message_response==8:
            print("Info service")
        elif message_response==9:
            print("Voice mailbox number")
        elif message_response==10:
            print("Service command editor")
    if response==3:
        print("chat")
    if response==4:
        print("""===Call register===
                1. Missed calls
                2. Received calls
                3. Dialled numbers
                4. Erase recent call lists
                5. Show call duration
                6.Show call costs
                7.Call cost settings
                8.prepaid credit
                                    """)
        callregister_response = int(input("Enter options"))
        if callregister_response==1:
            print("Missed calls")
        elif callregister_response==2:
            print("Received calls")
        elif callregister_response==3:
            print("Dialled numbers")
        elif callregister_response==4:
            print("Erase recent call lists")
        elif callregister_response==5:
            print("Show call duration")
        elif callregister_response==6:
            print("Show call costs")
        elif callregister_response==7:
            print("Call cost settings")
        elif callregister_response==8:
            print("prepaid credit")
    if response==5:
        print("""===Tones===
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
        tones_response = int(input("Enter options"))
        if tones_response==1:
            print("Ringing tone")
        elif tones_response==2:
            print("Ringing volume")
        elif tones_response==3:
            print("Incoming call alert")
        elif tones_response==4:
            print("Composer")
        elif tones_response==5:
            print("Message alert tone")
        elif tones_response==6:
            print("Keypad tones")
        elif tones_response==7:
            print("Warning and game tones")
        elif tones_response==8:
            print("Vibrating alert")
        elif tones_response==9:
            print("Screen saver")
    if response==6:
        print("""===settings===
                1.Call settings
                2.Phone settings
                3.Security settings
                4.Restore factory settings
                                  """)
        settings_response = int(input("Enter options"))
        if settings_response==1:
            print("Call settings")
        elif settings_response==2:
            print("Phone settings")
        elif settings_response==3:
            print("Security settings")
        elif settings_response==4:
            print("Restore factory settings")
    if response==7:
        print("Call divert")
    if response==8:
        print("Games")
    if response==9:
        print("Calculator")
    if response==10:
        print("Reminders")
    if response==11:
        print("""===Clock===
        1. Alarm clock
        2. Clock settings
        3. Date setting
        4. Stopwatch
        5. Countdown timer
        6. Auto update of date and time
                                     """)
        clock_response = int(input("Enter options"))
        if clock_response==1:
            print("Alarm clock")
        elif clock_response==2:
            print("Clock settings")
        elif clock_response==3:
            print("Date setting")
        elif clock_response==4:
            print("Stopwatch")
        elif clock_response==5:
            print("Countdown timer")
        elif clock_response==6:
            print("Auto update of date and time")
    if response==12:
        print("Profiles")
    if response==13:
        print("Sim services")

nokia_function()



