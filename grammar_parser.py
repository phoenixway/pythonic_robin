 #!/usr/bin/env python3

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