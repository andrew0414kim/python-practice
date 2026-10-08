
shots = [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]

def calculate_fg_percentage(shot_results):
    makes = sum(shot_results)

    attempts = len(shot_results)
    fg_pct = makes / attempts
    return fg_pct, makes

fg_pct,makes = calculate_fg_percentage(shots)
print(f"{fg_pct:.1%}, {makes} makes out of {len(shots)}")