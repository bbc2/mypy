# Stubs for email.contentmanager (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class ContentManager:
    get_handlers = ...  # type: Any
    set_handlers = ...  # type: Any
    def __init__(self): ...
    def add_get_handler(self, key, handler): ...
    def get_content(self, msg, *args, **kw): ...
    def add_set_handler(self, typekey, handler): ...
    def set_content(self, msg, obj, *args, **kw): ...

raw_data_manager = ...  # type: Any

def get_text_content(msg, errors=''): ...
def get_non_text_content(msg): ...
def get_message_content(msg): ...
def get_and_fixup_unknown_message_content(msg): ...
def set_text_content(msg, string, subtype='', charset='', cte=None, disposition=None,
                     filename=None, cid=None, params=None, headers=None): ...
def set_message_content(msg, message, subtype='', cte=None, disposition=None, filename=None,
                        cid=None, params=None, headers=None): ...
def set_bytes_content(msg, data, maintype, subtype, cte='', disposition=None, filename=None,
                      cid=None, params=None, headers=None): ...