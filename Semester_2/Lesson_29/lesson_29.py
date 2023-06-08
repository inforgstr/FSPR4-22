# import re


# titles = [
# "Middle Javascript developer",
# "Middle Javascript developer",
# "Middle Javascript developer",
# ]
#
# title = "middle javascript developer"
#
# js = {
# "javascript": [
# "javascript",
# "reaxt",
# "angular",
# "angularjs",
# "react",
# "node js",
# "node.js",
# "nodejs",
# ]
# }
#
# mapper_string = "|".join([reg_ex for reg_ex in js["javascript"]])
# result = re.finditer(mapper_string, title, re.IGNORECASE)
# print(next(result))
# print(next(result))

# Decorator for empty values in function argument

def plus(n):
    try:
        if int(n) > 0 and n:
            return int(n) + 5
        return "Wrong argument were given!"
    except (TypeError, ValueError) as error:
        return error

if __name__ == "__main__":
    print(plus())
