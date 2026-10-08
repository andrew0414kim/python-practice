import csv


def calculate_fg_pct(makes, attempts):
    if attempts == 0:
        return 0
    return makes / attempts


players = []

with open("players.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row['FGM'] = int(row['FGM'])
        row['FGA'] = int(row['FGA'])

        players.append(row)

for player in players:
    percentage = calculate_fg_pct(player['FGM'], player['FGA'])
    print(f"{player['Name']}: {percentage:.1%}")

makes = [player['FGM'] for player in players]
attempts = [player['FGA'] for player in players]

print(f"Team Shooting %: {calculate_fg_pct(sum(makes), sum(attempts)):.1%}")