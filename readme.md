# objmodv2
A python module for live-tweaking objects in bf2 engine through host.rcon_invoke.  
Patched for PR:BF2 post 1.4 versions, may not work on bf2.

Installing:  
1. Clone repo to ``<mod_root>/python/game``  
2. Add ``import objmodv2`` to ``<mod_root>/python/game/__init__.py``  
3. Launch server  

Notes:  
Sockets telemetry enabled by default and will cause huge udp flood on ``localhost:8888``.  
Can be disabled in ``config.py``, set ``C['SOCKET']`` to ``False``.