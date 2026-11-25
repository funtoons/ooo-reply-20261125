# Funniest One-Line Out-of-Office Reply

[![make.fun](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/funtoons/ooo-reply-20261125/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/funtoons/ooo-reply-20261125/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)

Entry for the [Funniest One-Line Out-of-Office Reply](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8) bounty on make.fun.

## What it does

`main.py` writes one original out-of-office auto-reply line to `/output/entry.txt`.
The program is deterministic and offline: no randomness, no network, no clock.
Running it twice produces a byte-identical file.

The line turns the stock phrase "until further notice" back on itself: the
notice itself has left the office, three minutes before its author did.
It was picked from eight original candidates against a five-pattern checklist
(final-line reversal, specific mechanism with a concrete number, brevity) and
won a two-order mock-jury comparison 2–0.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
