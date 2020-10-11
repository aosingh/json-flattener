import logging

from collections import deque, namedtuple
from typing import Dict

LOG = logging.getLogger(__name__)

__all__ = ['JSONFlattener']

'''
JSON objects are deserialized as Python dict. To flatten the dict, we traverse it in DFS manner.
As we traverse, we use a stack to store all nodes (in the path) unless we hit a terminal value.

'''

Node = namedtuple('Node', ('val', 'path'))


class JSONFlattener:
    """A callable to flatten a nested Python dict.

    """
    def __init__(self, data: Dict, skip_unknown=True):
        self.flattened_dict = {}
        self._stack = deque([Node(val=data, path=())])
        self.skip_unknown = skip_unknown

    def _flatten(self):
        """Perform DFS traversal on the input Python dict.

        Terminal values are stored in the output dict with path as keys.
        A value is considered to be terminal only if it is one of the following
        primitive types or if it is None.
            - str
            - int
            - bool
            - float

        """
        while self._stack:
            node = self._stack.pop()

            if node.val is None or isinstance(node.val, (str, int, bool, float)):
                self.flattened_dict[".".join(node.path)] = node.val

            elif isinstance(node.val, Dict):
                for k, v in node.val.items():
                    self._stack.append(Node(val=v, path=node.path+(k,)))
            else:
                if self.skip_unknown:
                    LOG.warning("Skipping %s", node)
                else:
                    raise TypeError(f"Unknown type {type(node.val)}")

    def __call__(self, *args, **kwargs) -> Dict:
        """ Returns the flattened python dict after invoking the procedure.
        """
        self._flatten()
        return self.flattened_dict
