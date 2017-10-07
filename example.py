from pywildhacks import WildhacksClient

client = WildhacksClient()
talks = client.get_talks()
users = client.get_users()
events = client.get_events()
teams = client.get_teams()