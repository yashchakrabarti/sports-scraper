import requests
from bs4 import BeautifulSoup
import csv

urls = {"Premier League": "https://www.bbc.com/sport/football/premier-league/table", "La Liga": "https://www.bbc.com/sport/football/spanish-la-liga/table",
        "Serie A:": "https://www.bbc.com/sport/football/italian-serie-a/table", "Ligue 1": "https://www.bbc.com/sport/football/french-ligue-one/table", "Bundesliga": "https://www.bbc.com/sport/football/german-bundesliga/table"}

# output_file = csv.writer(open('prem_table.csv', 'w'))

# output_file.writerow(['Position', 'Team', 'Played', 'Won',
#                      'Drawn', 'Lost', 'For', 'Against', 'GD', 'Points'])

# result = requests.get("https://www.bbc.co.uk/sport/football/tables")

# src = result.content

# soup = BeautifulSoup(src, 'html.parser')

# table = soup.find_all("table")
# league_table = table[0]

# teams = league_table.find_all("tr")

# for team in teams[1:21]:

#     stats = team.find_all("td")

#     position = stats[0].text
#     team_name = stats[2].text
#     played = stats[3].text
#     won = stats[4].text
#     drawn = stats[5].text
#     lost = stats[6].text
#     for_goals = stats[7].text
#     against_goals = stats[8].text
#     goal_diff = stats[9].text
#     points = stats[10].text

#     output_file.writerow([position, team_name, played, won,
#                          drawn, lost, for_goals, against_goals, goal_diff, points])

def get_table(league):
    url = urls[league]
    output_file = csv.writer(open('table.csv', 'w'))


    output_file.writerow(['Position', 'Team', 'Played', 'Won',
                        'Drawn', 'Lost', 'For', 'Against', 'GD', 'Points'])

    result = requests.get(url)

    src = result.content

    soup = BeautifulSoup(src, 'html.parser')

    table = soup.find_all("table")
    league_table = table[0]

    teams = league_table.find_all("tr")

    for team in teams[1:21]:

        stats = team.find_all("td")

        position = stats[0].text
        team_name = stats[2].text
        played = stats[3].text
        won = stats[4].text
        drawn = stats[5].text
        lost = stats[6].text
        for_goals = stats[7].text
        against_goals = stats[8].text
        goal_diff = stats[9].text
        points = stats[10].text

        output_file.writerow([position, team_name, played, won,
                            drawn, lost, for_goals, against_goals, goal_diff, points])

league = input("Enter name of the league you want to see the table of:")
get_table(league)