from __future__ import print_function
import httplib,urllib
from passlib.hash import pbkdf2_sha256
from passlib.hash import pbkdf2_sha512
from passlib.hash import pbkdf2_sha1
import json


def lambda_handler(event, context):
    details = event['body']
    digest = details['digest']
    hash_pass = details['hash_pass']
    password = details['password']

    if digest == "sha256":
        verification = pbkdf2_sha256.verify(password, hash_pass)
    elif digest == "sha512":
        verification = pbkdf2_sha512.verify(password, hash_pass)
    else:
        verification = pbkdf2_sha1.verify(password, hash_pass)
    return verification
