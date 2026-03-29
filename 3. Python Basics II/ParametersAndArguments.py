# Parameters and Arguments

# Parameters // Positional Parameters
def say_hello(name, emoji):
    print(f'helllooooo {name} {emoji}')


# Arguments // Positional Arguments
say_hello('Nitesh', ':)')
say_hello('Emily', ':p')
say_hello('Dah', ':\'(')
print()
helllooooo Nitesh :)
helllooooo Emily :p
helllooooo Dah :'(

# Default Parameters
def say_hello(name='Darth Vader', emoji='>:('):
    print(f'helllooooo {name} {emoji}')


# Keyword Arguments
say_hello(emoji=':)', name='Bibi')
say_hello()
say_hello('Timmy')
helllooooo Bibi :)
helllooooo Darth Vader >:(
helllooooo Timmy >:(
