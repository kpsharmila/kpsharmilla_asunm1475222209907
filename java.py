
package Account;
import java.util.Date;

class Account {
private int id;
private double balance; //balance for account
private double annualInterestRate; //store interest rate
private Date dateCreated; //store date account created

// no arg constructor for default account 
Account() {
    id = 0;
    balance = 0.0;
    annualInterestRate = 0.0;
}
//constructor with specfic id and initial balance
Account (int newId, double newBalance) {
id = newId;
balance = newBalance;
}
//
Account (int newId, double newBalance, double newAnnualInterestRate) {
    id = newId;
    balance = newBalance;
    annualInterestRate = newAnnualInterestRate;
}
//accessor and mutator methods
public int getId() {
    return id;
}
public double getBalance() {
    return balance;
}
public double getAnnualInterestRate() {
    return annualInterestRate;
}
public void setId (int newId) { 
    id = newId;
}
public void setBalance (double newBalance) {
    balance = newBalance;
}
public void setAnnualInterestRate (double newAnnualInterestRate) {
    annualInterestRate = newAnnualInterestRate;
}
public void seDateCreated (Date newDateCreated) { 
    dateCreated = newDateCreated;
}
//Method for monthly interest
double getMonthlyInterestRate() {
    return annualInterestRate/12;
}
//Define method withdraw
double withdraw (double amount) {  
    return balance -= amount;
}
//Define method deposit 
double deposit(double amount) {
    return balance += amount;
}

    public static void main(String[] args) {
        java.util.Date dateCreated = new java.util.Date();
        Account account1 = new Account (1122, 20000, 0.045); //
        //account1.withdraw(2500);
        //account1.deposit(3000);
        System.out.println("----------------------------------------");
        System.out.println("   Welcome to your online account!");
        System.out.println("Please find your account details below");
        System.out.println("----------------------------------------");

        System.out.println("Account ID:" + " " + account1.id);
        System.out.println("Initial Balance:" + account1.getBalance());

        System.out.println("Balance after Withdraw:" + " " + account1.withdraw(2500));
        System.out.println("Balance after deposit" + " " + account1.deposit(3000));


        System.out.println("Interest Rate:" + " " + account1.getAnnualInterestRate());

        System.out.println("Monthly Interest:" + " " + "£" + account1.getMonthlyInterestRate());


        System.out.println("Date Account was Created:" + " " + dateCreated);



        System.out.println("------------------------");
        System.out.println("The Process is complete");
        System.out.println("------------------------");