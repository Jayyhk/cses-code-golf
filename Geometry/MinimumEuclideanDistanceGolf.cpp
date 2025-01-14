#include <bits/stdc++.h>
using namespace std;  
#define c(x) (x) * (x)
#define z v[i][
#define w ] - v[j][
#define f ; for (i=n;i--;)
main() {
  long n, i, j, d = 8e18;
  cin >> n;
  array<long, 3> v[n]
  f
    cin >> z 1] >> z 2], z 0] = z 1] - z 2] / 3;
  sort(v, v + n)
  f
    for (j = i; j-- && c(z 0 w 0]) < d;)
      d = min(d, c(z 1 w 1]) + c(z 2 w 2]));
  cout << d;
}