# include<iostream>
# include<conio.h>
#include <iterator>
# include<set>
using namespace std;
int main()
{   
    string str,str1,tmpStr;
    cin>>str;
    for(int i=0;i<str.length()-1;i++){
        if (str[i]!=str[i+1]){
            tmpStr = str[i];
            cout<<tmpStr<<endl;
            str1.append(tmpStr);
        }
        else
            i++;
    }
    cout<<str1;
    return 0;
}