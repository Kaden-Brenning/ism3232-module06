# appointment_main.py
# Author: Kaden Brenning

from appointment_bot import AppointmentHelper
from appointment_tool import AppointmentBook
from appointment_toolbox import AppointmentToolbox
from booking_queue import BookingQueue
from ollama_model import OllamaModel

OPEN_TIMES = {
    "monday": "3:30 pm",
    "wednesday": "10:00 am and 11:30 am",
    "friday": "1:00 pm and 4:00 pm",
}

INSTRUCTIONS = """You are Steve, an assistant for Bayside Tax Help.
Answer in one short sentence.
If the client only says hello, greet them and ask how you can help.
The office is at 91 Southlake Street, on the fourth floor.
Bring a photo ID and last year's tax return to your appointment.
To request a booking you need the day, the time, and the client's full name.
Only state facts that appear in these instructions or in tool results.
If you do not know, say you do not know and offer to pass the client to the front desk."""

appointment_book = AppointmentBook(OPEN_TIMES)
booking_queue = BookingQueue(appointment_book)
tools = AppointmentToolbox(appointment_book, booking_queue)
model = OllamaModel("granite4.1:3b")
helper = AppointmentHelper("Steve", INSTRUCTIONS, tools, model)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{helper.name}: {helper.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(helper.history)}")

print("Front desk review")
for request in booking_queue.waiting():
    number = request["number"]
    print(f"Request {number}: {request['client']}, {request['day']} {request['time']}")
    answer = input("Approve? yes or no: ")
    if answer == "yes":
        print(booking_queue.approve(number))
    else:
        print(booking_queue.reject(number))

print(f"Bookings: {len(appointment_book.bookings)}")
