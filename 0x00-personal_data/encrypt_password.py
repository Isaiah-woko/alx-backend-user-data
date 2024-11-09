#!/usr/bin/env python3
"""This is a module for encrypting passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """This hashes a password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks is a hashed password was formed from the given password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
