from erros import invalid_token_error
from enum import Enum

dict_tokens = {
   1 : 'SUM_TOKEN',   
   2 : 'SUBTRACTION_TOKEN',   
   3 : 'TIMES_TOKEN',   
   4 : 'DIVISION_TOKEN',    
}

class Token(Enum):
    # Arithmetic Operators
    SUM_TOKEN = '+'
    SUBTRACTION_TOKEN = '-'
    TIMES_TOKEN = '*'
    DIVISION_TOKEN = '/'
    MODULE_TOKEN = 'mod'
    INTEGER_DIVISION_TOKEN = 'div'

    # Logic Operators
    OR_TOKEN = 'or'
    AND_TOKEN = 'and'
    NOT_TOKEN = 'not'

    # Comparison Operators
    EQUAL_TOKEN = '=='
    NOT_EQUAL_TOKEN = '<>'
    GREATER_TOKEN = '>'
    WEAKER_TOKEN = '<'
    
    GREATER_EQUAL_TOKEN = '>='
    WEAKER_EQUAL_TOKEN = '<='
    ATRIBUTTION_TOKEN = ':='

    # Reserved Keywords
    PROGRAM_TOKEN = 'program'
    VAR_TOKEN = 'var'
    INT_TOKEN  = 'integer'
    REAL_TOKEN = 'real'
    STR_TOKEN = 'string'
    BEGIN_TOKEN = 'begin'
    END_TOKEN = 'end'
    
    FOR_TOKEN = 'for'
    TO_TOKEN = 'to'
    BREAK_TOKEN = 'break'

    # Control Flow
    IF_TOKEN = 'if'
    ELSE_TOKEN = 'else'
    THEN_TOKEN = 'then'

    # IO Keyworkds
    WRITE_TOKEN = 'write'
    WRITELN_TOKEN = 'writeln'
    READ_TOKEN = 'read'
    READLN_TOKEN = 'readln'

    # Delimiters
    COLON_TOKEN = ','
    DOT_TOKEN = '.'
    DOUBLEDOT_TOKEN = ':'
    OPEN_PARENTHESES_TOKEN = '('
    CLOSE_PARENTHESES_TOKEN = ')'

def str_token(token):
    if isinstance(token, Token):
        return token.value
    else:
        invalid_token_error()
        return None 