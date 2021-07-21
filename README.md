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

    - [Existing and Design Features](#existing-and-design-features "Goto existing & design features")
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

# Deployment

This project was committed to Git and push to GitHub using the workspace terminal.

## Deployment on Heroku

To deploy this program to Heroku, the developer followed these steps:

1. Type Pip3 freeze > requirements.txt in the workspace terminal
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
9. Connect to GitHub
10. Search and Link up our GitHub repository code to Heroku app
11. Scroll down to manual deploy
12. Click to Deploy branch
13. After python, all requirements.txt file, and node.js installed, we can see the 'App was successfully deployed' message
14. Below there is a button to take us to the deployed link