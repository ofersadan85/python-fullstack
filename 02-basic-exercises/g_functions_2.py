# 1. Write a function that accepts a list of numbers and any number of additional numbers as arguments to be added to the list.
# my_list = [1, 2, 3]
# add_to_list(my_list, 4, 5, 6)  -> [1, 2, 3, 4, 5, 6]

# 2. Create a `multiply` function that multiplies any number of arguments passed to it.
# multiply(1, 2, 3, 4)  -> 24
# multiply()  -> 1

# 3. Develop a `save_user` function that accepts a mandatory `user_id` and any additional information about the user in the form of keyword arguments.
# save_user(1, name="John", age=22, city="London")  -> (save all user data as json)
# save_user(2, name="Jane", age=21, city="Paris", country="France")  -> (save all user data as json)

# 4. Write a function `concatenate_strings` that concatenates an arbitrary number of strings passed to it with a given separator.
# concatenate_strings("Hello", "World", "!", sep=" ")  -> "Hello World !"
# concatenate_strings("Hello", "World", "!", sep="*")  -> "Hello*World*!"

# 5. Write a `min_max` function that accepts any number of positional arguments and returns the minimum and maximum values.
# min_max(1, 2, 3, 4, 5)  -> (1, 5)
# min_max(5, 9, 1, 0)  -> (0, 9)
# min_max(1)  -> (1, 1)
# min_max()  -> # ValueError: min_max() expected at least 1 argument, got 0

# 6. Develop a `schedule_event` function that takes an event name, date, and any other optional keyword details like the location, time, and notes.
# schedule_event("Wedding") -> Wedding scheduled for tomorrow at 12:00
# schedule_event("Meeting", date="2021-01-01", time="12:00", location="London", notes="Bring a gift!") -> Wedding scheduled for 2021-01-01 at 12:00 in London

# 7. Create a `send_email` function that requires a recipient and a message body but also takes an optional subject line and any number of additional headers as keyword arguments.
# send_email("john@example", "Hello!")  -> Email sent to john@example with subject: None
# send_email("jane@example", "Hello!", subject="Hello", cc="john@example")  -> Email sent to jane@example and john@example with subject: Hello
