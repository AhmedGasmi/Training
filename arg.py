import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

subgroup = parser.add_argument_group('Subgroup')
subgroup.add_argument('--arg2a')
subgroup.add_argument('--arg2b')

group.add_argument('--arg1')
group.add_argument_group(subgroup)

args = parser.parse_args()

if args.arg1:
    print(f"arg1 is: {args.arg1}")
elif args.arg2a and args.arg2b:
    print(f"arg2a is: {args.arg2a}")
    print(f"arg2b is: {args.arg2b}")
else:
    print("Error: either arg1 or arg2a and arg2b must be provided")
