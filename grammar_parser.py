 #!/usr/bin/env python3

import re

from pyleri import (
    Grammar,
    Keyword,
    Token,
    Regex,
    List, 
    Sequence)
from pyleri.repeat import Repeat

class MyGrammar(Grammar):
    RE_KEYWORDS = re.compile('^[A-Za-z-=>]+')
    r_output = Regex('[a-zA-Z 0-9\']+')
    r_input = Regex('[a-zA-Z 0-9\']+')
    k_lead2 = Token('=>')
    START = Repeat(Sequence(r_input, k_lead2, r_output))

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

        