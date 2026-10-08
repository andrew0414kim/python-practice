

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
    },
    {
        "Name": "Daniel",
        "Team": "UVA",
        "FGM": 0,
        "FGA": 0
    }
]

total_fga = 0
total_fgm = 0


def calculate_fg_pct(makes, attempts):
    if attempts == 0:
        return 0
    return makes / attempts

for player in players:
    total_fga += player['FGA']
    total_fgm += player['FGM']
    percentage = calculate_fg_pct(player['FGM'], player['FGA'])
    print(f"{player['Name']}: {percentage:.1%}")
print(f"Team Shooting %: {calculate_fg_pct(total_fgm, total_fga):.1%}")