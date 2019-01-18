class Node:
    def __init__(self):
        print("init node")

    def evaluate(self):
        return 0

    def execute(self):
        return 0

class Node_w(Node):
    def __init__(self, v1, v2):
        self.boolexpr = v1
        self.block = v2
    def execute(self):
        while(bool(self.boolexpr.evaluate())):
            self.block.execute()

class Node_if(Node):
    def __init__(self, v1, v2, v3):
        self.boolexpr = v1
        self.ifblock = v2
        self.elseblock = v3
    def execute(self):
        if(bool(self.boolexpr.evaluate())):
            self.ifblock.execute()
        else:
            self.elseblock.execute()

class Node_if2(Node):
    def __init__(self, v1, v2):
        self.boolexpr = v1
        self.ifblock = v2
    def execute(self):
        if(bool(self.boolexpr.evaluate())):
            self.ifblock.execute()


class VariableNode(Node):
    def __init__(self, v,v2):
        self.variable = v
        self.value = v2
    def evaluate(self):
        return [names[self.variable][names[self.value]]]

class VariableNode3(Node):
    def __init__(self, name):
        self.name =name
    def evaluate(self):
        return names[self.name]

class AssignNode2(Node):
    def __init__(self, v,v2,v3):
        self.variable = v
        self.value = v2
        self.value3 = v3
    def execute(self):
        names[self.variable][self.value.evaluate()] = self.value3.evaluate()


class AssignNode(Node):
    def __init__(self, v,v2):
        self.variable = v
        self.value = v2
    def execute(self):
        names[self.variable] = self.value.evaluate()

class listNode(Node):
    def __init__(self, v):
        self.value = list(v)
    def evaluate(self):
        return self.value

class IndexNode2(Node):
    def __init__(self, v1,v2):
        self.element = v1
        self.index_value = v2
    def evaluate(self):
        self.element=names[self.element]
        self.value = self.element[self.index_value.evaluate()]
        return self.value

class IndexNode(Node):
    def __init__(self, v1,v2):
        self.element = v1
        self.index_value = v2
    def evaluate(self):
        return self.element.evaluate()[self.index_value.evaluate()]

class StringNode(Node):
    def __init__(self, v):
        self.value = str(v)
    def evaluate(self):
        return self.value


class BoolNode(Node):
    def __init__(self, v):
        self.value = bool(v)
    def evaluate(self):
        return self.value

class NumberNode(Node):
    def __init__(self, v):
        if('.' in v):
            self.value = float(v)
        else:
            self.value = int(v)

    def evaluate(self):
        return self.value

class BipNode(Node):
    def __init__(self, op, v1):
        self.v1 = v1
        self.op = op
    def evaluate(self):
        if (self.op == '-'):
            return (-(self.v1.evaluate()))



class Boolop2Node(Node):
    def __init__(self, op, v1):
        self.v1 = v1
        self.op = op
    def evaluate(self):
        if (self.op == 'not'):
            return bool(not(self.v1.evaluate()))


class BoolopNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op
    def evaluate(self):
        if (self.op == '<'):
            return bool(self.v1.evaluate() < self.v2.evaluate())
        elif (self.op == '<='):
            return bool(self.v1.evaluate() <= self.v2.evaluate())
        elif (self.op == '>'):
            return bool(self.v1.evaluate() > self.v2.evaluate())
        elif (self.op == '>='):
            return bool(self.v1.evaluate() >= self.v2.evaluate())
        elif (self.op == '=='):
            return bool(self.v1.evaluate() == self.v2.evaluate())
        elif (self.op == 'and'):
            return bool(bool(self.v1.evaluate()) and bool(self.v2.evaluate()))
        elif (self.op == 'or'):
            return bool(bool(self.v1.evaluate()) or bool(self.v2.evaluate()))
        elif (self.op == 'in'):
            return bool((self.v1.evaluate()) in (self.v2.evaluate()))
        elif (self.op == '<>'):
            return bool((self.v1.evaluate()) != (self.v2.evaluate()))


class BopNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op
    def evaluate(self):
        if (self.op == '+'):
            #print("+ expression", self.v1.evaluate(), self.v2.evaluate())
            return self.v1.evaluate() + self.v2.evaluate()
        elif (self.op == '-'):
            return self.v1.evaluate() - self.v2.evaluate()
        elif (self.op == '*'):
            return self.v1.evaluate() * self.v2.evaluate()
        elif (self.op == '/'):
            return self.v1.evaluate() / self.v2.evaluate()
        elif (self.op == '//'):
            return self.v1.evaluate() // self.v2.evaluate()
        elif (self.op == '%'):
            return self.v1.evaluate() % self.v2.evaluate()
        elif (self.op == '**'):
            return self.v1.evaluate() ** self.v2.evaluate()

class PrintNode(Node):
    def __init__(self, v):
        self.value = v
    def execute(self):
        print(self.value.evaluate())

class BlockNode(Node):
    def __init__(self, s=None):
        #print("block init",s)
        if s is None :
            self.sl = []
        else:
            self.sl = [s]

    def execute(self):
        for statement in self.sl:
            statement.execute()

tokens = [
        'LBRACE', 'RBRACE', 'PRINT', 'SEMI','WHILE','IF','ELSE',
 'NUMBER','STRING','MODULUS','POWER','LBRAC','RBRAC','NOT_EQUAL','COMMA','FALSE','TRUE',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS','FLOOR', 'AND','OR','NOT','IN',
    'LPAREN', 'RPAREN','LESS','LESS_EQUAL','EQUATES','GREAT','GREAT_EQUAL','NAME'
]
# Tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_POWER = r'\*\*'
t_DIVIDE = r'/'
t_FLOOR = r'//'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRAC = r'\['
t_RBRAC = r'\]'
t_MODULUS = r'%'
t_EQUATES = r'=='
t_LESS = r'<'
t_NOT_EQUAL = r'<>'
t_LESS_EQUAL = r'<='
t_GREAT = r'>'
t_COMMA = r','
t_GREAT_EQUAL = r'>='
t_AND = r'and '
t_OR = r'or '
t_NOT = r' not '
t_IN = r' in '
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_PRINT    = 'print'
t_SEMI  = r';'
t_WHILE = 'while'
t_IF = 'if'
t_ELSE = 'else'
t_NAME = r'((?!(and\b|or\b|\bnot\b|\bin\b|\bTrue\b|\bprint\b|\bwhile\b|\bif\b|\belse\b|\belif\b|\bFalse\b))[a-zA-Z_][a-zA-Z0-9_]*)'



def t_TRUE(t):
    r'True'
    try:
        t.value = BoolNode(t.value)
    except ValueError:
        print("String value too large %s", t.value)
        t.value = 0
    return t

def t_FALSE(t):
    r'False'
    try:
        t.value = BoolNode(0)
    except ValueError:
        print("String value too large %s", t.value)
        t.value = 0
    return t


def t_NUMBER(t):
    r'-?\d*(\d\.|\.\d)\d* | \d+'
    try:
        t.value = NumberNode(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_STRING(t):
    r'"([a-zA-Z0-9_=+`~!@#$%^&*()_\-}{,<>.?/ ]*)" | \'([a-zA-Z0-9_=+`~!@#$%^&*()_\-}{,<>.?/ ]*)\''
    try:
        t1 = t.value[1:]
        t1 = t1[:-1]
        t.value = t1
        t.value = StringNode(t.value)
    except ValueError:
        print("String value too large %s", t.value)
        t.value = 0
    return t

t_ignore = " \t"

def t_error(t):
    print("Syntax error at '%s'" % t.value)

# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules
precedence = (
    ('left','OR'),
    ('left', 'AND'),
    ('left','NOT'),
    ('left', 'IN','LESS','LESS_EQUAL','GREAT','GREAT_EQUAL','EQUATES','NOT_EQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MODULUS','TIMES', 'DIVIDE','FLOOR'),
    ('right', 'UMINUS'),
    ('right','POWER'),
    ('left','LBRAC','RBRAC'),
    ('left', 'LPAREN','RPAREN'),
)

def p_block(t):
    """
    block : LBRACE inblock RBRACE
    """
    t[0] = t[2]

def p_inblock(t):
    """
    inblock : smt inblock
    """
    t[0] = t[2]
    t[0].sl.insert(0,t[1])

def p_inblock2(t):
    """
    inblock : smt
    """
    t[0] = BlockNode(t[1])

def p_inblock3(t):
    """
    smt : block
    """
    t[0] = BlockNode(t[1])

#inblock
def p_empytyblock(t):
    """
    block : LBRACE RBRACE
    """
    #print("emptyblock")
    t[0] = BlockNode()
    #print("empty after block")



def p_whileblock(t):
    """
    smt : WHILE LPAREN expression RPAREN block
    """
    t[0] = Node_w(t[3],t[5])


def p_ifblock(t):
    """
    smt : IF  LPAREN expression RPAREN block ELSE block
    """
    #print(type(t[3]))
    #print(type(t[5]))
    t[0] = Node_if(t[3],t[5],t[7])

def p_ifblock2(t):
    """
    smt : IF  LPAREN expression RPAREN block
    """
    #print(type(t[3]))
    #print(type(t[5]))
    t[0] = Node_if2(t[3],t[5])

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_smt(t):
    """
    smt : print_smt
    """
    t[0] = t[1]

def p_print_smt(t):
    """
    print_smt : PRINT LPAREN expression RPAREN SEMI
    """
    t[0] = PrintNode(t[3])

def p_expr_list_name(t):
    '''expression : LBRAC NAME LBRAC NAME RBRAC RBRAC'''
    t[0]=VariableNode(t[2],t[4])

names = {}

def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = BipNode(t[1],t[2])

def p_statement_assign(t):
    'smt : NAME EQUALS expression SEMI'
    t[0]=AssignNode(t[1],t[3])

def p_statement_assign2(t):
    'smt : NAME LBRAC expression RBRAC EQUALS expression SEMI'
    t[0]=AssignNode2(t[1],t[3],t[6])

def p_expression_name(t):
    'expression : NAME'
    t[0] = VariableNode3(t[1])

def p_listindex(t):
    '''expression : expression LBRAC expression RBRAC
                    '''
    t[0]=IndexNode(t[1],t[3])

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MODULUS expression
                  | expression FLOOR expression
                  | expression POWER expression
                  '''
    t[0] = BopNode(t[2], t[1], t[3])


def p_expression_boolop(t):
    '''expression : expression LESS expression
                  | expression LESS_EQUAL expression
                  | expression GREAT expression
                  | expression GREAT_EQUAL expression
                  | expression EQUATES expression
                  | expression AND expression
                  | expression OR expression
                  | expression IN expression
                  | expression NOT_EQUAL expression
                  '''
    t[0] = BoolopNode(t[2], t[1], t[3])

def p_expression_boolop2(t):
    '''expression : NOT expression'''
    t[0]= Boolop2Node(t[1], t[2])

def p_expression_factor(t):
    '''expression : factor
                  '''
    t[0] = t[1]
    #evaluate and execute are not working here

def p_factor_number(t):
    '''factor : NUMBER
            | STRING
            | list
            | TRUE
            | FALSE
            '''
    t[0] = t[1]

def p_list(t):
    '''
    list : LBRAC listexpression RBRAC
         | LBRAC RBRAC
    '''
    if t[2] == ']':
        t[0]=[]
    elif ('dict' in str(type(t[2]))):
        t[0] = t[2]['value']
    else:
        t[0] = [t[2]]
    t[0]=listNode(t[0])

def p_listexpression(t):
    '''
    listexpression : expression listexpressionend
                   | expression
    '''
    t[0] = {}
    firstele = t[1].evaluate()
    if (len(t) == 3):
        l = t[2]['value'][:]
        l.insert(0, firstele)
        t[0]['value'] = l
    else:
        l=[]
        l.insert(0,firstele)
        t[0]['value'] = l

def p_listexpressionend(t):
    '''
    listexpressionend : COMMA expression
                    | COMMA expression listexpressionend
    '''
    t[0] = {}
    firstele = t[2].evaluate()
    if(len(t) == 3):
        t[0]['value'] = [firstele]
    else:
        l = t[3]['value'][:]
        l.insert(0, firstele)
        t[0]['value'] = l

def p_error(t):
    print("Syntax error at '%s'" % t.value)
import ply.yacc as yacc
yacc.yacc()
import sys
if (len(sys.argv) != 2):
    sys.exit("invalid arguments")
fd = open(sys.argv[1], 'r')
code = ""
for line in fd:
    code += line.strip()

try:
    lex.input(code)
    while True:
        token = lex.token()
        if not token: break
        #print(token)
    ast = yacc.parse(code)
    try:
        ast.execute()
    except Exception:
        print("Semantic error")
except Exception:
    print("Syntax error")


