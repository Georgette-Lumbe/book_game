# BOOK GAME

<img src='docs/screenshots/am_i_responsive.PNG'>

[View the live project here](https://book-choicegame.herokuapp.com/)

# Table of Content

1. [Introduction](#introduction "Goto introduction")

2. [UX](#ux "Goto ux")

    - [Ideal User Demographic](#ideal-user-demographic "Goto ideal user demographic")
    - [User Stories](#user-stories "Goto user stories")

3. [Features](#features "Goto features")

    - [Existing Features](#existing-features "Goto existing features")
    - [Features to Implement in the future](#features-to-implement-in-the-future "Goto features to implement in the future")
    
4. [Testing](#testing "Goto testing")

    - [Testing file](https://github.com/Georgette-Lumbe/book_game/blob/main/TESTING.md)

5. [Issues and Unfixed bugs](#issues-and-unfixed-bugs "Goto issues and unfixed bugs")

6. [Technologies used](#technologies-used "Goto technologies used")
 
    - [Main Languages Used](#main-languages-used "Goto main languages used")
    - [Libraries, Frameworks and Programs Used](#libraries-frameworks-and-programs-used "Goto libraries, frameworks and programs used")
    
7. [Deployment](#deployment "Goto deployment")

    - [Deployment on Heroku](#deployment-on-heroku "Goto deployment on heroku")

8. [Credits](#credits "Goto credits")

    - [Content](#content "Goto content")
    - [Media](#media "Goto media")
    - [code](#code "code")

9. [Acknowledgements](#acknowledgements "Goto acknowledgements")

---

# Introduction

Book Game is an interactive game about making a good choice of children's books for a school presentation. It allows the user to input some data, follow the text-based instructions and questions displayed at the terminal. If the instructions are followed correctly, they will get their desired choice printed to the terminal. The user have to be carreful because there are also some books which are not appropriate for children.

This is the third of five Milestone projects that the developer is required to complete as part of their full web development course at the Code Institute. The main requirements were to create an App using mainly *Python Programming Language*.

# UX

## Ideal User Demographic

* The ideal user of the game: Everyone who wants to have a good presentation book for a child

## User Stories

User Goals:

* I would like to run the program whenever I want
* I would like to choose the type of book that I want
* I would like to choose the book I want
* I would like to see a feedback after my choice
* I would like to make another choice easily
* I would like to see a good bye message

# Features

## Existing Features

1. Gif
* On top of the program, there is an animation gif, which brings an attractiveness to the game.

    <img src='docs/screenshots/gif.PNG'>

2. Run Program Button
* At the top of the terminal, there is a green button which allows the user to run the program from the start whenever he wants.

    <img src='docs/screenshots/run_button.PNG'> 

3. Terminal Area
* This section allows the user to start the program, follow the instructions and enter data.
    - Logo & Welcome Message 

    <img src=''>

    - Questions asked

    <img src=''>  <img src=''>  <img src=''>
    <img src=''>  <img src=''>
    
    - User responds

    <img src=''>  <img src=''>  <img src=''>
    <img src=''>  <img src=''>

    - Feedback to user

    <img src=''>

    <img src=''> 

    - Good Bye message

    <img src=''>

4. Program Structure
* In the Planning Stage of the project, the developer used a Flow Chart to conceptualise and bring the Book Game idea in life. Flow Chart was created in [Diagram Software and Flowchart Maker](https://www.diagrams.net/).

    <img src=''>

## Features to implement in the future

* More questions, create more situations to make the game more fun while keeping the basic objective of choosing a book.

# Testing

Testing information can be found in a separate [testing file](https://github.com/Georgette-Lumbe/book_game/blob/main/TESTING.md).

[Back to top](#introduction "Goto introduction")

# Issues and Unfixed bugs

1. Time counter: 

The developer wanted the 5 seconds for the opening of the game to count on the terminal so that the user could see the time count. 
On the Gitpod terminal, the time counts as the developer wanted but on the heroku terminal the counter doesn't show, there is just a timeout for 5 seconds.

2. Logo:

The developer has encountered a problem with the Book Game logo which is styled from Ascii Art Generator. When copying each step (with more than 79 characters on a line) of the logo via the generator, there was a problem as the Gitpod workspace does not accept more than 79 characters on a line. The developer had to remove some of the last characters from the logo so that the workspace would look good and be easy to follow.

3. Text:

Testing the program on Gitpod, the text appears perfectly fine. But once on the deployed site, some syllables are not well represented.

4. Helper functions:

The user could write something else starting with the suggested data, e.g. if the user was asked to enter yes or no, the user could just enter yesjfkf and the code would work. Why would this happen? Just because it started with yes. 
To avoid this, the developer created two helper functions (validate_integer & book_choice), which would return 'Invalid data' whenever the user entered something that was not suggested even if he enters nothing of the sort, it will be considered as invalid data.

5. Summary Option:

At the beginning, the developer had put an additional option, that of proposing to the user a summary in case they had chosen the right book. But this option was removed when the developer used the Helper functions. 
Indeed, this option was linked to the book_choice function, and would only have had an effect if the user had chosen the right answer. The developer preferred to remove this option to avoid complicating the code.

# Technologies used

## Main Languages Used

1. [Python](https://fr.wikipedia.org/wiki/Python_(langage))
2. [HTML5](https://fr.wikipedia.org/wiki/HTML5)
3. [CSS3](https://en.wikipedia.org/wiki/CSS)

### Libraries, Frameworks and Programs Used

1. [Diagram Software and Flowchart Maker](https://www.diagrams.net/) was used to create a flowchart. 
2. [Git](https://git-scm.com/) was used for version control by using the GitPod terminal to commit to Git and push to GitHub.
2. [GitHub](https://github.com/) was used to store the project after pushing.
3. [Am I Responsive?](http://ami.responsivedesign.is/#) was used to view the responsive design throughout the process and to generate image mock-ups for use.
4. [Heroku](https://id.heroku.com/login) was used to deploy the program
5. [Favicon](https://favicon.io/favicon-converter/) was used to convert an image form [Unsplash](https://unsplash.com/) to a favicon for the Book Game.
6. [Giphy](https://giphy.com/) was used to import the gif
7. [Pep8](http://pep8online.com/) was used to test and validate the code.
8. [Youtube](https://www.youtube.com/) was used for further clarification.
9. [Text to Ascii Art Generator](http://patorjk.com/software/taag/#p=display&f=Bloody&t=See%20you) was used to generate a styling logo name and a good bye message.

[Back to top](#introduction "Goto introduction")

# Deployment

This project was committed to Git and push to GitHub using the workspace terminal.

## Deployment on Heroku

To deploy this program to Heroku, the developer followed these steps:

1. Create requirements.txt by typing Pip3 freeze > requirements.txt in the workspace terminal
2. Log into [Heroku]()
3. Create new APP 
4. Rename the APP
5. Choose the region
6. Select Settings from the menu at the top
7. Go to Config Vars 
8. Click to Reveal Config Vars if you have sensitive information to put in
9. Go to Buildpack
10. Click to add builpack and add in order: Python the node.js
11. Select Deploy from the menu at the top
12. Go to deployment method and then click to GitHub 
13. Connect to [GitHub]()
14. Search and Link up our GitHub repository code to Heroku app
15. Scroll down to manual deploy
16. Click to Deploy branch
17. After python, all requirements.txt file, and node.js installed, we can see the 'App was successfully deployed' message
18. Below there is a button to take us to the [deployed link](https://book-choicegame.herokuapp.com/)

    <img src='docs/screenshots/heroku_deploy.PNG'>

# Credits

## Content 

* The developer has consulted some websites and tutorials for better understanding :
    - [Termcolor](https://pypi.org/project/termcolor/)
    - [W3CSchools](https://www.w3schools.com/)
    - [Tech Touhid](https://www.youtube.com/watch?v=zUf1BM1l8MQ), How to make Awesome ASCII Art with Pyfiglet in Python Programming.
    - [HowCode](https://www.youtube.com/watch?v=5uVXbb1ymVs), Simple countdown.

## Media
* The developer used a gif to make the site more attractive, the gif was taken from [Giphy](https://giphy.com/).

## Code 

* The developer has consulted some websites and tutorials in order to better understand and use the code for this site. Beloow are the sites and tutorials used:

    * [Stack Overflow](https://stackoverflow.com/)
    * [W3CSchools](https://www.w3schools.com/)

# Acknowledgements

* I would like to thank my mentor, Seun and my tutor Kasia for their helpfulness, constructive advice, feedback and guidance.
* I would like to thank my family, my friend Esther Booto, and my boyfriend Jimmy for all the support during this project.
* I would like to thank my colleagues of Code Institute and Slack Community for sharing their posts and experience.

[Back to top](#introduction "Goto introduction")