**Web Automation Task**

**Website Under Test:** [SauceDemo](https://www.saucedemo.com/)

**Overview**

This project automates the testing of key functionalities on **SauceDemo**, an e-commerce web application. The test cases are written following the **Page Object Model (POM)** for better maintainability.

-----
**Technologies Used**

- **Programming Language:** Python.
- **Automation Framework:** Selenium WebDriver.
- **Test Framework:** Pytest.
- **IDE:** PyCharm.
- **Libraries Used:** selenium, pytest, webdriver-manager.

-----
**Project Structure**

The following directory structure follows the **Page Object Model (POM)**, ensuring modularity and maintainability for test scripts.
#### **Web Automation Task** (Root Directory***)***
- **pageObjects** (Contains Page Object Model classes for different web pages)
  - **login\_page.py** → Handles login functionality
  - **cart\_page.py** → Handles cart interactions
  - **checkout\_page.py** → Manages checkout process
  - **inventory\_page.py** → Handles product-related actions
- **tests** (Contains test cases for different functionalities)
  - **test\_login.py** → Tests for login functionality
  - **test\_add\_to\_cart.py** → Tests for adding/removing items from the cart
  - **test\_cart\_badge\_count.py** → Tests the count of products to the cart
  - **test\_sorting.py** → Tests product sorting features
  - **test\_checkout.py**→ Tests the checkout process
  - **test\_locked\_out\_user.py** → Tests the special case of locked-out customer
  - **test\_logout.py**→ Tests the logout feature of the website
  - **conftest.py**→ Contains the mandatory functions
- ` `**utils** 
- **README.md** → Documentation for project setup, execution, and details.

**Test Cases Implemented**

**1) Login Functionality Test**

**Scenario:** Verify login with valid and invalid credentials.

**Steps:**

1. Navigate to **saucedemo.com**.
1. Enter **valid credentials**:

   Username: standard\_user

`          `Password: secret\_sauce

1. Click the **Login** button.
1. Verify successful login by checking the **Products page**.

**Negative Cases:**

- Try incorrect username/password (e.g., wrong\_user / secret\_sauce).
-----
**2) Add to Cart Functionality**

**Scenario:** Verify that products can be added to the cart.
**Steps:**

1. Login with **valid credentials**.
1. Add the first **two products** to the cart.
1. Click the **cart icon** to view the cart.
1. Verify that both products are **present** in the cart.

**Edge Cases:**

- Add and remove items **twice**.
- Verify that the **cart badge count updates correctly**.
-----
**3) Checkout Process Validation**

**Scenario:** Automate the full checkout process.
**Steps:**

1. Login with **valid credentials**.
1. Add a **product** to the cart.
1. Click the **cart icon** and proceed to checkout.
1. Enter checkout information:
   1. **First Name:** John
   1. **Last Name:** Doe
   1. **Postal Code:** 12345
1. Click **Continue** and verify the correct item appears in the summary.
1. Complete the order by clicking **Finish**.
1. Verify the success message: **“Thank you for your order!”**
-----
**4) Sorting Products Validation** 

**Scenario:** Verify the sorting functionality for products.
**Steps:**

1. Login to the application.
1. Use the **"Sort by" dropdown** to sort products by:
   1. **Price (low to high)**
   1. **Price (high to low)**
   1. **Name (A to Z)**
   1. **Name (Z to A)**
1. Verify that the products are displayed in the **correct order**.
-----

**5) Logout Functionality Test**

**Scenario:** Verify that the logout process works correctly.
**Steps:**

1. Login with **valid credentials**.
1. Click the **hamburger menu (☰)** in the top-left corner.
1. Click **Logout**.
1. Verify that the user is redirected to the **login page**.
-----
**6) Locked-Out User Validation**

**Scenario:** Ensure that a locked-out user cannot log in.
**Steps:**

1. Go to the login page.
1. Enter the credentials:
   1. **Username:** locked\_out\_user
   1. **Password:** secret\_sauce
1. Click **Login**.
1. Verify the error message: **“Sorry, this user has been locked out.”**
-----
**7) Cart Badge Count Validation**

**Scenario:** Verify that the cart badge updates correctly.
**Steps:**

1. Login to the app.
1. Add **multiple products** to the cart.
1. Verify the cart badge shows the **correct item count**.
1. Remove an item and verify the badge **updates accordingly**.

**2) Setup Virtual Environment**

To set up the virtual environment, follow these steps:

1. **Create a virtual environment** **using the following command**:
- bash
- CopyEdit
- python -m venv venv
1. **Activate the virtual environment:**
- On **macOS/Linux**:
- bash
- CopyEdit
- source venv/bin/activate
- On **Windows**:
- bash
- CopyEdit
- venv\Scripts\activate
-----
**3) Install Dependencies**

To install the necessary dependencies for the project, run the following command:

- bash
- CopyEdit
- pip install -r requirements.txt

This will install all the packages listed in requirements.

-----

**4) Run Test Cases**

To run the automated test cases, use the following command with **Pytest**: 

- bash
- CopyEdit
- pytest -v

This command will execute all the tests in the test folder and show the results in a verbose output.

## **Contact Information**
**Developer:** Ananya Deb
**GitHub Profile:** [aananyaa-deb](https://github.com/aananyaa-deb/)

