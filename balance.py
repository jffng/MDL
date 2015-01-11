#!/usr/bin/python

#function to remove all non-bracket characters
import sys

def isolate_brackets(program):
    all_brackets = set('({[]})')
    brackets = ''
    for b in program:
        if b in all_brackets:
            brackets+=b
    return brackets

def is_balanced(expression):    
    # if the number of brackets is not even, 
    # then there's no possibility of the expression being balanced.
    if len(expression) % 2 != 0:
        return False
    
    # create a set of possible open brackets
    open_brackets = set('({[')
    
    # create a set of pairs of match brackets
    matching_brackets = set([ ('(',')'), ('{','}'), ('[',']') ])
    
    # create a list to push brackets onto
    stack = []
    
    # iterate over every bracket in the the expression
    for c in expression:
        # if it's an opening bracket, push it to the stack
        if c in open_brackets:
            stack.append(c)
    
        else:
        	# check if stack contains an opening bracket, i.e. length of stack > 0
            if len(stack) == 0:
                return False
            
            # store the last opening bracket
            last_open = stack.pop()
            
            # check if the current bracket does not match the last opening bracket
            if (last_open, c) not in matching_brackets:
                return False
    
    # validate that logic is correct by ensuring every bracket has been removed from the stack
    # i.e. length of stack should be zero   
    return len(stack) == 0

expr = isolate_brackets(sys.argv[1])

if(expr):
	print is_balanced(expr)
else:
	print "No brackets in the expression."

