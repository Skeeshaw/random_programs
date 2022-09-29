#include <iostream>
#include <string>
using namespace std;


int main() {
  //until i find a better way of running functions individually i will just change this line
  //every time i want to run a different one
  bug_collector();
  return 0;
}

void bug_collector() {

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

