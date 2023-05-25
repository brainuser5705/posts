---
layout: post
title:  "Becoming a Linux User"
date:   2023-05-17 17:08
categories: linux update
---

An ongoing series of updates as I trek along the path of Linux mastery (*spoilers: there is no end*).

### (4.17.23) Setting up basic dev environment

#### Python
- `sudo apt install python3`
- Apt also had a `python` package, but from a little internet browsing, it looks like that is only for users with the previous Python2 installed and need a symlink to Python3.

#### VS Code
- originally using flatpak, then switched over to installing with a Debian package
- https://code.visualstudio.com/docs/setup/linux

### Java
- why was this a whole ordeal
- originally installed openjdk with apt `sudo apt install default-jdk` but VS Code was having issues recognizing that I had a JDK installed
- a whole bunch of searching and terminal work trying to figure out how to install the Oracle JDK via a tar file
- found a [video](https://www.youtube.com/watch?v=snN--wBu3xw&ab_channel=OSTechHelp) where everything worked (`java` is a recognized command, VS Code recognizes it)
    - installed in `/usr/local/lib`
    - put `JAVA_HOME` and new `PATH` in `.profile`
- useful commands learned throughout the process: 
    - `apt list [--installed] | grep jdk`
    - `tar zxvf <archive>`

### NodeJS and npm
- installing the [nvm package manager](https://github.com/nvm-sh/nvm#usage)

I definitely need to learn more about Linux package managers and installation methods.

---

### (4.21.23) Deep Cleansing and Installing Linux

#### No more crusty musty laptop
- [official cleaning guide](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-t-series-laptops/thinkpad-t480-type-20l5-20l6/20l5/solutions/ht035676-keeping-your-computer-clean-notebooks-all-in-one-desktops-tiny-in-one-and-monitors)
- [removing the keyboard](https://www.youtube.com/watch?v=0v-WO9VANyE) - pull on the black clip
- [removing the touchpad](https://www.youtube.com/watch?v=E51a_fRZG7Y&ab_channel=ChezDoesStuff)
- I was trying to clean the gunk off the crevices in the touchpad, but the pin I was using was too wide so the skin of the touchpad has some tears in it now.
- I also might have messed up the battery when I was unplugging it, but I'm not entirely sure if this was the cause. The battery can still hold charge, but the laptop sometimes have trouble starting up (it boots up then turns off a few seconds afterwards)

#### Checking some specs
- [video](https://www.youtube.com/watch?v=3hFmIVqpG6s&list=LL&index=2)
- thunderbolt firmware: 20.0 
- install lenvono vantage to install some new updates

#### Installing Linux
what a unexpected pain in the ass this was

My installation method was Live USB disk creation where all I need to do is flash the ISO onto a flashdrive, stick it in the Thinkpad, boot up and go through the installation wizard. Easy and done right? No.

The two flashdrives I brought from home were having issues. I don't think they were acting up beforehand; I was using the recommended USB flasher software Balena but it somehow destroyed the partitions on the drives and so I kept getting errors like "System can't find drive, disk is not allocated to drive, blah, blah". After a few hours of scouring the Internet, I finally found a [video](https://www.youtube.com/watch?v=s80HI2krsNA) that fixed the issue.


Unrelated note: How to change sudo password
```
sudo passwd brainuser5705
```

---

### (4.21.23) Purchased a Thinkpad Laptop & Specs

TLDR; Bought a Thinkpad off Ebay for ~$200 (proud to say that it was my first bid!) since there's seems to be consensus that old Thinkpads and Dells are the cheapest laptops on the market that has the hardware to support Linux.

Before starting this experiement, my one and only machine was a HP Spectre x360. I don't know the specific model by heart, but it's safe to say that it was definitely built for Windows. This Linux experiment isn't my first; around two summers ago I decided to try Linux out and after some major close-calls (i.e. breaking everything), I had dual-boot Ubuntu and Windows 10 on the Spectre. But unfortunately, there were a lot of issues. A lot of the hardware didn't have drivers available on Ubuntu. Camera, mic, and speakers were a no go. Coupled that with my lack of Linux knowledge, I had no idea what I was doing and I ended up switching back to Windows-only. A few more attempts were made to enter the gates of Linux heaven but no luck.

**But now, I have a THINKPAD.** I was in the market for a new laptop mainly because I was getting bored of the Windows OS and Spectre (gotta hate first-world problems). I wanted to give Linux another shot and given my past experience, I was in the market for a Linux-specific laptop. I initially had my wallet set on System76 but got sucked into the rabbit hole of consumer electronics and Reddit so I spent a good two days just browsing the internet for what laptop I should get. It was either a $1000+ brand new laptop with the latest specs or a cheap (but still popping) Thinkpad. The key questions were "what will I do with the laptop", "can I upgrade it", and "is it worth the money".

Long story short and skipping over a lot of details, I won a bid on Ebay and paid ~$200 for Thinkpad T480 with a 8th generation i7-8650U Intel Core CPU, 8GB RAM, and 256GB SSD. Despite the bad specs, it's a pretty darn good price and I can always upgrade the laptop if I need to.

<figure style="width: 400px" class="align-center">
  <img src="{{ '/images/linux_specs.png' | absolute_url }}" alt="">
  <figcaption>Screenshot of system information</figcaption>
</figure>

---