from datetime import datetime, timedelta
from twilio.rest import Client
import time

# Function to calculate time difference from a given start date
def calculate_time_difference(start_date):
    now = datetime.now()  # Get the current date and time
    delta = now - start_date  # Calculate the difference between now and the start date
    
    total_days = delta.days  # Total days passed
    total_weeks = total_days // 7  # Total weeks passed
    total_hours = delta.total_seconds() // 3600  # Total hours passed
    total_minutes = delta.total_seconds() // 60  # Total minutes passed
    total_seconds = delta.total_seconds()  # Total seconds passed
    
    return total_weeks, total_days, total_hours, total_minutes, total_seconds

# Function to send a WhatsApp message using the Twilio API
def send_whatsapp_message(message):
    # Twilio credentials
    account_sid = 'SID'  # Your Twilio Account SID
    auth_token = 'Token ID'  # Your Twilio Auth Token
    client = Client(account_sid, auth_token)

    # WhatsApp numbers
    from_whatsapp_number = 'whatsapp:+14155238886'  # Twilio WhatsApp sandbox number
    to_whatsapp_number = 'whatsapp:+919356379262'   # Your WhatsApp number

    # Send the message
    message = client.messages.create(body=message,
                                     from_=from_whatsapp_number,
                                     to=to_whatsapp_number)
    print(message.sid)

# Main function to run the script
def main():
    # Set the start date (e.g., July 25, 2024)
    start_date = datetime(2024, 7, 25)
    
    while True:
        # Calculate the time difference
        total_weeks, total_days, total_hours, total_minutes, total_seconds = calculate_time_difference(start_date)
        
        # Prepare the message content
        message_content = (f"Nofap Streak\n"
                           f"\n"
                           f"Time passed since {start_date.strftime('%Y-%m-%d')}:\n"
                           f"Total Weeks: {total_weeks}\n"
                           f"Total Days: {total_days}\n"
                           f"Total Hours: {int(total_hours)}\n"
                           f"Total Minutes: {int(total_minutes)}\n"
                           f"Total Seconds: {int(total_seconds)}")
        
        # Send the message via WhatsApp
        send_whatsapp_message(message_content)
        
        # Wait for 1 hour before sending the next message
        time.sleep(3600)

# Run the main function
if __name__ == "__main__":
    main()
