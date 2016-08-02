# D3 Fundamentals

The goal for this lesson will be for you to understand how [goal.html](goal.html) works. Let's take a look at the code and see what we understand already.

 * `src="http://d3js.org/d3.v3.min.js" charset="utf-8"`
 * `d3.scale`, `d3.select("body")`?
 * `function(d)`, `function(d, i)`?
 * `rect`, `x`, `y`?
 * `selectAll()`, `data()`, `enter()`, `append()`?
 * `svg` a variable?
 * Coordinate space inverted?

Remember D3 is a JavaScript framework, so there are all these functions specific to D3. For the full list of functions and uses, see the [D3 API reference](https://github.com/mbostock/d3/wiki/API-Reference).

---

### Selections

D3 is **data-driven-documents**, and what that means is we are binding data to DOM elements. To do that, we need to select DOM elements, and specify what we want to bind.

There are two key functions for selections in D3:

 * `select()` - grabs one element (the first)
 * `selectAll()` - grabs all matching elements

![DOM Tree Example](http://cdn0.mos.techradar.futurecdn.net/Review%20images/Linux%20Format/Issue%20118/DOM%20tree%20inline2-420-90.jpg "DOM Tree Example")

D3 selections are based on CSS selectors, so you can use any of the following to select your d3 elements:

```
#grabthis       ==   <anything id="grabthis">
.grabthis       ==   <anything class="grabthis">
grabthis        ==   <grabthis>
grab = this     ==   <anything grab="this">
grab this       ==   <grab><this></grab>
```

*For the most part, you don't want to write code that requires you to select things in 5 different ways. Most go with the simple "grabthis" and "#grabthis" approach, but it's nice to know you have options.*

---

Let's go to [work.html](work.html) and try to do the following:

 * Grab the first `p` tag.
 * Grab all the `p` tags.

For more on how selections work, check out Mike Bostock's [awesome post about it](http://bost.ocks.org/mike/selection/).

Use D3's `.text()` and `.remove()` to play with your selections.

---

Now that we can select things, let's start styling things! Try out some of the following in [work.html](work.html):

```javascript
d3.select("p").style("color", "red");
d3.selectAll("p").style("font-size", "20px");
d3.selectAll("p").style("background-color", "green");
```

While that's fun, what we really want to learn is how to bind **data**. Type in the following and check out the result:

```javascript
d3.select("p");
```

Now enter this and see what changed:

```javascript
d3.select("p").data([10])
```

See that `__data__` property? That's your data!

Before we start going more into selections, let's talk about SVG.

---

### SVG

For every D3 visualization we do, you will need an SVG element. SVGs are html objects, so we can make them in HTML simply by writing:

```html
<svg width="700" height="700"></svg>
```

Inside that SVG is where you place your objects, which must be SVG objects. Here's an example you can add to your [work.html](work.html) file:

```javascript
<svg width="700" height="700">
  <circle cx="100" cy="100" r="50" fill="red">
</svg>
```

Add that code to your [work.html](work.html), and reload the page.

The `circle` has `attr`ibutes `cx`, `cy`, `r`, and `fill`. Note that these only partially overlap with `style`s.

Try the following:

 * Make the circle green.
 * Make the circle HUGE.
 * Make the circle tiny.
 * Make the circle disappear!

*[Go here](http://www.w3schools.com/svg/default.asp) to see all the SVG objects and what attributes they require. This is important, as often, issues with creating different SVG objects happens when one uses the wrong attributes, such as setting `x` and `y` coordinates for a circle, which require `cx` and `cy` coordinates.*

---

### Enter, Update, and Exit

![D3 Venn](https://s3.amazonaws.com/assets-paperboy/adunkman/techtime-understanding-d3-selection-operations-venn.png "D3 Venn")

 * **Enter**: used to add / create objects with bounded data
 * **Update**: used to update existing objects with bounded data
 * **Exit**: used to update existing objects and remove objects when there is no element to match to data

Let's go back to [work.html](work.html), and try binding data to our cicle using these methods.

```javascript
// Define your data
var dataset = [10];

// Select the cirlce, and update it with data
d3.selectAll("circle")
  .data(dataset);
```

Select the circle and look at the data property to confirm it's updated. That's the update method. Simply select your objects and use the `data()` function to update them with data. To note, you only want to do this when there's a 1 to 1 relationship between your objects and your data _already_.

Now, define the circle's radius based on its bound data:

```javascript
d3.selectAll("circle").attr("r", function(d) { return d; });
```

 * What's this function(d)?

---

Now, let's use a larger dataset, and try the enter method.

```javascript
// Define new dataset
var dataset = [10, 20, 30];

//Select the circle, use the enter() function and append circles to match the data
d3.select("svg").selectAll("circle")
  .data(dataset)
  .enter().append("circle");
```

 * Where are the circles?

```javascript
d3.selectAll("circle")
  .attr("r", function(d) { return d*2; })
  .attr("cx", function(d) { return d*10; } )
  .attr("cy", function(d) { return d*10; } )
  .attr("fill", function(d) { if (d == 10) { return "red"; }
                        else if (d == 20) { return "blue"; }
                        else if (d == 30) { return "green"; }
    })
  .style("fill-opacity", .7)
  .style("stroke-width",".2em")
  .style("stroke",function(d) { if (d == 10) { return "red"; }
                        else if (d == 20) { return "blue"; }
                        else if (d == 30) { return "green"; }
    });
```

 * What's `cx` and `cy`?
 * What's `r`?

---

Ok, so now we know how to update and enter new data. Let's go over `exit()`.

Say we want to update our circles with a smaller dataset, and remove circles that don't match. Here is where we'll use the exit() function.

```javascript
// Define new dataset
var newdataset = [20,30]

//Select the circle, use the enter() function and append circles to match the data
d3.select("svg").selectAll("circle")
  .data(newdataset)
  .exit().remove();
```

What happened? Is that right?

In D3, you need to say what you want. We updated the data, removed the circle, now we need to set the attributes of those circles based on the new data.

Simply re-enter:

```javascript
d3.selectAll("circle")
  .attr("r", function(d) { return d*2; })
  .attr("cx", function(d) { return d*10; } )
  .attr("cy", function(d) { return d*10; } )
  .attr("fill", function(d) { if (d == 10) { return "red"; }
                        else if (d == 20) { return "blue"; }
                        else if (d == 30) { return "green"; }
    })
  .style("fill-opacity", .7)
  .style("stroke-width",".2em")
  .style("stroke",function(d) { if (d == 10) { return "red"; }
                        else if (d == 20) { return "blue"; }
                        else if (d == 30) { return "green"; }
    });
```

That's the enter, update, and exit approach to binding data in D3.


## Review

Now that we got a good sense of selections, SVGs and how to bind data, let's go back to our first visualization and answer a few questions:

 * What's that `colorScale` thing?
 * What's `i`?
