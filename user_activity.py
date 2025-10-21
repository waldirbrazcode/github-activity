import requests

base_url = 'https://api.github.com'

def get_user_events(username: str):
    url = f"{base_url}/users/{username}/events"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for event in data:
            message_event = ''

            event_type = event.get("type")
            repo = event.get('repo')
            payload = event.get('payload')
            date = event.get('created_at')

            match event_type:
                case 'CommitCommentEvent':
                    message_event = f"{date} : Make a commit comment at {repo['name']}"
                    print(message_event)
                case 'CreateEvent':
                    if payload['ref_type'] == 'repository':
                        message_event = f"{date} : Created a new repository called {repo['name']}"
                        print(message_event)
                    elif payload['ref_type'] == 'branch':
                        message_event = f"{date} : Created a new branch at {repo['name']}"
                        print(message_event)
                    else:
                        message_event = f"{date} : Created a new tag at {repo['name']}"
                        print(message_event)
                case 'DeleteEvent':
                    message_event = f"{date} : Deleted something at {repo['name']}"
                    print(message_event)
                case 'ForkEvent':
                    message_event = f"{date} : Forked {repo['name']}"
                    print(message_event)
                case 'GollumEvent':
                    page_action = payload['pages']['action']

                    if page_action == 'created':
                        message_event = f"{date} : Created a new wiki for {repo['name']}"
                        print(message_event)
                    else:
                        message_event = f"{date} : Updated a wiki of {repo['name']}"
                        print(message_event)
                case 'IssueCommentEvent':
                    comment_action = payload['action']

                    if comment_action == 'created':
                        message_event = f"{date} : Created a issue comment at {repo['name']}"
                        print(message_event)
                    elif comment_action == 'edited':
                        message_event = f"{date} : Edited a issue comment at {repo['name']}"
                        print(message_event)
                    else:
                        message_event = f"{date} : Deleted a issue comment at {repo['name']}"
                        print(message_event)
                case 'IssuesEvent':
                    issue_action = payload['action']

                    if issue_action == 'opened' or issue_action == 'reopened':
                        message_event = f"{date} : Opened a issue at {repo['name']}"
                        print(message_event)
                    elif issue_action == 'edited':
                        message_event = f"{date} : Edited a issue at {repo['name']}"
                        print(message_event)
                    elif issue_action == 'deleted':
                        message_event = f"{date} : Deleted a issue at {repo['name']}"
                        print(message_event)
                case 'MemberEvent':
                    member_action = payload['action']
                    member_added = payload['member']['name']

                    if member_action == 'added':
                        message_event = f"{date} : Accepted {member_added} at {repo['name']}"
                        print(message_event)
                case 'PublicEvent':
                    message_event = f"{date} : {repo['name']} turned public"
                    print(message_event)
                case 'PullRequestEvent':
                    pull_request = payload['action']

                    if pull_request == 'opened':
                        message_event = f"{date} : Open a pull request at {repo['name']}"
                        print(message_event)
                case 'PullRequestReviewEvent':
                    message_event = f"{date} : Created a pull request review at {repo['name']}"
                    print(message_event)
                case 'PullRequestReviewCommentEvent':
                    pull_request_comment = payload['action']

                    if pull_request_comment == 'created':
                        message_event = f"{date} : Created a comment on a pull request review at {repo['name']}"
                        print(message_event)
                case 'PullRequestReviewThreadEvent':
                    pull_request_review_action = payload['action']

                    if pull_request_review_action == 'resolved':
                        message_event = f"{date} : The comment on pull request for {repo['name']} is resolved"
                        print(message_event)
                    elif pull_request_review_action == 'unresolved':
                        message_event = f"{date} : The comment on pull request for {repo['name']} have been marked as unresolved"
                        print(message_event)
                case 'PushEvent':

                    message_event = f"{date} : Push 1 new commit at {repo['name']}"
                    print(message_event)
                case 'ReleaseEvent':
                    message_event = f"{date} : Create a new release at {repo['name']}"
                    print(message_event)
                case 'SponsorshipEvent':
                    sponsor_action = payload['action']

                    if sponsor_action == 'created':
                        message_event = f"{date} : Sponsored {repo['name']}"
                        print(message_event)
                case 'WatchEvent':
                    message_event = f"{date} : Starred {repo['name']}"
                    print(message_event)
                case _:
                    print("Not added event type")
    elif response.status_code == 404:
        print("User not found!")
    else:
        print("Request failed!")