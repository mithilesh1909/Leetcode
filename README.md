# LeetCode POTD

Solving LeetCode's Problem of the Day, one push at a time.

![Day](https://img.shields.io/badge/day-123-blue)
![Solved](https://img.shields.io/badge/solved-123-green)

## Progress

Auto-updated on every push — see [How this updates](#how-this-updates).

<!-- TRACKER_START -->

| Day | Date | Problem |
|:---:|:---:|:---|
| 123 | 2026-09-07 | _(add problem name)_ |
| 122 | 2026-09-07 | _(add problem name)_ |
| 121 | 2026-09-07 | _(add problem name)_ |
| 120 | 2026-09-07 | _(add problem name)_ |
| 119 | 2026-09-07 | _(add problem name)_ |
| 118 | 2026-09-07 | _(add problem name)_ |
| 117 | 2026-09-07 | _(add problem name)_ |
| 116 | 2026-09-07 | _(add problem name)_ |
| 115 | 2026-09-07 | _(add problem name)_ |
| 114 | 2026-09-07 | _(add problem name)_ |

_Last updated: 2026-09-07_

<!-- TRACKER_END -->

## Structure

```
Leetcode/
├── Day-001/
│   └── solution.py
├── Day-002/
│   └── solution.py
├── ...
├── Day-122/
│   └── solution.py
├── scripts/
│   └── update_tracker.py
├── progress_log.json
└── README.md
```

## How this updates

1. Solve today's problem, push it as `Day-123/`, `Day-124/`, and so on.
2. A GitHub Action scans all `Day-*` folders, recalculates the day count, and rewrites the badges and table above.
3. The bot commits the change back. Just push your solution — the count takes care of itself.

To label a day's problem, edit its entry in `progress_log.json` and set `"problem"` to the problem name.
