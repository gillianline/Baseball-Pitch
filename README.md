# Baseball-Pitch

1. compare_pitchers_breaks.py
Visualizes pitch break characteristics of two pitchers.

Inputs: PitcherId, PitchType, TrajectoryHorizontalBreak, TrajectoryVerticalBreakInduced
Output: Scatter plot comparing horizontal and vertical break by pitch type for:
Pitcher 11 (solid circles)
Pitcher 1 (X markers)

2. pitch_clustering.py
Uses K-Means clustering to group pitches by strike zone location and pitch type.

Inputs: GamePk, StrikeZoneBottom, StrikeZoneTop, PitchType
Output: Colored scatter plot showing 7 pitch clusters for Game 2

3. strikeout_rate_analysis.py
Compares strikeout rates by pitch type across Game 1 and Game 2.

Inputs: PitchCall, PitchType, GamePk
Output: Two line graphs showing strikeout effectiveness by pitch type


Python Requirements
pandas
numpy
matplotlib
scikit-learn

| Script                       | Visual             | Key Insight                                  |
| ---------------------------- | ------------------ | -------------------------------------------- |
| `compare_pitchers_breaks.py` | Scatter plot       | Pitch shape differences between two pitchers |
| `pitch_clustering.py`        | Clustering scatter | Common pitch zones & groupings               |
| `strikeout_rate_analysis.py` | Line plots         | Which pitch types yield more strikeouts      |
