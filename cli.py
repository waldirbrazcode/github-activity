import argparse
from user_activity import get_user_events

parser = argparse.ArgumentParser(prog='Github User Activity', description='Print the events of a user on the last 30 days')

parser.add_argument('username', type=str, help='Username of the user')

args = parser.parse_args()

get_user_events(args.username)