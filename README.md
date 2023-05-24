<h1 align="center">Modus Design</h1>

[View the live project here.](https://modusdesign.herokuapp.com/)

Site owners may use Modus Design to sell their work and offer graphic design services. The website is designed to be responsive and accessible on a range of devices, making it easy to navigate for potential customers and employers as a B2B.

![mockup](media/modus-mockup.png?raw=true)

## User Experience (UX)

-   ### User stories

    -   #### User Goals

        1. As a user I can fill out a form describing my needs so that get an automatic quote.
        2. As a user I can fill out a contact form so that I can contact the designer directly.
        3. As a user I can continue to checkout after getting a quote so that I can purchase graphical designs to address my needs.
        4. As a user I can easily access social media links so that I can interact with the website.
        5. As a user I can fill out a registration form so that register an account to then get a quote.
        6. As a user, I want to sign up to the Newsletter so that I am emailed any major updates and/or changes to the website.

    -   #### Site Owner Goals

        1. As a site owner I can see a list of all orders so that I can create and deliver the product to my client.
        2. As a site owner I can showcase my work so that I can help the clients visualize what I do.


-   ### Design
    -   #### Colour Scheme
        -   The two main colours used are white and black
    -   #### Typography
        -   The Lato font is the main font used throughout the whole website. The lato font is a sans serif typeface family paired with Merriwheater to create the logo. Both fonts are from google fonts.

## Features

-   Responsive on all device sizes

-   Interactive elements

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)
-   [Django](https://en.wikipedia.org/wiki/Django_(web_framework))


### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
2. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Lato' font into the style.css file which is used on all pages throughout the project.
3. [Visual Studio](https://code.visualstudio.com/)
    - Visual Studio was used for version control to commit to Git and Push to GitHub.
4. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

### Testing User Stories from User Experience (UX) Section

-   #### User Goals

    1. As a User, I want to easily understand the main purpose of the site and learn more about the organisation.

        1. Upon entering the site, users are automatically greeted with a clean and easily readable navigation bar to go to the page of their choice. Underneath there is a Hero Image and a "Get a quote now" button.
        2. Following the hero image are the ethos section, about, contact and testimonials sections.
        3. At the bottom of the page, the user can search the site contents with an integrated search bar, access social media links, read the privacy notice and sign up to newsletters.

    2. As a User, I want to be able to easily be able to navigate throughout the site to find content.

        1. The site has been designed to be fluid and never to entrap the user. At the top of each page there is a clean navigation bar, each link describes what the page they will end up at clearly.
        2. The about and contact links in the navigation bar redirects the user directly to the corresponding section in the homepage, making the website uncongested with fewer pages.
        3. On the contact section, after a form response is submitted, the page refreshes and the user is brought to the top of the page where the navigation bar is.

    3. As a User, I want to get a quote based on my needs as a potential customer.
        1. After clicking on "get a quote now", the user is redirected to a new page with a list of services.
        2. First, the user is required to select a type of service, then the user can write about their custom needs in a textarea field and finally click on the get a quote button to view the total price.
        3. Once the quote is displayed, the user can choose one of the following options: proceed to checkout or be redirected to the contact form.

-   #### Site Owner Goals

    1. As a Site Owner, I want to find the details of any new orders.

        1. These are clearly shown in the django admin panel once the owner signs in and clicks on orders.
        2. Once an order is submitted, the Site Owner can access the client details and project details as selected in the custom quote.

    2. As a Site Owner, I want to find the best way to get in contact with the customer with any questions I may have.

        1. Once a user submits the contact form, the form content is shown in the django admin panel.
        2. Here the Site Owner can see the user's name, email and message.
        3. The Site Owner can reply to the user through email.

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as MacBook Pro, HP ProBook, android mobiles and iPhone6.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-   N/A

## Deployment

### Heroku

The project was deployed to Heroku. The live version can be found [here](https://modusdesign.herokuapp.com/).

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System, Cards and Carousel.

-   [Stripe](https://stripe.com/en-gb-ca) : Stripe software and APIs to accept payments, send payouts, and manage orders online.

### Content

-   All content was written by the developer.

### Media

-   All Portfolio images were created by the developer.

### Acknowledgements

-   My Mentor for continuous helpful feedback.
-   Tutor support at Code Institute for their support.