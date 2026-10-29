from my_assistant import AppointmentHelper
from my_tool import AppointmentBook


def make_helper():
    """Build a fresh helper with its own tool for each test."""
    book = AppointmentBook(
        {"monday": "9:00 am and 2:30 pm", "friday": "11:00 am and 1:30 pm"}
    )
    return AppointmentHelper("Pete", "Be clear.", book)


def test_open_times_question_uses_the_tool():
    helper = make_helper()
    reply = helper.respond("What times are open on Monday?")
    assert reply == "Open times on monday: 9:00 am and 2:30 pm."


def test_question_without_a_known_day_asks_for_one():
    helper = make_helper()
    assert "Which day?" in helper.respond("What times are open on Sunday?")


def test_booking_request_goes_to_a_human():
    helper = make_helper()
    assert "front desk" in helper.respond("Please book me for Monday at 9")


def test_unknown_request_gets_a_safe_reply():
    helper = make_helper()
    assert "not sure" in helper.respond("What is your favorite color?")


def test_history_grows_by_two_each_turn():
    helper = make_helper()
    helper.respond("hello")
    helper.respond("What is open on Friday?")
    assert len(helper.history) == 4
