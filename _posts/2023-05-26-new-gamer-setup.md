---
title: New Gamer Setup
date: 2023-05-26
categories: life update
---

**Disclosure**: I am not a gamer.

---

I recently purchased some new furniture for my "developer setup". Not that I really had one to begin with, but life events led to me considering buying a few things as an "investment" to my "developer career". Lucky for me I wasn't that interested in jumping down a rabbit hole into office ergonomics, best deals, etc. so I got the goods pretty quickly *(took me 2 days to order both items)*. My strategy: I just picked the cheapest thing on Amazon and ran with it *(obviously had to look at some 3rd party reviews first)*.

For a total of ~$280, I snagged myself:
1. GTPlayer Gaming chair
2. FEBIZO Standing desk

### Some pics for the visuals:

<figure >
    <div class="light" style="position: relative">
        <img src="{{ '/images/light_setup.JPG' | absolute_url }}" alt="" width="300px">
        <figcaption>Setup in the light</figcaption>

        <div class="dark" style="position: absolute; top:0; left:0;">
            <img src="{{ '/images/dark_setup.JPG' | absolute_url }}" alt="" width="300px">
            <figcaption>Setup in the dark</figcaption>
        </div>
    </div>
    <button onclick="toggleVisibility()">Click to see other mode!</button>
</figure>

<figure style="clear: left;">
  <img src="{{ '/images/gaming_chair.JPG' | absolute_url }}" alt="" width="300px">
  <figcaption>Gaming chair</figcaption>
</figure>

<script>

    window.addEventListener("load", toggleVisibility)

    var lightVis = "visible", darkVis = "hidden";

    function toggleVisibility(){
        let light = document.getElementsByClassName("light");
        let dark = document.getElementsByClassName("dark");

        light[0].style.visibility = lightVis;

        dark[0].style.visibility = darkVis;

        [lightVis, darkVis] = [darkVis, lightVis];
    }

</script>



---

### Something always has to happen.

As life goes, things weren't that perfect. Mainly with the standing desk. The assembly for the gaming chair went smoothly(ish), but for the table I completely screwed up *(pun intended)* by tighting the screw way too much. So the rotator connecting the motorized leg and unmotorized leg is stuck, and it's severly misaligned that it's tearing the plastic housing. Here's a picture of my failure:

<figure class="align-center">
    <img src="{{ '/images/fail_setup.JPG' | absolute_url }}" alt="" width="300px">
    <figcaption>Das ist gar nicht gut.</figcaption>
</figure>

The screw is stuck and it can't get out! The damage in the image looks really nasty, but thankfully it's not enough to render the entire table useless. The motor can still rotate around the center axis, albeit I don't really know how stable the table is now. It seems okay as I'm using it, and it has some support from super sticky duct tape. **But yea, lesson of the day - don't screw around.**