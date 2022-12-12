from datetime import datetime
import pytz

name = input("Enter your name please : ")
curr_time = datetime.now(pytz.timezone('Asia/Kolkata'))
hour = int(curr_time.strftime('%H'))

if(hour >= 5 and hour < 12):
    print(f"Hey {name} sir, Good morning!")

elif(hour >= 12 and hour < 16):
    print(f"Hey {name} sir, Good afternoon!")

elif(hour >= 16 and hour < 21):
    print(f"Hey {name} sir, Good evening!")

elif(hour >= 21 and hour < 5):
    print(f"Hey {name} sir, Good night!")

else:
    print(f"Hey {name} sir!")
