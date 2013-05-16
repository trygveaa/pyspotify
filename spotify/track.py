from __future__ import unicode_literals

from spotify import ffi, lib


__all__ = [
    'Track',
]


class Track(object):
    def __init__(self, sp_track):
        lib.sp_track_add_ref(sp_track)
        self.sp_track = ffi.gc(sp_track, lib.sp_track_release)

    def as_link(self, offset=0):
        from spotify.link import Link
        return Link(self, offset=offset)

    # TODO Add sp_track_* methods
