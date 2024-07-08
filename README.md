# Banking System

Welcome to the Banking System project! This is a simple command-line banking system implemented in Python, allowing users to create accounts, log in, and perform various banking operations such as viewing balance, depositing money, withdrawing money, transferring money, and viewing transaction history.

## Features

- **Create Account**: Users can create a new bank account with a unique username and password.
- **Login**: Existing users can log in to their accounts using their username and password.
- **View Balance**: Users can check their current account balance.
- **Deposit Money**: Users can deposit money into their account.
- **Withdraw Money**: Users can withdraw money from their account.
- **Transfer Money**: Users can transfer money to another user's account.
- **View Transaction History**: Users can view the history of all transactions made on their account.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x installed on your system.
- `git` installed on your system.

### Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/Pivonn-tech/banking_system.git
    cd banking_system
    ```

2. **Run the banking system**:

    ```sh
    python bank.py
    ```

## Usage

Once you run the `bank.py` script, you will be presented with a main menu with the following options:

1. **Create Account**: Follow the prompts to create a new account. You will need to provide a name, create a username, and set a password.
2. **Login**: Enter your username and password to log in to your account. If the login is successful, you will see the account menu with the following options:
    - **View Balance**: Displays your current account balance.
    - **Deposit Money**: Enter the amount to deposit into your account.
    - **Withdraw Money**: Enter the amount to withdraw from your account.
    - **Transfer Money**: Transfer money to another user's account by providing their username and the amount to transfer.
    - **View Transaction History**: View the history of all transactions made on your account.
    - **Logout**: Logout from your account and return to the main menu.
3. **Exit**: Exit the banking system.

## File Structure

- `bank.py`: The main Python script that contains the code for the banking system.
- `accounts.json`: A JSON file that acts as the database for storing user account details and transactions.

## Contributing

Contributions are welcome! If you have any ideas or suggestions to improve this project, please feel free to fork the repository and submit a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add some feature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Acknowledgements

- Inspired by various simple banking system examples and tutorials.

---

Thank you for using our Banking System project! We hope it helps you manage your virtual finances effectively.
