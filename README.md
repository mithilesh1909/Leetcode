# LeetCode POTD

Solving LeetCode's Problem of the Day, one push at a time.

![Day](https://img.shields.io/badge/day-100-blue)
![Tracked](https://img.shields.io/badge/tracked_on_github-0-orange)

## Progress

Auto-updated whenever a new problem folder shows up — see [How this updates](#how-this-updates).

<!-- TRACKER_START -->

_Tracker hasn't run yet — it fills in after the first push once the workflow is set up._

<!-- TRACKER_END -->

## How this updates

This repo uses [LeetSync](https://github.com/BayBreezy/leetsync) to auto-push a folder per solved problem. A GitHub Action reads the folder history, works out which day each problem was solved (starting from **day 100**, when GitHub tracking began), and rewrites the badges and table above — no manual editing needed.

Going forward: solve a problem, let LeetSync push the folder as usual, and the tracker updates itself on the next Action run.

If the day count doesn't match your real streak after the first run, open `scripts/update_tracker.py` and adjust the `START_DAY` value, then delete `progress_log.json` and re-run the workflow to rebuild it.
