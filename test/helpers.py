# -*- coding: utf-8 -*-
"""
helpers
~~~~~~~

This module contains helpers for the h2 tests.
"""
from hyperframe.frame import (
    HeadersFrame, DataFrame, SettingsFrame, WindowUpdateFrame, PingFrame,
    GoAwayFrame, RstStreamFrame, PushPromiseFrame
)
from hpack.hpack import Encoder


SAMPLE_SETTINGS = {
    SettingsFrame.HEADER_TABLE_SIZE: 4096,
    SettingsFrame.ENABLE_PUSH: 1,
    SettingsFrame.MAX_CONCURRENT_STREAMS: 2,
}


class FrameFactory(object):
    """
    A class containing lots of helper methods and state to build frames. This
    allows test cases to easily build correct HTTP/2 frames to feed to
    hyper-h2.
    """
    def __init__(self):
        self.encoder = Encoder()

    def refresh_encoder(self):
        self.encoder = Encoder()

    def preamble(self):
        return b'PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n'

    def build_headers_frame(self, headers, flags=None, stream_id=1):
        """
        Builds a single valid headers frame out of the contained headers.
        """
        f = HeadersFrame(stream_id)
        f.data = self.encoder.encode(headers)
        f.flags.add('END_HEADERS')
        if flags:
            f.flags.update(flags)
        return f

    def build_data_frame(self, data, flags=None, stream_id=1):
        """
        Builds a single data frame out of a chunk of data.
        """
        flags = set(flags) if flags is not None else set()
        f = DataFrame(stream_id)
        f.data = data
        f.flags = flags
        return f

    def build_settings_frame(self, settings, ack=False):
        """
        Builds a single settings frame.
        """
        f = SettingsFrame(0)
        if ack:
            f.flags.add('ACK')

        f.settings = settings
        return f

    def build_window_update_frame(self, stream_id, increment):
        """
        Builds a single WindowUpdate frame.
        """
        f = WindowUpdateFrame(stream_id)
        f.window_increment = increment
        return f

    def build_ping_frame(self, ping_data, flags=None):
        """
        Builds a single Ping frame.
        """
        f = PingFrame(0)
        f.opaque_data = ping_data
        if flags:
            f.flags = set(flags)

        return f

    def build_goaway_frame(self, last_stream_id, error_code=0):
        """
        Builds a single GOAWAY frame.
        """
        f = GoAwayFrame(0)
        f.error_code = error_code
        f.last_stream_id = last_stream_id
        return f

    def build_rst_stream_frame(self, stream_id, error_code=0):
        """
        Builds a single RST_STREAM frame.
        """
        f = RstStreamFrame(stream_id)
        f.error_code = error_code
        return f

    def build_push_promise_frame(self,
                                 stream_id,
                                 promised_stream_id,
                                 headers,
                                 flags=[]):
        """
        Builds a single PUSH_PROMISE frame.
        """
        f = PushPromiseFrame(stream_id)
        f.promised_stream_id = promised_stream_id
        f.data = self.encoder.encode(headers)
        f.flags = set(flags)
        return f
