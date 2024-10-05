from typing import Callable, Dict


# Registry to hold event handlers
event_handlers: Dict[str, Callable] = {}

def on_init(func: Callable):
    event_handlers['on_init'] = func
    return func

def on_query(func: Callable):
    event_handlers['on_query'] = func
    return func

def on_close(func: Callable):
    event_handlers['on_close'] = func
    return func
