#include <iostream>
#include <string>
using namespace std;

class MyClass {       // The class
  public:             // Access specifier
    int total;        
};
void bug_collector() {

  cout << "Welcome to Bug Masters bug collection system." << "\n";

  //in c, the accumulator can be set in the for loop conditions
  //this is the same as "for num in range(1,6)"
  for (int accum = 1;accum < 6;accum++) {
    int userinput;
    cout << "\nHow many bugs did you collect on day " << accum << "? ";
    cin >> userinput;

    int total = total + userinput;
    
  }
  cout << "Great job, you collected " << total << " bugs this week. You're the bug master!";
}

int main() {
  bug_collector();
  return 0;
}