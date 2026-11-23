# news-image-20261122 — World News, Sunday, November 22, 2026

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/Cm11w/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/Cm11w/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

One 1024x1024 PNG summarising the world news of Sunday, 22 November
2026 as a newspaper front page: a dark masthead with the date, one lead
story, and four further stories in a 2x2 grid, with a one-line source
footer. Built Sunday 22 November 2026 ~07:45 WIB (00:45 UTC) as a morning
snapshot, then REFRESHED Monday 23 November 2026 ~07:00 WIB (00:00 UTC,
after 22 Nov ended UTC) — see `research-22nov.md`, section
"REFRESH — HASIL": the lead is now the confirmed COP31 collapse, and a
new Gulf story replaces the FBI story.

## The five stories (all traceable to `research-22nov.md`)

1. **CLIMATE — COP31 collapses with no deal at all** (lead): the summit
   in Antalya ended on Sunday after the EU and others rejected a final
   text with no mention of fossil fuels; the president conceded there was
   no agreement. It is the longest COP ever and the first to end with no
   deal since 2000; UN chief Guterres called the outcome deeply
   disappointing. Sources: AP, UN News, Greenpeace.
2. **WAR — Russian drone collapses Kyiv apartment block**: a drone hit a
   five-storey block in Dymer, near Kyiv, on Sunday; at least 14 people
   are missing, Zelensky said. Russia fired 3 missiles and 148 drones
   overnight, Kyiv said. Sources: Euronews, France 24, IBTimes, AP.
3. **MIDDLE EAST — Israeli strike kills 3 in Gaza aid vehicle**: three
   people killed in Gaza City on Saturday, Gaza Health Ministry said;
   Israel said it hit Islamic Jihad militants in a truck bearing a World
   Central Kitchen logo; WCK said it was not its vehicle. Sources:
   Reuters, The Media Line.
4. **GULF — Iran strikes US bases in Bahrain** (new in the refresh,
   replaces the FBI story): Iran said it fired missiles and drones at US
   Patriot radars at two bases on Saturday night. Bahrain said a civilian
   site was hit and two people were hurt; the US said its forces were
   unharmed. Sources: Reuters, Xinhua, Al Jazeera, IRNA.
5. **MARKETS — Bitcoin rebounds past $61,000**: Bitcoin fell to $55,830
   on Friday, its lowest since September 2024; it rose 8% on Saturday and
   past $61,000 on Sunday, after $2.4bn in futures were liquidated in a
   day. Sources: Reuters, Binance/Finnhub, news.bitcoin.com.

Honesty notes (from the research): most events took place on Saturday,
Nov 21, and were reported on Sunday, Nov 22 — the image says "as
reported on Sunday" in the masthead. COP31 is "collapses with no deal"
because the final text was formally rejected and the president conceded
no agreement — confirmed, no longer "deadlocked". The Gaza victims are
not called WCK workers or militants (both claims are attributed); the
IRGC claim that it hit US Patriot radars is attributed to Iran, with
Bahrain's and the US accounts alongside it and no independent
confirmation claimed. The FBI breach story was displaced by the Gulf
strike (still reported on Sunday, but smaller); the unverified "Sunday
tanker" report from arabiansea.co.uk was left out (no UKMTO warning
number found).

## How to run

```sh
python3 draw_entry.py   # regenerates entry.png (deterministic)
node main.ts             # copies entry.png to $MAKEFUN_OUTPUT_DIR (default /output)
```

`draw_entry.py` draws everything with PIL (Noto Sans) and aborts with
an error if any text would overflow its card. Two runs produce a
byte-identical PNG.

## Files

- `draw_entry.py` — fresh PIL drawing script for this entry
- `entry.png` — the image (1024x1024, < 1 MiB)
- `main.ts` — copies `entry.png` to the output directory
- `research-22nov.md` — the research behind every sentence
- `LICENSE` — license
