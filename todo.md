#top vulnerbilities to check first

## authorization/authentication:

Client demands/Server responds, check and see what the permissions are looking like.
Sometimes the client has toooo much control.


## encryption/encoding

This is probobly the first thing we need to look for when designing the framework, all sockets should be upgraded to wss:// if not we can sniff all incoming/outgoing traffic.


## malicious input attacks

Checking to see if all input data is sanitized properly








