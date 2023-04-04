<h1 align="center">Modus Design</h1>

[View the live project here.](https://modusdesign.herokuapp.com/)

Site owners may use Modus Design to sell their work and offer graphic design services. The website is designed to be responsive and accessible on a range of devices, making it easy to navigate for potential customers and employers.

![mockup](media/modus.png?raw=true)

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
        -   The Lato font is the main font used throughout the whole website. Lato is a sans serif typeface family found on google font.
    -   #### Imagery
        -   Imagery is important. The large, background hero image is black and white, with modern geometric shapes and matches the color theme.

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
3. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
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
        2. Following the hero image are the about, contact and testimonials sections.
        3. At the bottom of the page, the user can search the site contents with an integrated search bar, access social media links, read the privacy notice and sign up to newsletters.

    2. As a User, I want to be able to easily be able to navigate throughout the site to find content.

        1. The site has been designed to be fluid and never to entrap the user. At the top of each page there is a clean navigation bar, each link describes what the page they will end up at clearly.
        2. The about and contact links in the navigation bar redirects the user directly to the corresponding section in the homepage, making the website uncongested with fewer pages.
        3. On the contact section, after a form response is submitted, the page refreshes and the user is brought to the top of the page where the navigation bar is.

    3. As a User, I want to get a quote based on my needs as a potential customer.
        1. After clicking on "get a quote now", the user is redirected to a new page with a custom form.
        2. The form is divided in 3 steps. First, the user needs to select a service, then check the products they need and finally select a plan based on their budget and timeframe.
        3. Once the form is submitted, the user can see the automatically calculated quote, and choose one of the following options: proceed to checkout, redirect to the contact form or start over.

-   #### Site Owner Goals

    1. As a Site Owner, I want to find the details of any new orders.

        1. These are clearly shown in the django admin panel once the owner signs in and clicks on orders.
        2. Once an order is submitted, the Site Owner can access the client details and project details as selected in the custom quote.

    2. As a Site Owner, I want to find the best way to get in contact with the customer with any questions I may have.

        1. Once a user submits the contact form, the form content is shown in the django admin panel.
        2. Here the Site Owner can see the user's name, email and message.
        3. The Site Owner can reply to the user through email.

    3. As a Site Owner, I want to add new testimonials to the homepage easily.
        1. On the testimonials section on the homepage, the Site Owner can create, read, update or delete the testimonials.

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop and iPhone6.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-   N/A

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

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

-   The full-screen hero image code came from this [StackOverflow post](https://stackoverflow.com)

-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

-   [MDN Web Docs](https://developer.mozilla.org/) : For Pattern Validation code. Code was modified to better fit my needs and to match an Irish phone number layout to ensure correct validation. Tutorial Found [Here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/tel#Pattern_validation)

### Content

-   All content was written by the developer.

-   Psychological properties of colours text in the README.md was found [here](http://www.colour-affects.co.uk/psychological-properties-of-colours)

### Media

-   All Images were created by the developer.

### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.