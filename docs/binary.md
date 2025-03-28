# Binary
It has only two digits: 0 and 1.

---
## What Are Decimal and Binary?

- **Decimal (Base 10)**: What we normally use. It has digits from 0 to 9.
- **Binary (Base 2)**: Used by computers. It has only two digits: 0 and 1.

### Decimal to Binary (Step-by-Step)

**Example: Convert 13 to binary**

1. **Divide the number by 2**, write down the **remainder**.
2. **Repeat with the quotient** until you get to 0.
3. **Binary = remainders read bottom to top**.

| Division           | Quotient | Remainder |
|--------------------|----------|-----------|
| 13 ÷ 2             | 6        | 1         |
| 6 ÷ 2              | 3        | 0         |
| 3 ÷ 2              | 1        | 1         |
| 1 ÷ 2              | 0        | 1         |

So, **13 in binary = 1101**


### Binary to Decimal (Step-by-Step)

**Example: Convert 1101 to decimal**

1. Start from the **rightmost digit**, assign powers of 2:  
   `1×2³ + 1×2² + 0×2¹ + 1×2⁰`
2. Compute each term:
   `1×8 + 1×4 + 0×2 + 1×1 = 13`

So, **1101 in decimal = 13**


### Tips

- In binary, each digit represents a power of 2,
- Read decimal: binary from bottom up after dividing,
- Read binary: decimal from right to left using powers of 2.


### First: Real Numbers = Integers + Fractions

Real numbers can have:
- An **integer part** (like 10 in 10.1)
- A **fractional part** (like .1 in 10.1)


### Decimal to Binary: Real Numbers (Integers + Fractions)

Let’s break it down.

### 1. Integer Part: Same as before  
Just divide by 2, track remainders.

**Example**: 10 --> binary  
10 ÷ 2 = 5 remainder 0  
5 ÷ 2 = 2 remainder 1  
2 ÷ 2 = 1 remainder 0  
1 ÷ 2 = 0 remainder 1  
> Binary = `1010`


#### 2. Fractional Part: Multiply by 2, track *whole number*  

**Example**: 0.1 in decimal to binary

1. 0.1 × 2 = 0.2 --> whole part: 0  
2. 0.2 × 2 = 0.4 --> whole part: 0  
3. 0.4 × 2 = 0.8 --> whole part: 0  
4. 0.8 × 2 = 1.6 --> whole part: 1  
5. 0.6 × 2 = 1.2 --> whole part: 1  
6. 0.2 × 2 = 0.4 --> starts repeating...

So, **0.1 decimal ≈ 0.0001100110011... (binary, repeating)**


#### Putting it together

**10.1 decimal = 1010.0001100110011... (binary, repeating)**

### Irrational Numbers in Binary (like π or √2)
Just like in decimal, **irrational numbers** never end and never repeat.

- **π ≈ 3.14159...**
  - Binary approximation:  
    `π ≈ 11.001001000011111... (binary)`  
    It goes on *forever* without repeating.

- **√2 ≈ 1.41421...**
  - Binary:  
    `√2 ≈ 1.01101010000010... (binary)`  

Computers store only a limited number of binary digits (bits), so these are always **approximated**.

| Decimal Number | Binary Equivalent           |
|----------------|-----------------------------|
| 10             | 1010                        |
| 0.1            | 0.0001100110011... (repeat) |
| 10.1           | 1010.0001100110011...       |
| π              | 11.001001000011111...       |
| √2             | 1.01101010000010...         |

### What Is *Scientific Binary Form*?

It’s like **scientific notation** in decimal — but using **base 2 (binary)** instead of base 10.

### In decimal scientific notation:
**10,000 = 1.0 × 10⁴**  
**0.00052 = 5.2 × 10⁻⁴**

We're rewriting the number so there's **one digit before the decimal point**, and the rest in the fraction part, then multiplied by a power of 10.


#### In *binary*, it’s the same idea, but:

- The base is **2**, not 10.
- There’s **one 1 before the binary point**, then the rest are the fractional digits.
- Multiplied by **2ⁿ** instead of 10ⁿ.

#### Examples:

##### Binary: `1010.00011`  
Let’s convert to scientific binary:

We move the point **3 places to the left** to make `1.01000011`  

So:

> `1010.00011 = 1.01000011 × 2³` :: this is scientific binary form.

##### Binary: `0.000101`  
Move the point **4 places to the right** to get `1.01`  

So:

> `0.000101 = 1.01 × 2⁻⁴` ← another example of scientific binary form.


Computers store numbers this way using `IEEE 754`:
- The `1.` part becomes the **mantissa** (but without the leading 1 — it's "hidden").
- The exponent (power of 2) is stored separately.
- The sign is stored too.


---
---

## How Computers Store Real Numbers
It uses something called the **`IEEE 754` Floating-Point Format**.

### What is `IEEE 754`?

`IEEE 754` is the **standard** format for storing **real (floating-point) numbers** in binary on computers.

Just like scientific notation (e.g., `1.23 × 10⁴`), it breaks numbers into:

#### Three Parts:
| Part                           | Description                           |
|--------------------------------|---------------------------------------|
| **Sign bit**                   | 0 = positive, 1 = negative            |
| **Exponent**                   | Adjusts the "scale" (base-2 exponent) |
| **Mantissa** (aka significand) | The actual digits (in binary)         |

## Format Types

| Type                | Bits | Sign | Exponent | Mantissa |
|---------------------|------|------|----------|----------|
| **Float (single)**  | 32   | 1    | 8        | 23       |
| **Double**          | 64   | 1    | 11       | 52       |

Most programming languages use **double** as default.


## Example: 10.1 as 32-bit float (`IEEE 754`)

Let’s store `10.1` as a 32-bit float:

### Step 1: Convert to binary
We already saw:  
**10.1 decimal = 1010.0001100110011... (binary)**

Rewrite in scientific binary form:  
`1.0100001100110011... × 2³`

### Step 2: Fill the `IEEE 754` parts

#### 1. Sign bit = 0 (positive)

#### 2. Exponent:
- True exponent = 3  
- Bias for 32-bit = 127 --> **Stored exponent = 127 + 3 = 130**  
- 130 in binary = `10000010`
>###  What is a "bias"?
>
>In `IEEE 754` format (for both float and double), **the exponent is stored with a bias**.  
>This means we **add a fixed number** (the *bias*) to the actual exponent so we can store **both positive and negative exponents** using only **unsigned binary numbers**.
>
>### Why not just use negative numbers?
>
>Because exponents are stored in **binary**, and binary (as stored in bits) doesn’t directly support negative numbers without extra logic.  
>So instead of storing `-3`, `0`, `+5`, etc., we shift everything **upward** by a fixed number --> the **bias**.
>
>###  What is the bias?
>
>| Format               | Exponent Bits  | Bias       |
>|----------------------|----------------|------------|
>| **Float (32-bit)**   | 8              | **127**    |
>| **Double (64-bit)**  | 11             | **1023**   |
>
>So:
>- If your actual exponent is `0`, you store `127` (in binary: `01111111`)
>- If your actual exponent is `3`, you store `130` (`127 + 3`)
>- If your actual exponent is `-3`, you store `124` (`127 - 3`)
>
>
>### Where did 127 come from?
>
>Because you have **8 bits** for the exponent in float, the max value you can store is:
>
>```bash
>2⁸ = 256 possible values
>```
>
>The bias is chosen as:  
>* `bias = 2ⁿ⁻¹ - 1 = 2⁷ - 1 = 127`
>
>This allows exponents to range from `-126` to `+127` (0 and 255 are reserved).
>
>### Summary
>
>- The **bias** is a trick to let computers store **signed exponents** using **unsigned bits**.
>- **127** is the bias for **32-bit floats** (because of the 8-bit exponent field).



#### 3. Mantissa (drop the leading 1):
Take 23 bits after the dot from:  
`.01000011001100110011001`

#### Final `IEEE 754` (32-bit) representation:

```bash
Sign | Exponent     | Mantissa
  0  | 10000010     | 01000011001100110011001
```

* Binary: `01000001001000011001100110011001`  
* This is how 10.1 is stored as a float!


### What about π?

`π` ≈ 3.1415926535  
`IEEE 754` (32-bit float):  
```bash
01000000010010010000111111011011
```

`IEEE 754` (64-bit double):  
```bash
0100000000001001001000011111101101010100010001000010110100011000
```

### Why Use This Format?
- Can represent **very large** and **very small** numbers.
- Allows **efficient calculations** in hardware.
- But it has **limited precision** (e.g., 32 bits ≈ 7 decimal digits).

---
---
---

## IEEE 754 (32-bit Float) Format — Visual Cheat Sheet

```html
+---+----------+-------------------------------+
| S | Exponent |       Mantissa (Fraction)     |
| 1 |   8 bits |            23 bits            |
+---+----------+-------------------------------+
```


### Each Part Explained

| Field        | Bits | What it Stores                     | Example for 10.1             |
|--------------|------|------------------------------------|------------------------------|
| **Sign**     | 1    | 0 = positive, 1 = negative         | 0 (10.1 is positive)         |
| **Exponent** | 8    | Stored as: `actual exponent + 127` | 130 = `3 + 127` → `10000010` |
| **Mantissa** | 23   | Binary digits after leading 1      | 01000011001100110011001      |


### Scientific Binary Form

Just like decimal `1.23 × 10⁴`, binary uses:  
> `1.xxx... × 2ⁿ`

So for `10.1`:
- Binary: `1010.0001100110011...`
- Scientific binary: `1.0100001100110011 × 2³`

* **Exponent = 3**  
* **Stored exponent = 127 + 3 = 130**


### Bias Formula

For any format:

```html
bias = 2^(number of exponent bits - 1) - 1
```

| Format     | Exponent Bits  | Bias |
|------------|----------------|------|
| 32-bit     | 8              | 127  |
| 64-bit     | 11             | 1023 |
| 16-bit     | 5              | 15   |


### Final 32-bit Binary (for 10.1)

```html
0 10000010 01000011001100110011001
 ↑    ↑               ↑
 |    |               |
sign  exponent        mantissa (23 bits)
```

### Tips to Remember

- Scientific binary → move point to get `1.xxxx × 2ⁿ`
- Exponent = how many moves → add bias (127 or 1023)
- Mantissa = bits **after** the leading 1 (the 1 is implied!)
- IEEE format is just a clever way to pack this info into binary bits

