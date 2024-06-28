from merge_team_stats import merge_team_stats
from get_last_perf import get_last_perf
from flat_games_stats import flat_games_stats
from add_elo_rates import add_elo_rates
from diff_stats import diff_stats

data = merge_team_stats()
data = get_last_perf(data)
data = flat_games_stats(data)
data = add_elo_rates(data)
data = diff_stats(data)

data.to_csv('../dataset/final_dataset.csv', index=False)