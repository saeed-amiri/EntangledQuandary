# Foundations of Two’s Complement:
$$
-B = \mathrm{NOT}(B) + 1
$$  
in an $n$-bit binary system. We’ll talk about **wrapping around** in modular arithmetic, which is the real underlying reason.

- **Two’s complement** is a way to represent negative numbers in binary.
- It’s based on the idea of **modular arithmetic**.

## 1. The Essence: We’re in “Mod $2^n$”

When we store numbers in $n$-bit binary, we’re effectively working **mod $2^n$**. That means all arithmetic wraps around at $2^n$.  

- The largest unsigned $n$-bit value is $2^n - 1$.  
- If you add 1 to $2^n - 1$, you wrap around to 0.

In that sense, saying “$-B$” in $n$-bit binary means:  
$$
(-B) \equiv 2^n - B \pmod{2^n}.
$$  
This is how we define the negative in a fixed-bit system: the number you add to $B$ to get a total of 0 modulo $2^n$.


## 2. Two’s Complement = $\bigl(2^n - 1 - B\bigr) + 1$

The expression $2^n - B$:

1. $2^n - 1$ is an $n$-bit number full of 1’s in binary.  
   - Example for $n=4$: $2^4 - 1 = 15 = 1111_2$.

2. If you do $(2^n - 1) - B$, that’s exactly the **bitwise NOT** of $B$.  
   - Because `(all 1s) - B` flips every bit of $B$.  

3. Then adding 1 gives you $2^n - B$.

So:

$$
2^n - B = \bigl[(2^n - 1) - B \bigr] + 1 = \mathrm{NOT}(B) + 1.
$$

Hence, in an $n$-bit system,

$$
-B \;\equiv\; 2^n - B \;\equiv\; \mathrm{NOT}(B) + 1 \pmod{2^n}.
$$

That’s the deeper logic.

## 3. Verifying: $B + \bigl(\mathrm{NOT}(B) + 1\bigr) = 2^n$

Because $\mathrm{NOT}(B)$ = $(2^n - 1) - B$, we get:

$$
B + \mathrm{NOT}(B) = B + \bigl((2^n - 1) - B\bigr) = 2^n - 1.
$$

Add 1 more:

$$
B + [\mathrm{NOT}(B) + 1] = (2^n - 1) + 1 = 2^n.
$$

In binary, adding up to $2^n$ means you produce a carry out of the $n$-th bit, leaving 0 in those $n$ bits. That’s exactly how the system represents 0 in mod $2^n$. So:

$$
B + (-B) \equiv 2^n \equiv 0 \;(\text{mod }2^n),
$$

which shows $\mathrm{NOT}(B) + 1$ must be $-B$ in this system.

## 4. Concrete Example Tying It All Together

Let’s pick $n=4$, so $2^n = 16$. Suppose $B=6$.  
- $2^n - 1 = 15 = (1111)_2$.  
- $B=6=(0110)_2$.  

1) $\mathrm{NOT}(B) = 1001_2 = 9$.  
2) $\mathrm{NOT}(B) + 1 = 1001 + 0001 = 1010_2 = 10$.  
3) Check $B + (-B)$:  
   - $6 + 10 = 16$.  
   - $16$ in 4-bit mod-16 arithmetic is 0 (with a carry out of the 4th bit).

Thus, in a 4-bit system, $10_{decimal}$ is indeed $-6$.

---
- We live in an **$n$-bit modulo $2^n$ world**.  
- Negative numbers are represented by the number that, when added to the positive counterpart, sums to $2^n$ (which is effectively 0 with an overflow carry).  
- **That number** is exactly $\mathrm{NOT}(B) + 1$.  

Hence:

$$
-B \equiv \mathrm{NOT}(B) + 1 \pmod{2^n}.
$$

---
---

## Example 1: Two's Complement in Binary
### **What exactly is a negative number in binary?**

Computers can't "directly" represent negative numbers easily. They represent negative numbers as **special positive numbers** in binary called **two's complement** numbers.

To get the negative number (`-B`) in two's complement, we do two things clearly:

- **Step 1:** Flip each bit of B (**NOT** operation).
- **Step 2:** Add **1** to the flipped bits.


**Decimal example:**  
Consider `B = 3` in binary (`011`). What would `-3` look like?

Let's use 3 bits for simplicity:

| Number | Binary |
|--------|--------|
| 3      | `011`  |

Let’s apply the rule clearly:

- **NOT(011)** = `100`
- **Add 1** → `100 + 1 = 101`

We got `-3` = `101` (binary).

Let’s quickly confirm if this actually works:

```css
   011 (3)
 + 101 (-3)
---------
  1000 
```

With 3 bits, the leftmost bit (`1`) is carried out and discarded, leaving:

```css
000 = 0  correct
```

This shows clearly that `101` is the correct binary representation of `-3`.


### **Why "NOT(B) + 1"? (The Core Intuition)**

In any binary system, if you take any number and **add its NOT**, you get a number that's all ones:

- **General formula:**  
$$
B + \text{NOT}(B) = 111...111
$$

For example, let's verify clearly again:

```css
  B =  011  (3)
+ NOT =100
---------
       111
```

We got **111**.

Now, if we add **1** more to `111` (all ones), we reach a number that goes over (wraps around) and becomes zero:

```css
  111 (all ones)
+   1
-------
 1000 (wrap around → 000)
```

The carry (`1`) exceeds the number of bits we have, making the result effectively zero. 

Thus, clearly:

- **NOT(B) + 1 is the exact value you need to add to B to wrap around and get zero.** 

This means:

$$
B + [\text{NOT}(B) + 1] = 0
$$

If you rearrange this clearly, you see:

$$
-B = \text{NOT}(B) + 1
$$

In other words, **NOT(B) + 1** is perfectly the negative of B in binary!

---

### **Summary:**  
- `NOT(B)` alone is not enough (it gives "one less than negative B").
- Adding **1** fixes it, creating a "wrap-around" effect, perfectly creating negative numbers in binary.


### **Test it with another quick example (optional)**:  
- Take `B = 1` (binary `001`):
- NOT(001) = `110`  
- Add `1`: `110 + 1 = 111` = `-1`

Check again clearly:
```css
 001 (1)
+111 (-1)
--------
1000 → overflow = 000 = 0 Correct!
```


**Negative numbers are represented using two’s complement** because:

$$
B + \text{NOT}(B) = 111...111
$$

Adding **1** to this (all ones) gives you a **wrap-around** (zero), so clearly:

$$
-B = \text{NOT}(B) + 1
$$

---
---