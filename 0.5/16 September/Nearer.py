"""Nearer"""
def man():
    """beom hong"""
    alice = int(input())
    bob = int(input())
    ice = int(input())
    if abs(ice -bob) < abs(ice-alice):
        print("Bob", abs(ice-bob))
    elif abs(ice -bob) > abs(ice-alice):
        print("Alice", abs(ice-alice))
    elif abs(ice -bob) == abs(ice-alice):
        print("Sundaes", abs(ice-bob))
man()
