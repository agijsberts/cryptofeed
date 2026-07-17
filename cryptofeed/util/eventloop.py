'''
Copyright (C) 2017-2025 Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
import asyncio


def get_or_create_event_loop() -> asyncio.AbstractEventLoop:
    """
    Return the event loop set for the current thread, creating and
    registering a new one if none exists. Unlike asyncio.get_event_loop(),
    this works on Python 3.12+ and with uvloop >= 0.21, where a loop is
    no longer created implicitly from synchronous code.
    """
    try:
        loop = asyncio.get_event_loop()
        if not loop.is_closed():
            return loop
    except RuntimeError:
        pass
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop
