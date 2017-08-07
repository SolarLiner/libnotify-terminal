import os
import pytest

def TestCompiledBin(object):
    def test_reply(self):
        args = [ "./.bin/libnotify-terminal"
            "--appname Test message",
            "--title New message",
            "--subtitle",  '"Ali Connors"',
            "--reply --reply-to", '"Ali Connors"',
            "--reply-message", '"Hey, you down for dinner?"'
        ]

        out = os.popen(" ".join(args))
        assert str(out).startswith("reply:")