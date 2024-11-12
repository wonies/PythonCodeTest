#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    for (int i=0; i<n; i++)
    {
        string a;
        cin >> a;

        bool is_palin = true;
        int len = a.length();

        for (int j =0; j<len/2 ; j++)
        {
            if (a[j]!=a[len-j-1])
            {
                is_palin = false;
                break;
            } 
        }
        if (is_palin)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}