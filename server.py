#!/usr/bin/python
import asyncore
import smtpd

port = 2500
smtpd.DebuggingServer(
    ("0.0.0.0", port),
    ("localhost", port)
)
asyncore.loop()

