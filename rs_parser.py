 #!/usr/bin/env python3

import re
from pyparsing import *
import pyparsing as pp

from pyleri import (
    Grammar,
    Keyword,
    Token,
    Regex,
    List, 
    Sequence)
from pyleri.repeat import Repeat

class RobinScriptGrammar(Grammar):
    RE_KEYWORDS = re.compile('^[A-Za-z =>]+')
    r_output = Regex('[a-zA-Z 0-9\']+')
    r_input = Regex('[a-zA-Z 0-9\']+')
    k_lead2 = Token('>>')
    START = Repeat(Sequence(r_input, k_lead2, r_output))

    statement = Forward()
    #suite = indentedBlock(statement)

    text = alphanums + ".,!? "
    input = Word(text)('input')
    output = Word(text)('output')
    input2output = (input + Suppress("=>") + output) ("in2out")
    comment = ("#" + Word(text))("comment")
    statement << Group(input2output | comment)('statement')
    statement.setResultsName("statement")
    module_body = OneOrMore(statement)


def node_props(node, children):
    return {
        'start': node.start,
        'end': node.end,
        'name': node.element.name if hasattr(node.element, 'name') else None,
        'element': node.element.__class__.__name__,
        'string': node.string,
        'children': children}

def get_children(children):
    return [node_props(c, get_children(c.children)) for c in children]

def get_ast(node):
    if (type(node.element) is Sequence) and (len(node.children) == 3):
        return {
            'type': 'answer',
            'input': node.children[0].string,
            'output': node.children[2].string
        }
    else:
        return None

def getRules(pyparserResults):
    rules = []
    for item in pyparserResults:
            #print("Is {} a in2out? {}".format(item, 'in2out' in item))
            if 'in2out' in item:
                #print("Content is: {}".format(item['in2out']))
                #print("Input: {}, output: {}".format(item['in2out'][0], item['in2out'][1]))
                input = item['in2out'][0]
                output = item['in2out'][1]
                rules.append({
                    'type': 'answer',
                    'input': input.rstrip(' '),
                    'output': output
                })
    return rules

        