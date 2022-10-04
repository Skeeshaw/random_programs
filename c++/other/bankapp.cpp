#include <iostream>
#include <fstream>
#include <string>
#include <cctype>
using namespace std;

void add_account() {

  string name;
  string address;
  string phone;
  string choice;
  
  cout << "\nPlease enter the information below.";
  
  cout << "\n\nFull Name: ";
  cin.ignore();
  getline(cin,name);

  cout << "\n\nAddress: ";
  cin.ignore();
  getline(cin, address);

  cout << "\n\nPhone Number: ";
  cin.ignore();
  getline(cin, phone);


  ofstream accounts("accounts.txt");

  accounts << "Name: " << name;
  accounts << "\nAddress: " << address;
  accounts << "\nPhone Number: " << phone;
  accounts << "\nBalance: $0.00";
  accounts << "\n";

  accounts.close();

  cout << "\nWould you like to add another account? (y/n) ";
  cin >> choice;

  for (auto& x : choice) {
        x = tolower(x);
    }

  if (choice == 'y') {
    add_account();
  }

  
}




int main() {

  int choice = 0;
  
  cout << "\n\n\n";

  cout << "Banking Account Manager v1.0.0";
  cout << "\n\nMAIN MENU";

  cout << "\n1) New Account" << "\n2) Deposit Amount";
  cout << "\n3) Withdraw Amount" << "\n4) Balance Enquiry";
  cout << "\n5) All Account Holder List" << "\n6) Close an Account";
  cout << "\n7) Modify an Account" << "\n8) Exit\n";
  cout << "Select your option (1-8): ";
  cin >> choice;

  switch(choice) {
    case 1:
      add_account();
      break;
    
  }
  
}