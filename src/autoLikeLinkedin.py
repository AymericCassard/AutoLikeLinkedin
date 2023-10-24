import argparse

parser = argparse.ArgumentParser(
    description="simple program that likes or dislikes Linkedin post from"
    + " selected company"
)
parser.add_argument("company_name", help="name of the company to be liked")
group = parser.add_mutually_exclusive_group()
group.add_argument("-l", help="like one post", action="store_true")
group.add_argument("-L", help="like all posts", action="store_true")
group.add_argument("-d", help="dislike one post", action="store_true")
group.add_argument("-D", help="dislike all posts", action="store_true")
args = parser.parse_args()

print(args.company_name)

if args.l:
    print(args.l)
if args.L:
    print(args.L)
if args.d:
    print(args.d)
if args.D:
    print(args.D)
