# Banking Simulator Application
This application is a python based banking application. It allows the user to create an account, deposit money, withdraw money, move money to a savings account, buy and sell stocks and/or cryptocurrencies, check account information, check account balances and take a quiz to win a stock share.

## Live Site & Repository

## Contents
* [Project Planning](#project-planning)
* [Project Walkthrough](#project-walkthrough)
* [Future Features](#future-features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Bugs](#bugs)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

## Project Planning

## Project Walkthrough
### Overview
* On startup of the application the user is met with a gretting method and a propmt to begin registering a new account.
![start up screen](documentation/start-up.jpg)

* The user is then prompted to enter their first name, last name, age, country of residence and email address.
![User first name input](documentation/first-name.jpg)<br>
![User last name input](documentation/last-name.jpg)<br>
![User age input](documentation/age.jpg)<br>
![User country input](documentation/country.jpg)<br>
![User email input](documentation/email.jpg)
* When all user details are entered correctly they are met with a confirmation message and a random account number is generated for the user. <br>The user is then prompted to enter an amount to deposit to their account.<br>
![Confirmation that account has been created](documentation/account-creation.jpg)

* The user is then navigated to to the main menu.<br>From here the user has access to the different functions of the application.<br>
![Main Menu](documentation/main-menu.jpg)

* The user can check their account balance <br>
![Check Balance](documentation/check-balance.jpg)

* The user can make a deposit to their current account balance<br>
![Deposit to current account](documentation/deposit-to-current.jpg)<br>
![Successful deposit to current account](documentation/successful-deposit.jpg)

* The user can withdraw money from their account after entering their correct account number that was assigned to the on registration.
![withdraw security page](documentation/withdarw-security.jpg)<br>
![user prompt to withdraw](documentation/withdraw.jpg)<br>
![successful withdrawl of funds](documentation/successful-withdraw.jpg)

* The user can deposit money from their current account to their savings account.
![deposit money to savings account prompt](documentation/deposit-to-savings.jpg)<br>
![successful deposit to savings](documentation/deposit-to-savings-success.jpg)

* The user can invest in 3 different stocks. The stock prices are generated randomly.<br>
![investment menu](documentation/investment-menu.jpg)
![stock investment menu](documentation/stock-investment-menu.jpg)
![prompt to buy share in google](documentation/buy-google.jpg)
![successful purchase of google](documentation/buy-google-success.jpg)

* The user can invest in 2 different cryptocurrencies.<br>
![crypto investment menu](documentation/invest-in-crypto-menu.jpg)
![user propted to purchase bitcoin](documentation/buy-bitcoin.jpg)
![successfull purchase of bitcoin](documentation/buy-bitcoin-success.jpg)

* The user can sell their stocks or cryptocurencies and will be told whether they sold at a profit or loss.
![sell crypto menu](documentation/sell-crypto-menu.jpg)
![user prompted to sell bitcoin](documentation/sell-bitcoin.jpg)
![successfull sale of bitcoin](documentation/sell-bitcoin-success.jpg)

* The user can check their account information.<br>
![checking user account information](documentation/user-info.jpg)

* The user can take a quiz about the stock market with 4 different questions. Upon successful completion of the quiz the user is given a share of google stock.<br>
![quiz start up prompt](documentation/quiz.jpg)
![quiz question](documentation/quiz-1.jpg)
![user is informed on the result of the answered question](documentation/question-result.jpg)<br>
![User quiz results printed to the screen](documentation/quiz-result.jpg)

* The user can log out and quit the application.<br>
![User logging out of application](documentation/log-out.jpg)

### Fail safes
* When the user tries to enter the wrong character they are prompted to enter they are met with an error
![User entered the wrong character](documentation/not-valid-continue.jpg)

* Regular expression operations are used to make sure only letters are used in the name and country, only number are used in the age and the email must consist of an "@" and "." symbols.<br>
When the application prompts the user to add a money value regular expresions are called to make sure only a number value is entered.<br>
If the user enters no value for any of these prompts the will get a "No data entered" error message.<br>
![User informed of using characters that are not allowed](documentation/wrong-characters.jpg)

* If the user enter an age below the age of 18 they will be informed that they cannot create an account under the age of 18
![User informed they must be over the age of 18](documentation/age-limit.jpg)

* If the user's balance is to low for the action they are trying to undertake, they will be informed they have an insuffiecient balance to complete the operation.<br>
An example of this would be that they try to deposit €100 to their savings account but their current account balance is only €50.<br>
![User informed they have insufficient funds to complete action](documentation/insufficient-funds.jpg)

* If the user has no money invested in stocks or crypto and tries to sell their investments they will be given an alert message and a prompt.<br>
![User informed they have no money invested](documentation/no-investments.jpg)

* Because the application only allows the user to own one stock or crypto at a time if the user already owns a share in Google they will recieve the current value of Google deposited into their current account.<br>
![User informed they can only have 1 share in google and money has been added to their account](documentation/quiz-result-owning-google.jpg)

* If the user enters their account number wrong they will be given a security message and prompted to return to the main menu.<br>
The account number can always be found in user info section.<br>
![User informed they entered the wrong account number](documentation/account-num-wrong.jpg)

* If the user enters a non valid character on the menus the menu function is re-called.






