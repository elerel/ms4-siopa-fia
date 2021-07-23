<div align="center">
<img src="https://res.cloudinary.com/elerel/image/upload/v1627032789/amiresponsive2_yak1an.png" alt="multi-device site display image"/>
<br>
<h1>Siopa Fia</h1>
</div>

# Project Overview

Siopa Fia is my 4th and final milestone project as part of the Code Institute's Software Development Diploma, intending to be full-stack site based on a fictional online Irish eco/sustainable clothing store. All products in the store are made locally, ethically sourced and are made from 100% organic materials.

The idea of siopaFIA came to mind when I first visited my cousin’s new business venture specialising in ethical fashion (BasicJuju.com) which is a subject I always felt passionate about. My five year old daughter was also particularly impressed that I would name my next project after her, which resulted it being named “Siopa Fia” or Fia’s Shop.

The logic behind siopaFIA was to create an e-commerce fashion store that promotes sustainable fashion, for someone who likes to wear good quality clothing that lasts while supporting local business.


Primary functions of Siopa Fia:
- Product purchase functionality
- User authentication and authorisation for site subscribers and site admin
- Customer profile page which will contain purchase history and store customer details
- All CRUD functionalities


---

# Table of Contents

**<details><summary>[User Experience (UX)](#user-experience-ux)</summary>**

- [User Stories](#user-stories)
- [Strategy](#strategy)
- [Scope](#scope)
  - [Existing Features](#existing-features)
  - [Future Features to Implement](#future-features-to-implement)
- [Structure](#structure)
- [Database](#database)
- [Database Model Schema](#database-model-schema)
- [Skeleton](#skeleton)
- [Wireframes](#wireframes)
- [Surface](#surface)
  - [Colours](#colours)
  - [Typography](#typography)
  - [Imagery](#imagery)

</details>

**<details><summary>[Technologies Used](#technologies-used)</summary>**

- [Languages](#languages)
- [Integration](#integration)
- [Dependencies](#dependencies)
- [Tools](#tools)
- [IDE Extensions](#ide-extensions)
- [Code Validity](#code-validity)


</details>

**<details><summary>[Bugs/Issues](#bugs)</summary>**

- [Project barriers and solutions](#project-barriers-and-solutions)
- [Known Issues](#known-issues)

</details>

**<details><summary>[Workflow](#workflow)</summary>**

- [Version Control](#version-control)
- [Development Environment](#development-environment)

</details>

**<details><summary>[Deployment](#deployment)</summary>**
</details>

**<details><summary>[Testing](#testing)</summary>**
</details>

**<details><summary>[Credits](#credits)</summary>**

- [Resources](#resources)
- [Media](#media)
- [Content](#content)
- [Code Snippets](#code-snippets)
- [Acknowledgments](#acknowledgments)

</details>

# User Experience (UX)

## [Strategy](#strategy)

### Business Logic

- To make the site easy to navigate and create a positive user experience for the shopper
- To be able to add add, edit or delete products available
- To manage a blog circling the topics of discussion around ethical fashion, promoting awareness to users
- To encourage the user to understand the site owner's mission behind siopaFIA
- To support local fashion designers and promote ethical fashion
- To promote awareness of the impact of the fast-fashion industry and help the sustainable fashion grow or even take its place

### User Stories

|      As a/an...      |                         I want the ability to...                         |                        So that I can...                       |
|:--------------------:|:------------------------------------------------------------------------:|:-------------------------------------------------------------:|
|                      |                                                                          |                                                               |
|          ---         |                                    ---                                   |                              ---                              |
| First time user      | easily navigate the site;                                                | find what I am looking for quickly                            |
| First time user      | view the site on all screen sizes;                                       | view the store across all devices                             |
| First time user      | view a list of products                                                  | view items available to buy                                   |
| First time user      | view individual product details                                          | see exactly what I am buying                                  |
| First time user      | read about the company description                                       | gain trust in the company and support local business          |
| First time user      | search for categories of products                                        | find the best-rated/priced products in a specific category    |
| First time user      | search for a product by name or category                                 | easily find the exact product Im looking for                  |
| First time user      | view items selected in the shopping bag                                  | easily see how much I am spending                             |
| First time user      | adjust or remove items from the shopping bag                             | easily change my order in case I change my mind               |
| First time user      | access contact details;                                                  | get in touch with any questions                               |
| First time user      | access social media of the company;                                      | join social media forums for news and updates                 |
| First time user      | register for a user profile account by choosing a username and password; | store my own personal details and purchase history            |
| First time user      | make purchases as a guest user                                           | do not have to set up an account if I dont want to            |              
|          ---         |                                    ---                                   |                              ---                              |
| Registered user      | log in and log out of my profile account;                                | Safeguard my information whilst not active on the site        |
| Registered user      | update my details                                                        | update address and other details in case they change          |
| Registered user      | store my address for later use;                                          | avoid having to retype it every time I make a purchase        |
| Registered user      | store my purchase history;                                               | access my previous purchase history                           |
| Registered user      | store my choices in checkout;                                            | go back to the site in case I wish to add more options        |
| Registered user      | Make secure payments                                                     | ensure my payments are securely handled                       |
| Registered user      | Receive email confirmation of payment                                    | confirm that my payment was made |
|          ---         |                                    ---                                   |                              ---                              |
| Site Owner           | add new items and category listings;                                     | continuously update the site with new items or specials       |
| Site Owner           | update items                                                             | change price or product criteria                              |
| Site Owner           | delete items                                                             | delete items that are no longer for sale                      |


 ---


## [Scope](#scope)

### [Existing Features](#existing-features):

### [Features Left to Implement](#features-left-to-implement):

## [Structure](structure)

### Database 
- As suggested in throughout the walkthrough project, SQLlite (that comes pre-installed with Django) was used for development.
- PostgreSQL was used when deployed through Heroku (as an additional add-on).

### Database Model Schema
- The Data Model below was created using [drawSQL](https://drawsql.app/):

![image](https://res.cloudinary.com/elerel/image/upload/v1626455309/drawSQL-export-2021-07-16_18_07_zniam0.png)

---

### Wireframes

#### Desktop View:

- Home Page:

![image](https://res.cloudinary.com/elerel/image/upload/v1626507220/desktop-home-new_d6svbt.png)

- All Products on offer through siopaFIA:

![image](https://res.cloudinary.com/elerel/image/upload/v1626507354/desktop-all-products_zqzyz9.png)

- Product Detail Page:

![image](https://res.cloudinary.com/elerel/image/upload/v1626507301/desktop-product-detail_zgdflo.png)

- Shopping Bag Page:

![image](https://res.cloudinary.com/elerel/image/upload/v1626548287/desktop-shoppingbag_qxjfez.png)

- Checkout Page:

![image](https://res.cloudinary.com/elerel/image/upload/v1626548341/desktop-checkout_otmkk9.png)

Further desktop views can be accessed here <a href="static/readme/wireframes/siopafia_desktopview.pdf" target="_blank">here.</a>
