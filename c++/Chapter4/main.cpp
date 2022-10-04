#include <iostream>
#include <string>
#include <fstream>
using namespace std;




void bug_collector() {
  //yeah this func is funny but it adds your bugs together
  cout << "Welcome to Bug Masters bug collection system." << "\n";

  //idk why but if i dont set this to 0 it gives me a weird output
  int total = 0;
  
  int userinput;
  
  //in c, the accumulator can be set in the for loop conditions
  //this is the same as "for num in range(1,6)"
  for (int accum = 1;accum < 6;accum++) {
    
    
    cout << "\nHow many bugs did you collect on day " << accum << "? ";
    cin >> userinput;

    total = total + userinput;
    
  }
  
  cout << "\nGreat job, you collected " << total << " bugs this week. You're the bug master!";
}

void distance_traveled() {
  //shows how far you traveled, given hours and speed
  int mph;
  int hours;
  
  cout << "\nEnter the speed of the vehicle in mph: ";
  cin >> mph;

  //simple input validation
  //later programs will use more advanced validation
  while(mph < 1) {
    cout << "\nYour answer was not calculatable. Please try again.";
    distance_traveled();
  }

  cout << "\nEnter the amount of hours the vehicle traveled:";
  cin >> hours;

  while(hours < 1) {
    cout << "\nYour answer was not calculatable. Please try again.";

    cout << "\nEnter the amount of hours the vehicle traveled:";
    cin >> hours;

  }

  cout << "\nHour\tDistance";
  cout << "\n----------------";

  for(int travel = 1; travel < hours + 1; travel++) {

    cout << "\n" << travel << "\t\t" << mph * travel; 
  }
  
  cout << "\n";
  
}

void pennies() {
  //doubles pennies for amount of days user specifies
  int days;
  double amount = 0.01;
  
  cout << "Enter the amount of days to double pennies: ";
  cin >> days;

  cout << "\nDays\t\tAmount";
  cout << "\n------------------";
  for(int accum = 1;accum < days + 1;accum++) {
    
    cout << "\n " << accum << "\t\t\t$" << amount;
    amount *= 2;
  }

  
}

void hot_dog() {

  //c++ has constants built in
  const int dogs_per_pack = 10
  const int buns_per_pack = 8

  int people;
  int dogsperperson;

  cout << "\nHow many people will be attending your event? ";
  cin >> people;
  cout << "\n\nHow many hot dogs will be cooked per person? ";
  cin >> dogsperperson;

  
  
}


int main() {
  //until i find a better way of running functions individually i will just change this line
  //every time i want to run a different one
  hot_dog();
  return 0;
}