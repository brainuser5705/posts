---
layout: post
title:  "Using Jekyll for Blog Posts"
date:   2023-05-17 14:20:13 -0400
categories: jekyll update
---

Jekyll is such a wonderful frontend framework. From my experience developing the current verison of my personal website, a Jekyll site is simple to create, extensible with plugins, and customizable. And Jekyll's integration with Github Pages only makes it easier to set up a site and deploy. It's the best tool for anyone who wants a quick and easy (and lazy) way of setting up a static website for free.

I've recently realized is that I could use Jekyll for my blog page as well, but also with a Jekyll Theme. If you've seen my [blog page](https://ashleyliew.com/blog) before, it was barebones markdown with the default Github Pages theme. I decided to switch over to Jekyll and use an opensource theme for a fresh new frontend, along with some cool interactivity provided by the theme such as tag filtering. I am currently using [**So Simple Theme**](https://github.com/mmistakes/so-simple-theme) by Michael Rose ([mmistakes](https://github.com/mmistakes) on Github).

## Setting Up

*Here is the list of steps I took to set up my new blog page. Note that this is I did as a first time user of Jekyll Themes; there is a probably a more "official" way of doing it.*

1. Follow these [Quickstart instructions](https://jekyllrb.com/docs/) to create a new directory for a Jekyll site.
2. Fork the So Simple Theme Github repository and follow the [README.md](https://github.com/mmistakes/so-simple-theme#remove-the-unnecessary) to remove all the unnecessary files.
3. Since I am hosting with Github Pages, I will need to edit the `Gemfile` and `_config.yml`. Follow these [instructions](https://github.com/mmistakes/so-simple-theme#github-pages-method) on the README. Remember to comment out or remove any default configurations from creation process.
4. After that, deploy with Github Pages and the site should be good to go!

## Next Steps

The next steps for me is to read up on the features provided by the So Simple Theme and customize the source code to make it more my "brand".