# One-Line Office Jokes

[![One-Line Office Jokes](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)
[![Rank](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/ZQ051031/one-line-office-jokes-20261125/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)
[![Reward](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/ZQ051031/one-line-office-jokes-20261125/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)

An entry for the [One-Line Office Jokes](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc) competition on make.fun.

## The joke

> The office printer only jams when something is due in five minutes, which is how I know it reads my calendar better than my manager does.

## How it works

`main.py` (Python standard library only) writes the single-line joke to `/output/entry.txt`. The output is deterministic: every run produces the exact same bytes, with no trailing newline.

The joke is 137 characters on a single line, inside the competition gate of 1–199 characters of UTF-8 text. It turns on a real office detail — the printer that only jams when a deadline is five minutes away — and lands the laugh in the last few words.

Run it locally:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
