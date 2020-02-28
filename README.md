# RedditWebapp
A webapp that extracts data from Reddit Api with the help of a wrapper class called PRAW.

## Frameworks Used

### Functionality

- Praw
- Django

### Design
- Bootstrap
- Jquery
- Datatables

## Setup

- Install PRAW
  - $ pip install praw
- And then you can just run it on your local server using
  - $ python manage.py runserver

## Tests

- To be able to run the tests, you will need to change the selenium chrome driver path in tests.py and change it to your driver location.
- You would also need to install selenium. The following command line should work fine, but you can check the documentation for selenium as well.
  - $ pip install selenium

## How everything works

This application uses the PRAW library built for extracting data from reddit. It creates an instance of reddit and then I can search through that instance for subreddits. The subreddit method returns a listgenerator which is passed in to the view file to display all the various kinds of information I felt were reasonable.

In my view file, I used the datatables for managing my table of data for all the possible values as it helped maintain and organise all the information on the website.

## Hours spent

Even though it took me more than a week to do all of this, I gave this project around 2-3 days as I was studying for midterms for the rest of the time (It was one of the busiest weeks of this semester lol). Here is the timeline of the project development.

#### Planning and initial development (7-8 hours)
- I took a lot of time initially to figure out which technology would be best for this situation. I started with ruby on rails but then as I read more and more about this, I came to know more about the PRAW library and I was able to achieve expected results within a span of 30 minutes.

#### Presenting python as a web-app (Django) (7-8 hours)
- I read about the various possible technologies I could use to achieve this task and after the email response from Ryan(if I may), I decided to learn and use django from scratch. This, for obvious reasons, took time. I had a lot of difficulty initially, but after working on this project, I feel like I can work on other projects that involve Django with ease. It got better once I understood the flow of things.

#### Making my website look cool (3-4 hours)

- I know it doesn't look as pretty as you would expect, but it looks a lot better than what I had when I started coding it out. I used bootstrap for design and as less of CSS and styling as I could because even though I know and want to use custom stylesheets, I think I should stick with existing frameworks as they provide cross-browser stability and are generally reliant and provide much more readability.

#### Writing tests (1-2 hours)

- I have been writing tests in ruby on rails so I knew about various types of testing, but since I didn't have much time on hand. I figured I could just stick with selenium tests. Getting the webdriver to work was a challenge but somehow I got it working and tested out the basic things.

#### Handling exceptions (1-2 hours)
- There were a lot of exceptions that happened when provided with an invalid subreddit and I read about most of them and in the end just figured I would stick with a general exception handler.

#### Deployment to heroku (1-2 hours)
- It was confusing at first, but heroku is pretty intuitive and I was able to follow tutorials and set it up in no time. You can check it out [here](https://redditwebapp.herokuapp.com/).

## Overall Experience

This was a great learning experience for me since I now know Django! I think this was a good exercise and it is really most similar to what real life problems are in my opinion and I thank you for the oppurtunity!

## TLDR
 Here is the link for the webapp: <https://redditwebapp.herokuapp.com/>
