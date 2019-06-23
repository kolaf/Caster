'''
Handles standard imports for creating grammars. Import using:
from castervoice.lib.imports import *
'''

from dragonfly import Repeat, Function, Dictation, Choice, MappingRule, ContextAction, ShortIntegerRef, Mimic, Playback, Pause, Window, Compound, Repetition, Paste

from castervoice.lib import context, navigation, alphanumeric, textformat, text_utils, settings
from castervoice.lib import control, utilities, text_manipulation_functions

from castervoice.lib.actions import Key, Text, Mouse
from castervoice.lib.clipboard import Clipboard
from castervoice.lib.context import AppContext
from castervoice.lib.dfplus.additions import IntegerRefST, SelectiveAction

from castervoice.lib.dfplus.merge.ccrmerger import CCRMerger
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.merge.selfmodrule import SelfModifyingRule

from castervoice.lib.dfplus.state.actions import AsynchronousAction, ContextSeeker
from castervoice.lib.dfplus.state.actions2 import UntilCancelled
from castervoice.lib.dfplus.state.short import L, S, R

from castervoice.lib.ccr.standard import SymbolSpecs
from castervoice.lib.ccr.core.punctuation import double_text_punc_dict, text_punc_dict

import os, sys, re, copy
