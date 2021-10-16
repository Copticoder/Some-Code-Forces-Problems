#include <iostream>
using namespace std;
int main(){
    int n,m;
    int numList[100001];
    cin>>n;
    for(int i=0; i<n;i++){
        cin>>m;
        numList[m]=i;
    }
    long long vas=0, pet=0;
    int queNum, query;
    cin>>queNum;
    while(queNum--){
        cin>>query;
        vas+=numList[query]+1;
        pet+=(n-numList[query]);
    }
    cout<<vas<<' '<<pet;

}