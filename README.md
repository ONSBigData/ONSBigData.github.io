
# [ONS Big Data Team Github.io website][7]

This website was built using [Jekyll][1] & [Minimal Mistakes][2].

* **Jekyll:** Jekyll is a simple and blog-aware static site generator built in Ruby. It takes a template directory containing raw text files in various formats, and spits out a complete, ready-to-publish static website. Jekyll also happens to be the engine behind GitHub Pages, which means you can use Jekyll to host your project’s page, blog, or website from GitHub’s servers for free.

* **Minimal Mistakes:** A flexible two-column Jekyll theme, suited for personal sites, blogs, and portfolios hosted on GitHub

## Requirements to run this website locally

#### 1. Install Ruby
Ruby should come pre-installed on all OSX computers. You can check if Ruby is installed by running ```ruby -v```. It should return with Ruby version 2.0.0 or higher.

The version I am currently using is:
``` bash
ruby 2.4.1p111 (2017-03-22 revision 58053) [x86_64-darwin16]
```
If you’re running a lower version, you can update:
``` bash
gem install ruby
```

#### 2. Install Bundler
Bundler is a package manager that will aid you in installing all the Jekyll dependencies. To install it simply run:

``` bash
gem install bundler
```
Running ```bundle  -v``` in the terminal tells me the version I am currently using is:
``` bash
Bundler version 1.15.4
```

#### 3. Clone this repo
Move with the terminal to the folder location where you want to place this website.
Now you can close this repo using:
``` bash
git clone https://github.com/ONSBigData/ONSBigData.github.io.git
```
Before proceeding any further, make sure to move inside the website folder, via
``` bash
cd ONSBigData.github.io.git
```

Type ```ls``` and you should see more or less the following files and folders:
```
Gemfile        Rakefile          _layouts        _site       scripts
Gemfile.lock   config.yml        _pages          assets
LICENSE.txt    _data             _posts          banner.js
README.md      _includes         _sass           package.json
```

#### 4. Run bundle to install everything else

Run this command in the directory that contains the Gemfile:
``` bash
bundle install
```
![][3]
*(Source: https://mmistakes.github.io/minimal-mistakes/docs/installation/)*

#### 6. Test that everything works!
At this point, all the setup is complete. Run the following code:
``` bash
bundle exec jekyll serve
```
This command runs a “watch” on the entire server. Changes made to any files (except the configuration file!) will be compiled into static HTML.

Now go to the url ```http://localhost:4000```.

Your are ready to modify the website and see the changes reflected immediately when refreshing this webpage.

When you are happy with the changes commit your changes and push them to GitHub.


## How to modify this website
For a more conplete guide on how the website is structured refer to [the theme website][2]. This section covers the basics you might want to do to modify this website.

### The About Page
To modify the content of the publication page you can simply edit the markdown file ```_pages/home.md```

### The Publication Page

To modify the content of the publication page you can simply edit the markdown file ```_pages/publications.md```
If you added a new publication which has an associated GitHub repo, don't forget to add a link to it using the GitHub icon:
``` HTML
<a href="insert-your-URL-to-the-github-repo-here">
  <i class="fa fa-fw fa-github" aria-hidden="true"></i>
</a>
```
### Blog

#### New post from scratch
Blog posts can be written as markdown files. This allow you to easily insert charts, code snippets in it, etc.
To add a new blog post you need to do 3 things:

1. Name your ```.md``` file using the following convention:

  ```YYYY-MM-DD-your-post-name-here.md```

  where ```YEAR``` is a four-digit number, ```MONTH``` and ```DAY``` are both two-digit numbers

2. Put your ```YYYY-MM-DD-your-post-name-here.md``` file in the  ```_posts``` folder

3. Add, if not already there, the [Front Matter][4] to your file. It should indicate at least the title of the post and an excerpt.

```
---
title: 'Happy campers: Using machine learning to identify caravans in Zoopla data'
excerpt: 'Using machine learning to extract holiday homes in Zoopla data'
---
```

> ProTip: Remember to write unique excerpt descriptions for each post for improved SEO and archive listings.


#### If the post already exist. How do I republish it here?
If a post already exists, is posted somewhere else and you just want to add it, only thing you need to do is to convert that post to a markdown file.

To do that you can use the Python script named ```html_to_md_post.py``` in the ```scripts/``` folder.

Navigate with the terminal to the ```scripts/``` folder:
``` bash
cd scripts/
```

then run the script with the following required arguments:
``` Python
python3 html_to_md_post.py arg1 arg2 arg3
```
where:

* ```arg1``` is the url to the blog post you want to convert
* ```arg2``` is the title of the post (which will be placed in the Front Matter)
* ```arg3``` is the name wich will be used to save the new ```.md``` file in the ```_posts``` folder

As an example:
``` Python
python3 html_to_md_post.py "https://digitalblog.ons.gov.uk/2017/06/21/happy-campers-using-machine-learning-to-identify-caravans-in-zoopla-data/" "Happy campers: Using machine learning to identify caravans in Zoopla data" "2017-06-21-happy-campers.md"
```
After running this script a new ```.md``` file will be generated in the ```_posts``` folder. You can open the new generated file and check that all links and markdown titles have been generated correctly.
The script uses the [FUCK YEAH MARKDOWN][6] API service to convert the HTML URL in a markdown file.


Finally do step [2.][5] and [3.][5] (is not compulsory, but the excerpt is not generated automatically so you need to add it manually) as before for the post from scratch.

[1]: https://jekyllrb.com/
[2]: https://mmistakes.github.io/minimal-mistakes/
[3]: https://mmistakes.github.io/minimal-mistakes/assets/images/mm-bundle-install.gif
[4]: https://jekyllrb.com/docs/frontmatter/
[5]: #New-post-from-scratch
[6]: http://fuckyeahmarkdown.com/
[7]: https://onsbigdata.github.io/

## LICENSE

Released under the [MIT License](LICENSE.txt).
