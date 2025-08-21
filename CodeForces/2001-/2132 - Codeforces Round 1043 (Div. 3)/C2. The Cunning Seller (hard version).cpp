#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int main() {
    int t;
    cin >> t;
    
    const long long INF = 1e18;
    vector<long long> cost = {3, 10, 33, 108, 351, 1134, 3645, 11664, 37179, 118098, 373977, 1180980, 3720087, 11691702, 36669429, 114791256, 358722675, 1119214746, 3486784401, 10847773692, 33705582543};
    vector<long long> number = {1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467, 3486784401};
    
    while (t--) {
        int n, k;
        cin >> n >> k;
        
        vector<vector<long long>> dp(k + 1, vector<long long>(n + 1, INF));
        dp[0][0] = 0;
        
        for (int i = 1; i <= k; i++) {
            for (int j = 0; j <= n; j++) {
                dp[i][j] = dp[i - 1][j];
                for (int x = 0; x < cost.size(); x++) {
                    if (number[x] <= j) {
                        dp[i][j] = min(dp[i][j], dp[i - 1][j - number[x]] + cost[x]);
                    }
                }
            }
        }
        
        if (dp[k][n] != INF) {
            cout << dp[k][n] << endl;
        } else {
            cout << -1 << endl;
        }
    }
    
    return 0;
}
