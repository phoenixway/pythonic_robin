 #!/usr/bin/env python3
from string import whitespace
from pyparsing import *
import pyparsing as pp

test = """\
here
are
some
strings
and
some
others
 with
 different
 levels
 of
  indentation
    sir
"""

# newlines are significant for line separators, so redefine 
# the default whitespace characters for whitespace skipping
ParserElement.setDefaultWhitespaceChars(' ')

NL = LineEnd().suppress()
HASH_SEP = Suppress(Optional(NL))

# a normal line contains a single word
word_line = Word(alphas) + NL


indent_stack = [1]

# word_block is recursive, since word_blocks can contain word_blocks
word_block = Forward()
word_group = Group(OneOrMore(word_line | (indentedBlock(word_block, indent_stack))) )

# now define a word_block, as a '#'-delimited list of word_groups, with 
# leading and trailing '#' characters
word_block <<= (delimitedList(word_group))

# the overall expression is one large word_block
parser = word_block

# parse the test string
parser.parseString(test).pprint()
