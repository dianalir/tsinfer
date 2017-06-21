"""
Implementation of the Li and Stephens algorithm for inferring a tree
sequence.

Python 3 only.
"""

import sys

__version__ = "0.4.dev1"

if sys.version_info[0] < 3:
    raise Exception("Python 3 only")

# TODO remove old code and change file names.
from .inference import ReferencePanel
from .inference import Illustrator

from .new_inference import AncestorBuilder
from .new_inference import AncestorStore
from .new_inference import AncestorMatcher
from .new_inference import Traceback
from .new_inference import TreeSequenceBuilder
from .new_inference import infer
