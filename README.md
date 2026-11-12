# ISM3232 - Module 6: OOP for agents chatbot and tool

## Contents
This module contains an assistant that responds to user input. This is a mock chatbot, since it cannot handle user input that is outside of the keywords that are included. An input will go to a human when the input message contains address, payment, or card. These are not handled by the assistant, since it cannot do data entry. If real customer data is used, the assistant might need to use different responses for the data.
## One Good
One positive is that the assistant is able to recognize a request as not answerable. This avoids the assistant from providing incorrect information to the user.
## One Bad
One major flaw with the assistant is the human handoff only checks for keywords. This means that asking about gift cards would stop the model since it includes the word card.
## What Stays
The human handoff will stay in the code, as the assistant still cannot handle certain requests. 