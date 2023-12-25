---
layout: post
title: \`pack\` function in Haskell
date: 2023-12-24
tags: functional-programming
---

Explanation of my implementation for the [`pack` problem (9)](https://wiki.haskell.org/99_questions/1_to_10) and a brief look into type declarations for functions

---

## Problem

The problem is *"given a list of numbers, for each group of the consecutive numbers that are the same, put them in their own list". So `[1,2,2,1,1,4,4,5]` => `[[1], [2,2], [1,1], [4,4], [5]]`.

## Solution

### Base cases

```haskell
pack [] = []
pack [x] = [[x]]
```
- Self explanatory.

### Recursive cases

- My initial idea was to have an *accumulator* that would hold onto the sublists that we would create. I attempted to make a function, but ran into issues when having to "rebuild" (append a new element) to that accumulator at a recursive call.
```haskell
packHelper ys (x:xs) = 
    if  recent == x
        then initList ++ packHelper (lastList ++ [x])) xs
        else (initList ++ ) -- rebuilding the list was a lot of work
    where 
        initList= (init ys)
        lastList = (last ys)
        recent = (last lastList)
```

**New solution:**

```haskell
pack (x:xs) = packHelper 1 x xs
packHelper count x (y:[]) =
    if x == y
        then [(replicate (count+1) x)]
        else [(replicate count x)] ++ [[y]]
packHelper count x (y:ys) =
    if x == y
        then packHelper (count+1) x ys
        else [(replicate count x)] ++ (pack (y:ys))
```

- New idea is to build the sublist separate from the parameters, as show in the `if-then-else` clause. Instead I have a `count` parameter that increments each time the elements are equal.
    - If they are, then increment and call again for the rest of the list.
    - If not, then make the sublist (`replicate`) and call again with a new element to compare.
- I needed a terminating case when it reaches the last element in the list. Note that it can reduced to just when the list is empty: `packHelper count x [] = [(replicate count x)]`

> Notice that the sublists are wrapped around in *brackets* since the final result is a 2D list ([[]]). With `++` the two operands must be of the same type to concatenate together. So `[[1]] ++ [[2]]` => `[[1], [2]]`

## Type declarations

```haskell
-- for pack
pack :: (Eq a) => [a] -> [[a]]

-- for packHelper
packHelper :: (Eq a) => Int -> a -> [a] -> [[a]]
```

- `Eq` typeclass since the elements must be able to perform `x == y`.
- `Int` does not have a type variable because it's not a typeclass, it's its own type. I could have done `(Integral c, Eq a) => c -> ...` but I would be required to use `fromIntegral` whenever I use `count`.

