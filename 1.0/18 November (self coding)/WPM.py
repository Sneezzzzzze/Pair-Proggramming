"""WPM"""
def main():
    """BEOM"""
    inp = input()
    num = int(input())
    dicct = {"Kids": {(num < 11): "Very Slow",
                      (11 <= num <= 20): "Slow",
                      (21 <= num <= 31): "Average",
                      (31 <= num <= 40): "Fast",
                      (num > 40): "Very Fast"},
             "Adults": {(num < 26): "Very Slow",
                        (26 <= num <= 35): "Slow/Beginner",
                        (36 <= num <= 45): "Intermediate/Average",
                        (46 <= num <= 65): "Fast/Advanced",
                        (66 <= num <= 80): "Very Fast",
                        (num > 80): "Insane"
                        }
             }
    print(dicct[inp][True])
main()
