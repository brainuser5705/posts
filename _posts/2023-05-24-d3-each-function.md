---
layout: post
title: Using D3.each()
date: 2023-05-24
categories: d3 tutorial
---

This blog post describes when and how to `d3.each()`.

---

## Starting with call()

The D3 `call()` function's primary purpose is to enable "synthetic" function calls while passing the current D3 `Selection` instance as an argument. As read in "D3 for the Impatient" by Philipp K. Janert, its usage is the most idiomatic way of invoking functions, since it returns the same D3 `Selection` instance for method chaining. 

**Here's an example:**  
*(ignore the fact that it's more verbose than setting the attribute directly)*

```js
var svg = d3.select("svg");

function makeRed(sel){
    sel.attr("fill", "red");
}

svg.append("circle")
    .attr("r", 100)
    .attr("cx", 100)
    .attr("cy", 100)
    .call(makeRed); // invoke makeRed() passing the circle SVG element
```

`call()` also allows additional arguments to pass in the form of `call(function, [arguments])`.

```js
var svg = d3.select("svg");

function makeColor(sel, color){
    sel.attr("fill", color);
}

svg.append("circle")
    .attr("r", 100)
    .attr("cx", 100)
    .attr("cy", 100)
    .call(makeColor, "red"); // color string is passed explicity
```

The main thing is that the invoked function should take in a `Selection` argument and do something with it.

---

## Switching to each()

**So what happens when you want to invoke the same function for a list of elements?** Note that the function manipulates the DOM element (by changing the fill color), so we will need to be able to get the bounded DOM element for each data item.

Let's say you have this code:

```javascript
var colors = ["red", "blue", "green"];
var spacing = 100;

var svg = d3.select("svg");

function makeColor(sel, color){
    sel.attr("fill", color);
}

svg.selectAll("text")
    .data(colors).enter()
    .append("text").text("Hello!")
    .attr("x", (d,i)=>i*spacing).attr("y",30)
    .attr("font-size", 20)
    // what do we put here?
```

How can we invoke `makeColor()` for each of the newly created `<text>` elements? Unfortunately we cannot simply chain with `call(makeColor(this, d=>d))`. The reason being that `call()` only invokes the function once, and doesn't pass any parameters related to the data element.

Instead we have to use `each()` which does pass data element related arguments:
- `d` - the current data item
- `i` - the index of the data item
- `nodes` - an array of DOM nodes bounded to the data

Because it doesn't pass the original selection (aka the parent) contrary to `call(), we'll only be able to invoke the function to manipulate the bounded DOM elements in a roundabout way:

```javascript
// setup code segments omitted

var colors = ["red", "blue", "green"];
var spacing = 100;

var svg = d3.select("svg");

function makeColor(sel, color){
    sel.attr("fill", color);
}

svg.selectAll("text")
    .data(colors).enter()
    .append("text").text("Hello!")
    .attr("x", (d,i)=>i*spacing).attr("y",30)
    .attr("font-size", 20)
    .each(function(d,i,ns){
        makeColor(d3.select(ns[i]), d);
    });
```

1. In `each()`, we create an anonymous function that accepts the three parameters.
2. We then invoke `makeColor()` as a regular function call. The function accepts a `Selection` instance and additional arguments just like the function in the `call()` example.
3. We obtain the DOM element with `ns[i]`, essentially indexing in the `nodes` array. It has to be wrapped in a `Selection` abstraction so we use `d3.select()`.
4. The next argument is the color, so we can pass the data item `d`.

---

## Sources
1. [Stack Overflow](https://stackoverflow.com/questions/47337119/how-can-i-get-call-to-execute-for-each-data-element-in-d3)