# Perform Dense Rank on the scores (descending order) and return two columns (scores and rank) in sorted
# ascending order of rank.

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    return scores[['score', 'rank']].sort_values(by=['rank'])