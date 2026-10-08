
shots = [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]

def calculate_fg_percentage(shot_results):
    makes = sum(shot_results)

    attempts = len(shot_results)
    fg_pct = makes / attempts
    return fg_pct, makes

fg_pct,makes = calculate_fg_percentage(shots)
print(f"{fg_pct:.1%}, {makes} makes out of {len(shots)}")

player = {
    "Name": "Andrew",
    "Team":  "UVA",
    "FGM": 8,
    "FGA": 15,
    "3PM": 3,
    "3PA": 7
}

player["FGM"] += 2
player["FGA"] += 3
player["3PM"] += 1
player["3PA"] += 2

print(f"{player['Name']} ({player['Team']})")
print(f"FG%: {player['FGM'] / player['FGA']:.1%}")
print(f"3P%: {player['3PM'] / player['3PA']:.1%}")


players = [
    {
        "Name": "Andrew",
        "Team": "UVA",
        "FGM": 10,
        "FGA": 18
    },
    {
        "Name": "James",
        "Team": "UVA",
        "FGM": 6,
        "FGA": 12
    },
    {
        "Name": "Michael",
        "Team": "UVA",
        "FGM": 9,
        "FGA": 15
    }
]

total_fga = 0
total_fgm = 0

for player in players:
    total_fga += player['FGA']
    total_fgm += player['FGM']
    fg_pct = player["FGM"] / player["FGA"]
    print(f"{player['Name']}: {fg_pct:.1%}")
print(f"Team Shooting %: {(total_fgm / total_fga):.1%}")