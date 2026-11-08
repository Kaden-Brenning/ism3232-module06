# Week 11 answers

## Exercise 1
1. The message the customer never saw: 
The system message that holds the instructions.
2. How many times the customer has spoken: 
2 times
3. Can the model tell that the last reply came from the order tool? Why does that matter? 
No. In the history every reply has the role assistant, whether a rule, a tool, or the model wrote it. The model reads the whole history, so it can copy the pattern of an earlier tool answer and state something the tool never said.
4. The customer now types "thanks". How many messages are sent on the next call? 
Six

## Exercise 3
You: how long does shipping take?
Sunny: Shipping takes 3 to 5 business days.
You: can i return a late item?
Sunny: No, sale items cannot be returned.
You: do you offer gift wrapping
Sunny: I do not know and can offer to pass the customer to a human agent.
You: do you have a store in orlando?
Sunny: I do not know and can offer to pass the customer to a human agent.
You: quit
Messages in this conversation: 8

## Exercise 4
Sunny: The store now closes at 11 pm.