# include<iostream>
# include<conio.h> 

using namespace std;
int atoi(char str){
    return str-'0';
}
int main()
{
    int t,l=0,num,flag = 1;
    cin >> t;
    string str;
    while(t--){
        flag = 1;
        num = 0;
        cin>>str;
        for(int i=0;i<str.length();i++)
        {
            if(isdigit(str[i])){
             num = num*10 + atoi(str[i]);
            }
            else if(str[i]=='-' || str[i] == '+'){
                if(str[i] == '-')
                    flag = -1;
            }
        }
        cout<<num * flag <<endl;
    }
    return 0;
}


// the code is not completed the solution is completed in python