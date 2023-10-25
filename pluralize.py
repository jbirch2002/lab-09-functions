def pluralize(word):
    if word == "moose":
        return "moose"
    elif word == "automaton":
        return "automata"
    elif word == "mouse":
        return "mice"
    else:
        return word + "s"

user_input = input("Word please: ")
plural_version = pluralize(user_input)

print(plural_version)