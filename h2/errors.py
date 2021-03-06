# -*- coding: utf-8 -*-
"""
h2/errors
~~~~~~~~~~~~~~~~~~~

Global error code registry containing the established HTTP/2 error codes.

The current registry is available at:
https://tools.ietf.org/html/rfc7540#section-11.4
"""
NO_ERROR = 0x0
PROTOCOL_ERROR = 0x1
INTERNAL_ERROR = 0x2
FLOW_CONTROL_ERROR = 0x3
SETTINGS_TIMEOUT = 0x4
STREAM_CLOSED = 0x5
FRAME_SIZE_ERROR = 0x6
REFUSED_STREAM = 0x7
CANCEL = 0x8
COMPRESSION_ERROR = 0x9
CONNECT_ERROR = 0xa
ENHANCE_YOUR_CALM = 0xb
INADEQUATE_SECURITY = 0xc
HTTP_1_1_REQUIRED = 0xd

H2_ERRORS = [NO_ERROR, PROTOCOL_ERROR, INTERNAL_ERROR, FLOW_CONTROL_ERROR,
             SETTINGS_TIMEOUT, STREAM_CLOSED, FRAME_SIZE_ERROR, REFUSED_STREAM,
             CANCEL, COMPRESSION_ERROR, CONNECT_ERROR, ENHANCE_YOUR_CALM,
             INADEQUATE_SECURITY, HTTP_1_1_REQUIRED]
