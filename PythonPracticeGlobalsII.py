"""
Practice from Chapter 12, 13

"""

# thismod.py
y = 5 # Global variable == module attribute
z = 7 # Global variable == module attribute

def some_global():
    global x # Change local var
    x = 3
    
some_global()
print 'x, y, z = ', x, ', ', y, ', ', z
x = 11
print 'x, y, z = ', x, ', ', y, ', ', z

def f1():
    X = 88
    def f2():
        print(X) # Remembers X in enclosing def scope
    return f2 # Return f2 but don't call it
action = f1() # Make, return function
action() # Call it now: prints 88

def maker(N):
    def action(X): # Make and return action
        return X ** N # action retains N from enclosing scope
    return action

f = maker(2)
print f
print f(3)
print f(4)
