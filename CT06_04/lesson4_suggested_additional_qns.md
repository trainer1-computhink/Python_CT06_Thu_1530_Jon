## 1) Ang Bao “Exact Split” Challenge (ceil / floor)

You are packing **`money`** dollars into **`kids`** ang baos.
Each kid must get the **same integer amount**, and you must ensure you prepare **enough** even if it doesn’t divide evenly.

* Print exactly:

```
Each gets: <each>
Prepare: <needed>
Extra needed: <extra>
```
```
**Input  (not to be shown) **

* `money` (string from input)
* `kids` (string from input)

**Task (not to be shown)**

* Convert inputs properly.
* Compute:

  * `each = floor(money / kids)`
  * `needed = ceil(money / kids) * kids`  (total money you must prepare)
  * `extra = needed - money`
```
---

## 2) Pineapple Tart Ring Box (pi + round)

A pineapple tart box is shaped like a **ring** (donut shape).
Outer radius = `R`, inner radius = `r` (both in cm).
Area of ring = π(R² − r²)

**Input**

* `R`, `r` (strings)

**Task**

* Convert to float.
* Compute area and **round to 2 dp**.
* Print:

```
Ring area: <area>
```

---

## 3) Reunion Dinner Bill Shock (abs + PEMDAS)

Your family budgeted `budget` dollars. The final bill is `bill` dollars.
You want to show how far off you are **in absolute dollars**, but also include a **10% service charge already inside bill** (meaning bill includes it).

**Input**

* `budget`, `bill` (strings)

**Task**

* Convert to float.
* Compute **pre-service cost**: `bill / 1.1`
* Difference from budget: `abs(pre_service - budget)`
* Round difference to 2 dp.
* Print:

```
Pre-service: <pre_service rounded 2dp>
Off by: <difference rounded 2dp>
```

---

## 4) Mandarin Orange “Fair Bagging” (floor + remainder logic without %)

You have `oranges` oranges and want to pack them into `bags` bags as evenly as possible.
No bag can have more than 1 orange difference compared to another.

**Input**

* `oranges`, `bags` (strings)

**Task**

* Convert to int.
* Compute:

  * `base = floor(oranges / bags)`
  * `left = oranges - base * bags`
* Print:

```
Base per bag: <base>
Bags with one extra: <left>
```

---

## 5) Firecracker Countdown Timer (string concat + math)

You want a countdown board that displays:
`"T-" + seconds + "s"`
But the input might be `"060"` or `"60"`.

**Input**

* `seconds` (string)

**Task**

* Convert properly to int, then back to string (no leading zeros).
* Print exactly:

```
T-<seconds>s
```

---

## 6) Lion Dance Drum Beats (PEMDAS + round)

The drum beat speed changes based on excitement level.

**Input**

* `base_bpm` (string), `level` (string)

**Rule**
Final BPM = `base_bpm * (1 + level/20) + 3`

**Task**

* Convert to float.
* Apply PEMDAS correctly.
* Round final BPM to **nearest integer**.
* Print:

```
Final BPM: <integer>
```

---

## 7) Lantern Distance Check (abs + ceil)

Two lanterns are hung at positions `a` and `b` (in meters along a corridor).
A safety officer wants the distance rounded **up** to the next whole meter.

**Input**

* `a`, `b` (strings)

**Task**

* Convert to float.
* Compute `ceil(abs(a - b))`
* Print:

```
Safety distance: <distance>
```

---

## 8) CNY Sale Price Tag (type conversion + concatenation + round)

A shop shows original price `p` and discount `d` percent (e.g. `15` means 15%).
Print a nice label like:
`"Sale: $" + <final price to 2dp>`

**Input**

* `p`, `d` (strings)

**Task**

* Convert to float.
* Final = `p * (1 - d/100)`
* Round to 2 dp.
* Print exactly:

```
Sale: $<price>
```

---

## 9) Hotpot Table Spacing (floor + pi)

Each round table has diameter `D` meters. You have a hall length `L` meters.
You can fit tables in one row with **0.5m gap** between tables.

**Input**

* `D`, `L` (strings)

**Task**

* Convert to float.
* Table space needed per table = `D + 0.5` (except last table still needs full diameter; using this simplified model is intended)
* Compute max tables = `floor(L / (D + 0.5))`
* Also compute table top area of ONE table: `pi*(D/2)**2`, rounded to 2 dp
* Print:

```
Tables: <max>
One table area: <area>
```

---

## 10) Zodiac Wheel Spin (floor + abs + tricky input)

A zodiac wheel has 12 animals numbered 0–11.
Starting position is `start`. The wheel is spun by `spin` steps (can be negative).
You want the final position but you must do it **without %**.

**Input**

* `start`, `spin` (strings)

**Task**

* Convert to int.
* Compute:

  * `pos = start + spin`
  * Adjust to be within 0–11 using only:

    * `floor(pos/12)` and multiplication/subtraction
* Print:

```
Final position: <pos_in_0_to_11>
```
