# Logical Gates:
A *logic gate* is device that performs a Boolean function, logical operation performed on one or more binary inputs that produces a single binary output [[wiki](https://en.wikipedia.org/wiki/Logic_gate)].

## Basic Logic Gates:
>1. `NOT` Gate (Inverter)
>- Inverts the inputs,
>- Symbol: A triangle with a small circle (representing inversion) at its output.
>2. `AND` Gate:
>- Outputs true (1) only if both inputs are true,
>- Symbol: A flat-ended shape.
>3. `OR` Gate:
>- Outputs true if at least one input is true,
>- Symbol: A curved shape pointing to the output.

## Derived Gates:
>1. `NAND` Gate:
>- Outputs the inverse of the `AND` gate,
>- Symbol: `AND` + o at the end.
>2. `NOR` Gate:
>- Outputs the inverse of the `OR` gate,
>- Symbol: `OR` + o at the end.
>3. `XOR` Gate (Exclusive `OR`):
>- Outputs true if and only if one of the inputs is true,
>- Symbol: `OR` + parallel initial line of the `OR` gate.
>4. `XNOR` Gate (Exclusive `NOR`):
>- The inverse of `XOR`; outputs true if both inputs are the same,
>- Symbol: `XOR` + o at the end

|Input A|Input B| AND   | OR    | NAND  | NOR   | XOR   | XNOR  |
|-------|-------|-------|-------|-------|-------|-------|-------|
|    0  |  0    |  0    |  0    |  1    |  1    |  0    |   1   |
|    0  |  1    |  0    |  1    |  1    |  0    |  1    |   0   |
|    1  |  0    |  0    |  1    |  1    |  0    |  1    |   0   |
|    1  |  1    |  1    |  1    |  0    |  0    |  0    |   1   |


## The Basic Operations:
The overlien dash stands for `NOT`.
### `AND`  and `OR` Operations:
* `AND` operation is denoted with "$\cdot$": $A\cdot B$ or just $AB$
* `OR` operation is denoted with "$+$": $A + B$
#### Basic Axioms and Properties
* **Commutative property:**

    $A\cdot B = B\cdot A$ and $A + B = B + A$
* **Associative property:**

    $(A\cdot B)\cdot C = A\cdot(B\cdot C)$ and $(A + B) + C = A + (B + C)$
* **Distributive Property:**

    $A \cdot (B + C) = (A \cdot B) + (A \cdot C) A \cdot (B + C) = (A \cdot B) + (A \cdot C)$

    $A + (B \cdot C) = (A + B) \cdot (A + C) A + (B \cdot C) = (A + B) \cdot (A + C)$
 
---

## `NOT`

    ___________________
    |              |   |
    |              |   |
    |             /     ¯¯¯)
 ¯¯¯¯¯¯¯           |   |¯¯¯
  ¯¯|¯¯            |   |
    |______________|___|


## `AND`

    _____/ ___/ ______
    |                 |
    |                 |
    |                  ¯¯¯)
 ¯¯¯¯¯¯¯              |¯¯¯
  ¯¯|¯¯               |
    |_________________|

## `NAND`

    ___________________
    |              |   |
    |             /    |
    |              |   |
    |             /     ¯¯¯)
 ¯¯¯¯¯¯¯           |   |¯¯¯
  ¯¯|¯¯            |   |
    |______________|___|

## `OR`

    __________/ ______
    |    |____/ ____| |
    |                 |
    |                  ¯¯¯)
 ¯¯¯¯¯¯¯              |¯¯¯
  ¯¯|¯¯               |
    |_________________|

## `NOR`

    ______________________
    |              |  |   |
    |              |  |   |
    |             /  /     ¯¯¯)
 ¯¯¯¯¯¯¯           |  |   |¯¯¯
  ¯¯|¯¯            |  |   |
    |______________|__|___|

## `XOR`

    __________________
    |         |   |   |
    |         |   |   |
    |          \__*__/
 ¯¯¯¯¯¯¯      |   |   |
  ¯¯|¯¯       |   |   |
    |_________|___|___|

## `XNOR`

    __________________
    |                 |
    |                 |
    |                  ¯¯¯)
 ¯¯¯¯¯¯¯              |¯¯¯
  ¯¯|¯¯  1______1     |
    |_____      ______|
          ______
         0      0