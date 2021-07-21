# BOOK GAME

[View the live project here](https://book-choicegame.herokuapp.com/)

# Table of Content

1. [Introduction](#introduction "Goto introduction")

2. [UX](#ux "Goto ux")

    - [Ideal User Demographic](#ideal-user-demographic "Goto ideal user demographic")
    - [User Stories](#user-stories "Goto user stories")
    - [Development Planes](#development-planes "Goto development planes")
    - [Design](#design "Goto design")

3. [Features](#features "Goto features")

    - [Existing Features](#existing-features "Goto existing features")
    - [Features to Implement in the future](#features-to-implement-in-the-future "Goto features to implement in the future")
    
4. [Testing](#testing "Goto testing")

    - [Manual Testing](#)
    - [Validator Testing](#)

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

# Features

## Existing Features

1. Run Program Button

    * At the top of the terminal, there is a green button which allows the user to run the program from the start whenever he wants
    <img src=''>

2. Terminal Area

    * This section allows the user to start the program, follow the instructions and enter data.
    <img src=''>

3. Program Structure

    * In the Planning Stage of the project, the developer used a Flow Chart to conceptualise and bring the Book Game idea in life. Flow Chart was created in []()
    <img src=''>

## Features to implement in the future

# Testing

# Issues and Unfixed bugs

# Technologies used

## Main Languages Used

1. [Python]()
2. [HTML5](https://fr.wikipedia.org/wiki/HTML5)
3. [CSS3](https://en.wikipedia.org/wiki/CSS)

### Libraries, Frameworks and Programs Used


# Deployment

This project was committed to Git and push to GitHub using the workspace terminal.

## Deployment on Heroku

To deploy this program to Heroku, the developer followed these steps:

1. Create requirements.txt by typing Pip3 freeze > requirements.txt in the workspace terminal
2. Log into [Heroku]()
3. Create new APP 
  - Rename the APP
  - Choose the region
4. Select Settings from the menu at the top
5. Go to Config Vars 
  - Click to Reveal Config Vars if you have sensitive information to put in
6. Go to Buildpack
  - Click to add builpack and add in order: Python the node.js
7. Select Deploy from the menu at the top
8. Go to deployment method and then click to GitHub 
9. Connect to [GitHub]()
10. Search and Link up our GitHub repository code to Heroku app
11. Scroll down to manual deploy
12. Click to Deploy branch
13. After python, all requirements.txt file, and node.js installed, we can see the 'App was successfully deployed' message
14. Below there is a button to take us to the [deployed link](https://book-choicegame.herokuapp.com/)