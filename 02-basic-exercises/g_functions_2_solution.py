import json

# 1. Write a function that accepts a list of numbers and any number of additional numbers as arguments to be added to the list.
# my_list = [1, 2, 3]
# add_to_list(my_list, 4, 5, 6)  -> [1, 2, 3, 4, 5, 6]


# Solution 1 (Note: This will modify the original list)
def add_to_list(my_list, *args):
    my_list.extend(args)
    return my_list


# Solution 2 (Note: This will NOT modify the original list)
def add_to_list(my_list, *args):
    return my_list + list(args)


# 2. Create a `multiply` function that multiplies any number of arguments passed to it.
# multiply(1, 2, 3, 4)  -> 24
# multiply()  -> 1


def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


# 3. Develop a `save_user` function that accepts a mandatory `user_id` and any additional information about the user in the form of keyword arguments.
# save_user(1, name="John", age=22, city="London")  -> (save all user data as json)
# save_user(2, name="Jane", age=21, city="Paris", country="France")  -> (save all user data as json)


def save_user(user_id, **kwargs):
    user_id = str(user_id)
    kwargs["user_id"] = user_id
    try:
        with open(f"users.json", "r") as f:
            users = json.load(f)  # don't forget to import json
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        # We'll get here if the file is empty or doesn't exist
        users = {}
    users[user_id] = kwargs
    with open(f"users.json", "w") as f:
        json.dump(users, f, indent=2)  # indent=2 is optional, but makes the file more readable


# 4. Write a function `concatenate_strings` that concatenates an arbitrary number of strings passed to it with a given separator.
# concatenate_strings("Hello", "World", "!", sep=" ")  -> "Hello World !"
# concatenate_strings("Hello", "World", "!", sep="*")  -> "Hello*World*!"


# Solution 1, loop:
def concatenate_strings(*args, sep=" "):
    if not args:  # if len(args) == 0:
        return ""
    result = args[0]
    for arg in args[1:]:
        result = result + sep + arg
    return result


# Solution 2, join:
def concatenate_strings(*args, sep=" "):
    return sep.join(args)


# 5. Write a `min_max` function that accepts any number of positional arguments and returns the minimum and maximum values.
# min_max(1, 2, 3, 4, 5)  -> (1, 5)
# min_max(5, 9, 1, 0)  -> (0, 9)
# min_max(1)  -> (1, 1)
# min_max()  -> # ValueError: min_max() expected at least 1 argument, got 0


def min_max(*args):
    if not args:
        raise ValueError("min_max() expected at least 1 argument, got 0")
    return (min(args), max(args))


# 6. Develop a `schedule_event` function that takes an event name, date, and any other optional keyword details like the location, time, and notes.
# schedule_event("Wedding") -> Wedding scheduled for tomorrow at 12:00
# schedule_event("Meeting", date="2021-01-01", time="12:00", location="London", notes="Bring a gift!") -> Wedding scheduled for 2021-01-01 at 12:00 in London


def schedule_event(event_name, **kwargs):
    if "date" not in kwargs:
        kwargs["date"] = "tomorrow"
    if "time" not in kwargs:
        kwargs["time"] = "12:00"
    description = f"{event_name} scheduled for {kwargs['date']} at {kwargs['time']}"
    if "location" in kwargs:
        description = f"{description} in {kwargs['location']}"
    return description


# 7. Create a `send_email` function that requires a recipient and a message body but also takes an optional subject line and any number of additional headers as keyword arguments.
# send_email("john@example", "Hello!")  -> Email sent to john@example with subject: None
# send_email("jane@example", "Hello!", subject="Hello", cc="john@example")  -> Email sent to jane@example and john@example with subject: Hello


def send_email(recipient, body, **kwargs):
    subject = kwargs.get("subject")
    cc = kwargs.get("cc")
    if cc:
        recipient = f"{recipient} and {cc}"
    if subject:
        print(f"Email sent to {recipient} with subject: {subject}")
    else:
        print(f"Email sent to {recipient} with subject: None")
    print(body)
