<h1 align="center">Modus Design</h1>

[View the live project here.](https://modusdesign.herokuapp.com/)

Site users may use ModusDesign to purchase pre-made web templates or custom design services. The website is designed to be responsive and accessible on all devices. This e-commerce platform provides a wide range of choices for its users. This README provides an overview of the purpose, features, testing, and the security measures in place.

![mockup](media/modus-mockup.png?raw=true)

## Intent and Purpose

At its core, ModusDesign aims to offer a user-friendly platform for both users and administrators to engage with web templates and design services effectively. The primary goal is to provide a centralized hub for creating, managing, and sharing design assets.

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

        1. As a site owner, I can see a list of all orders so that I can create and deliver the product to my client.
        2. As a site owner, I can showcase my work so that I can help the clients visualize what I do.
        3. As a site owner, I can use C.R.U.D functionality to add new templates through the product manager link in the My account dropdown menu. I can also edit or delete them once selected.


-   ### Design
    -   #### Colour Scheme
        -   The two main colours used are white and black

    -   #### Typography
        -   The Lato font is the main font used throughout the whole website. The lato font is a sans serif typeface family paired with Merriwheater to create the logo. Both fonts are from google fonts.
    
    - #### Wireframe
        - I created the wireframe with Figma. The link can be found here:
        [ModusDesign Figma](https://www.figma.com/file/oaLvCGHA1YyYgmSKfzmzog/Modus-Design?type=design&node-id=0%3A1&mode=design&t=RfrP8RmXt5egmIum-1)

## Features

# General features:

-   Responsive Design: The website is optimized to provide a seamless user experience across all device sizes, including desktop, tablet, and mobile.
-   Authentication: Users can create an account and securely log in to manage their information and view their order history.
-   Payment System: The platform includes a secure payment system that enables users to purchase HTML templates or hire freelance services conveniently.
-   UX Design: The user interface (UI) is designed with a focus on user experience (UX), incorporating intuitive navigation, interactive elements, and engaging animations.

# Navigation Bar Features:

The navigation bar plays a vital role in facilitating user navigation and providing convenient access to various sections of the website. It ensures seamless movement between different pages, incorporates dropdown menus for enhanced functionality, and complements the overall design and user experience.

-   Logo and Homepage Link: The navigation bar includes a logo that serves as a link to the homepage, allowing users to easily navigate back to the main page.

-   About Page: A link in the navigation bar directs users to the About page, where they can learn more about Modus Design and the designer. Clicking on the link triggers a smooth scrolling action, bringing users back to the homepage section where the about container is located.

-   Services and Products: The navigation bar includes links to the Services and Products pages, where users can explore and access the main features of the site. These pages provide detailed information about the available services and products and offer a convenient platform for users to make payments.

-   Portfolio: The navigation bar features a link to the Portfolio section, showcasing various works and projects. Clicking on the Portfolio link reveals a dropdown menu with three options: Branding Portfolio, Website Portfolio, and Illustration Portfolio. Each option leads to a dedicated gallery, allowing users to explore specific works within each category.

-   Contact Page: The navigation bar provides a link to the Contact page, which allows users to get in touch with the site owner/designer. Similar to the About page, clicking on the Contact link triggers a smooth scrolling action, bringing users back to the homepage section where the contact form is located.

-   My Account: The navigation bar includes a My Account dropdown menu that provides options for user login and registration. When a user is not logged in, the dropdown menu displays login and registration links. Once a user logs in, the menu options change to My Profile and Logout, enabling users to manage their account details and log out from the platform.

-   Admin Access: For users with admin privileges, the My Account dropdown menu includes an additional link called Product Management. This link grants access to the product management section, where admins can perform specific administrative tasks related to the products or services offered.

    -   Admin CRUD functionality
        As well as all of the abpve features(read), the admin can add, edit and delete products, artists and classes from the site - they don't have to visit the admin panel for this.

        Add(Create): From the 'My Account' dropdown, the admin can choose 'Product Management'. This allows them to add a new template by filling in the form.

        Edit(Update): From the item detail page, the admin has an edit button that will direct them to the edit page. All of the form fields wil be populated with the Template information that can then be updated and saved.

        Delete(Delete) From the item detail page, the admin has a delete button that will trigger a confirmation modal. Once the admin confirms deletion, the Template will be removed from the database

# Products and Services:

ModusDesign offers a product catalog featuring diverse design templates, each tailored to different design needs. Our catalog includes:

<b>Website Design</b>: Templates for creating captivating and functional websites across various industries.

<b>Graphic Design</b>: Designs to craft compelling branding materials, including logos, promotional items, stationary, and packaging, from brand identities to album covers.

# Footer:

-   All pages include a footer section located at the bottom, which contains social media links and a newsletter subscription form. The footer provides easy access to the project's social media profiles and allows users to stay updated by subscribing to the newsletter.

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python3](https://www.python.org/)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries & Programs Used

-   [Django](https://en.wikipedia.org/wiki/Django_(web_framework))
-   [Pip3](https://pip.pypa.io/en/stable/)
-   [FontAwesome](https://fontawesome.com/)
-   [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
-   [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Lato' font into the style.css file which is used on all pages throughout the project.
-   [Visual Studio](https://code.visualstudio.com/)
    - Visual Studio was used for version control to commit to Git and Push to GitHub.
-   [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.

### All Others

-   [Heroku](https://www.heroku.com/) used to deploy live site.
-   [Stripe](https://dashboard.stripe.com/login) used for the payments system.
-   [AWS](https://aws.amazon.com/) used for file storage.
-   [GitHub](https://github.com/) used to host repository.
-   [VisualStudio](https://code.visualstudio.com/) was used to develop project and organise version control.
-   [RandomKeygen](https://randomkeygen.com/) used to create a strong password for required <SECRET_KEY>.

## Security Measures

These are the measures taken to safeguard user data and application integrity:

<b>User Authentication</b>: Passwords are securely stored, ensuring user accounts are protected using Django authentication mechanism.

<b>Role-Based Access</b>: The application distinguishes between regular users and administrators. Admins are granted elevated privileges to manage products, while users access design templates and place orders.

<b>Data Validation</b>: Data submitted through forms is thoroughly validated and sanitized to prevent common security vulnerabilities.

<b>Secure Transactions</b>:
Using Stripe's secure payment gateways to facilitate transactions, users can confidently make payments for their selected design templates using credit cards.


## Testing

### Validator Testing
#### HTML
I checked all of the HTML pages using [W3C Markup Validation Service](https://validator.w3.org/)

> **Note**
> There was a few warnings and errors I left untouched. For example, {% extends "base.html" %} provides consistent layouts across pages, though the validator might not be aware of DOCTYPE and lang attributes in the base template when validating individual files. Also, it is not recognizing the {% url '' %} template tag, which is due to the way the URLs are imported. I found it more important to ensure that my web application works properly and renders correctly for users, rather than solely focusing on eliminating these validator warnings.

Errors found & fixed:

- Bag:
    - removed stray `</div>` tag in bag.html
    - I decided to not omit the type attribute in the `<script>` tag since it is not causing any issues but I will take that into consideration in future projects in order to keep my code up-to-date.
    - I made no change to quantity-form.html as item.item_id and item.quantity will always be numeric. In that case, the error message should not be a problem.

- Checkout:
    - removed stray `</div>` tag in checkout.html
    - removed empty `<h1>` heading with nested icon and moved the icon to a div

- Home:
    - No

- Media:
    - No

While some of the errors were simple fixes, other were a lot harder to understand how to fix:

<b>Error: Duplicate attribute id</b>

This error was noted on the following pages:

- Add Artist Page
- Edit Artist Page
- Add Class Page
- Edit Class Page
- Add Product Page
- Edit Product Page

In the `custom_clearable_file_input.html` file in each of the 3 apps, the image input field has an id="new-image" attribute added. But there seems to be another one generated in the form: id="id_image".

If I remove the id from the widget, the file name won't display when uploaded to the form.

I can't find where the second id is being generated to be able to remove it or add id_image to the widget id.

<b>The value of the for attribute of the label element must be the ID of a non-hidden form control.</b>

This error was noted on the following pages:

- Add Class Page
- Edit Class Page

This was a lot harder to figure out as none of the form elements are hidden.

If I had more time I would work on resolving these issue but at this point it's a matter of a deadline, but they're something that I will definitely be going back over.

#### CSS

The CSS file was checked using [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

#### JavaScript
I checked the all the JavaScript files using [JS Hint](https://jshint.com/)

There were a few missing semicolons and ES6 version issues but they were easy fixes.

One error that I found that I was in the checkout javascript file:

<b>JS valiadation error</b>

Because the code comes from Strip itself, I don't want to touch this and am happy to leave it alone.

#### Python

I checked the Py files using [PythonChecker](https://www.pythonchecker.com/)

I used unittest to test the core functionalities of each app.

|Test Name               |Description               |Pass/Fail|
|:-------------         |:----------------------------------|:---|
| **Bag**            |                                         |    
|TestAddToBagFunction  |This test case checks whether the `add_to_bag` function successfully adds a specified quantity of a product to the shopping bag. It validates that the response status code is as expected. It ensures that the bag contents are updated accurately and that appropriate success messages are generated.                   |Pass|
**Checkout**            |                                         |    
|TestAddToBagFunction  |This test case checks whether the `add_to_bag` function successfully adds a specified quantity of a product to the shopping bag. It validates that the response status code is as expected. It ensures that the bag contents are updated accurately and that appropriate success messages are generated.                   |Pass|
|


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
        2. Once an order is submitted, the Site Owner can access the client details and project details.

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

-   None

## Deployment

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


8. Run the development server using `python manage.py runserver`.

### Deploying to Heroku

The project was deployed to Heroku. The live version can be found [here](https://modusdesign.herokuapp.com/).

1. Create a requirements.txt file that lists all the Python packages required for the project. Run the following command in your terminal:
```
$ pip3 freeze --local > requirements.txt
```
2. Create a Procfile in the project's root directory and add the following line:
```
web: gunicorn ARTstop.wsgi:application
```
3. Push the requirements.txt and Procfile to your repository.
4. Log in to Heroku (https://www.heroku.com/) and navigate to the dashboard.
5. Click on "Create New App" and choose a unique name for your app.
6. Select the appropriate region based on your location.
7. Click "Create App" to create the Heroku app.
8. In the Heroku dashboard, navigate to the "Deploy" tab.
9. Under the "Deployment Method" section, select "GitHub".
10. Search for your repository by name and click "Connect" to connect Heroku to your GitHub repository.

## Credits

### Code

-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System, Cards and Carousel.

-   [Stripe](https://stripe.com/en-gb-ca) : Stripe software and APIs to accept payments, send payouts, and manage orders online.

### Content & Media

-   All images and content was created and written by the developer.


### Acknowledgements

-   My Mentor for continuous helpful feedback.
-   Tutor support at Code Institute for their support.
