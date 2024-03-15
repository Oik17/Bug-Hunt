
#include <stdio.h>

typedef struct {
    int account_number;
    float balance;
} BankAccountCorrect;

void deposit(BankAccountCorrect *account, float amount) {
    account->balance += amount;  // Correct: adds to the balance
}

float withdraw(BankAccountCorrect *account, float amount) {
    if (amount <= account->balance) {
        account->balance -= amount;
        return amount;
    } else {
        printf(""Insufficient funds.\n"");
        return 0;
    }
}

void display_balance(BankAccountCorrect *account) {
    printf("Account Number: %d\n", account->account_number);
    printf("Current Balance: %.2f\n", account->balance);
}

int main() {
    BankAccountCorrect account;
    account.account_number = 12345;
    account.balance = 1000;

    deposit(&account, 500);
    withdraw(&account, 200);
    display_balance(&account);

    return 0;
}
