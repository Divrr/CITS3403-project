# CITS3403 Project

## Project Overview

This project is a web application for students to help students, where you can offer your skills and services or request help when you need it and together, help build a vibrant and supportive UWA community.

### User Workflow

Here are some basic vocabulary used in this website:

(noun) Offer: A service a user wants to provide.
(noun) Request: A service a user is asking to be provided.
(noun) Your "Accept": An offer or request that has been accepted by you.
(noun) Your "Item": An offer or request that you have created.
(noun) "Accept": Any offer or request that has been accepted by another user.
(noun) "Item": Any offer or request.
(verb) To "accept" an offer: You are agreeing to recieve a service that another user is offering.
(verb) To "accept" a request: You are agreeing to provide the service that another user is asking for.
(verb) To "resolve" an item: You, as the creator of an item, are removing it for yourself and all other users by clicking the tick button
(verb) To "cancel" an accept: You, as a user who has accepted an item, is choosing to undo your accept, thereby removing that item from your homepage and returning it to its respective Offers/Requests page for another user to accept by clicking the x button.

1. **Sign Up**: Click the blue link on the page you are on that says "Don't have an account? Create Account here" to navigate to the page to create a new account. Once you are there, create an account by providing your username, email, password, and then password again. Click "Signup". You are now navigated to the sign-in.
2. **Sign In**: Log in with your username and password. If you would like the site to remember your details, select "Remember Me". Click "Login". You are now navigated to the user's page called "Home".
3. **Welcome Message**: Upon login and subsequent navigation to the user page "Home", you will see a pop-op welcome message describing the purpose of this webseit. Read carefully. Click "Close".
4. **Navigation Bar**: At the top of every page, there is a navigation bar. If you are on another page and want to return to the user page to view your items and accepts, click "Home". If you want to browse, search, or accept offers, click "Offers". If you want to browse, search, or accept requests, click "Requests".
5. **Navigate Offers/Requests**:
   - **Offers Page**: You can browse and click "accept" to accept various service offers. Any accepted offer will appear in the Home page under "Your Accepts" and will the blue. The description of that offer in "Your Accepts" will be the the italisized content of that offer while it was in the "Offers" page.
   - **Requests Page**: You can browse and click "accept" accept requests for services. Any accepted request will appear in the Home page under "Your Accepts" and will the orange. The description of that request in "Your Accepts" will be the the italisized content of that request while it was in the "Requests" page.
   - **Search Functionality**: You can search for specific keywords or scroll through the list by using the search bar at the top of "Offers" and "Request". The search bar in "Offers" only searches offers, and the same goes for Requests.
6. **Create an Offer or Request**:
   Navigate to the "Home" page to make a new Offer or Request. Click the big green plus button. You are now navigated to the form to create your offer or request. Select either "Offer" or "Request" from Type (offers and requests are both types of items), input a Category name to categorize your item, and input a Description to provide some more details about your item. Click submit when you are done. The new offer/request will appear on the offers/requests page and under "Your Items". You are automatically navigated back to "Home".
7. **Manage Your Accepts in Home**:
   If you no longer wish to accept another user's offer or request, you can click the red x button to the right of that respective accepted offer or request ("accept") under "Your Accepts" in "Home". This will delete it for you only by removing it from "Your Accepts". It will return that offer/accept to its respective Offer/Accepts page for another user to accept. In contrast, if you want to proceed with that accept, you can click the "Contact --insert username--" button to open an email to the user that created that offer or request to discuss how the offer or request will be carried out.
8. **Manage Your Items in Home**: If you wish to delete an offer or request that you have made, click the green tick button to the right of that respective offer or request This will detete it for yourself and for all other users. Once another user has accepted that offer or request, a "Contact --insert username--" button will appear to the right of that item. Clicking this contact button will open up an email to the user that accepted your item, where the two of you can discuss the details of the item.
9. **Log Out**: Once you are done, you can click "Logout" in the navigation bar at the top of the page.

## Files and Directory Structure

### Configuration and Initialization

- **`config.py`**: Configuration settings for the Flask application.
- **`application.py`**: Main application file where the Flask app is created and routes are defined.
- **`__init__.py`**: Initialization file for setting up the Flask app and configuration.
- **`env.py`**: Environment configuration file for setting up environment variables.
- **`alembic.ini`**: Configuration file for Alembic, a database migration tool for SQLAlchemy.

### Application Logic

- **`forms.py`**: Form definitions using Flask-WTF for handling and validation.
- **`models.py`**: Database models using SQLAlchemy for ORM.
- **`routes.py`**: Routes/endpoints and corresponding view functions.
- **`test_data.py`**: Test data for populating the database during development or testing.
- **`unit_testing.py`**: Testing scripts to ensure application functionality.
- **`test_unit_testing.py`**: Further testing scripts to ensure application functionality.
- **`selenium_testing.py`**: Selenium-based unit tests for verifying application functionality.
- **`blueprints.py`**: Sets up a Flask Blueprint for the main module and imports the routes.

### Templates (HTML)

- **`templates/base.html`**: Base template that other HTML templates extend, including common HTML structure and resources.
- **`templates/login.html`**: Login page template for user authentication.
- **`templates/mainpage.html`**: Main page template displaying user items and accepted items.
- **`templates/navbar.html`**: Navigation bar template for consistent navigation between menu items.
- **`templates/offer_request_form.html`**: Form template for creating offers and requests.
- **`templates/offers.html`**: Template for displaying available offers.
- **`templates/requests.html`**: Template for displaying available requests.
- **`templates/searchboxitem.html`**: Template for rendering individual search result items.
- **`templates/signup.html`**: Sign-up page template for new user registration.

### Static Files

#### CSS

- **`static/css/login_signup.css`**: Styling for the login and signup pages.
- **`static/css/main.css`**: Styling for the home page.
- **`static/css/offers.css`**: Styling for the offers page.
- **`static/css/requests.css`**: Styling for the requests page.

#### JavaScript

- **`static/js/form.js`**: Handles the offers/ request form-related scripts.
- **`static/js/resolve_activity.js`**: Manages the resolving of completed offer and request services.
- **`static/js/cancel_activity.js`**: Handles the cancelling of offer and request services.
- **`static/js/accept_activity.js`**: Manages the acceptance of activities.
- **`static/js/search.js`**: Manages search functionality.
- **`static/js/toast.js`**: Handles toast notifications.
- **`static/js/welcome_modal.js`**: Handles the welcome pop up message.

### Miscellaneous

- **`script.py.mako`**: Mako template script for generating dynamic content.
- **`LICENSE`**: Licensing information for the project.
- **`requirements.txt`**: Used to install all the necessary dependencies.

### Installation Steps

### Installation Steps

1. **Clone the repository**

   ```bash
   git clone <https://github.com/Divrr/CITS3403-project.git>
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Start the application**

   ```bash
   flask run
   ```

## Running the Application

Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the application in action.

## Authors

- **Adib Rohani 23722809**: [Divrr](https://github.com/Divrr)
- **Aviv Dvir Silman 22917067**: [hhK2001-blast](https://github.com/hhK2001-blast)
- **Theresa Needham 23348927**: [TheresaNeedham](https://github.com/TheresaNeedham)
- **Zahra Vink 23987684**: [zahravink](https://github.com/zahravink)

## Licensing

This project is licensed under the terms specified in the `LICENSE` file.

## Image References

- **Plus Icon**:
- **Profile Icon**:
  FLATICON- ![Profile Icon](https://www.flaticon.com/free-icon/profile_3135715)
- **Tick Icon**:
  Stockio- ![Tick Icon](https://www.stockio.com/free-clipart/green-tick-simple#google_vignette)
- **University of Western Australia Logo**:
  ![UWA Logo](https://www.google.com/url?sa=i&url=https%3A%2F%2Fseeklogo.com%2Fvector-logo%2F491535%2Fthe-university-of-western-australia&psig=AOvVaw0kMSh4zbcN1o5-PJmUoKJ0&ust=1716040660013000&source=images&cd=vfe&opi=89978449&ved=0CBQQjhxqFwoTCLDvoOHrlIYDFQAAAAAdAAAAABAI)
- **University of Western Australia Background**:
  Churchill Gowns- ![UWA Background](https://www.churchillgowns.com.au/pages/university-of-western-australia)
- **Cancel Icon**:
  CLEANPNG- ![Cancel Icon](https://www.cleanpng.com/png-button-computer-icons-cancel-button-831795/)

# Acknowledgements

- ahax. (2017, January 5). AJAX request to perform search in Flask. Stack Overflow. https://stackoverflow.com/questions/41475945/ajax-request-to-perform-search-in-flask
- Cairocoders. (2020, November 15). Flask MySQL jquery ajax Live Search. YouTube. https://www.youtube.com/watch?v=Us8gBacBDJ8
- contributors, M. O., Jacob Thornton, and Bootstrap. (n.d.). Toasts. Getbootstrap.com. https://getbootstrap.com/docs/5.3/components/toasts/
- Red Eyed Coder Club. (2022, May 2). Flask AJAX Tutorial: Basic AJAX in Flask app | Flask casts. YouTube. https://www.youtube.com/watch?v=nF9riePnm80

AI tools were used to explain syntax and errors, populate data, and suggest alterations. These AI tools include: Github copilot, ChatGPT, Microsoft Copilot, and Pi.
