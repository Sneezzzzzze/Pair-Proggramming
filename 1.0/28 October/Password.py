""" Password"""
import hashlib
def main():
    """beom"""
    password = hashlib.sha512()
    password.update(input().encode("utf-8"))
    print(password.hexdigest().upper())
main()
