# Selenium BDD using PyTest Automation Test Suite

This project is a demonstration of an automation testing framework using **Selenium** for browser automation, **Behavior-Driven Development (BDD)** for clear, human-readable tests, and **Python** for scripting. It was built from scratch and showcases best practices such as the Page Object Model (POM) for maintainability.
I have used PyTest's in house reporter to generate reports.

## Project Structure
The project is organized as follows:
- `features`: Contains the `.feature` files written in Gherkin.
- `pageFactory`: Contains locators and page objects.
  -  `objects`: Locators used in the test.
  -  `pages`: Contains page objects organized by their functionality.
      -  `basePage.py`: Includes the base class for common page interactions.
      -  `ticketPage.py`: Includes page objectes related to ticket creation.
- `utils`: Houses common utility classes like `apiHelpers.py`.
- `test`: Includes the step definitions to login and create a ticket.
- `reports`: Contains reports generated by PyTest for the feature files.
- `conftest.py`: This file is being used to define fixtures that are being used across the project.

## Getting Started
1. Clone this repository to your local machine
2. Configure a virtual environment referring to https://docs.python.org/3/library/venv.html and install dependancies from `requirements.txt`
3. Rest the test by simply entering `pytest` in your CMD.

## Future scope:
- These tests ban easily be executed on remote clouds such as BrowserStack, SauseLabs
- Implement cross browser and parallel testing. Pytest inherently supports this.
- Create a GitHub actions pipeline. 
 
## Contributing
Contributions to enhance the framework and test coverage are welcome! Feel free to fork the repository and submit pull requests with your improvements or bug fixes.

## License
This project is licensed under the MIT License.
