// C++ program to find  minimum number of swaps
#include<bits/stdc++.h>
using namespace std;
 
// Function returns the minimum number of swaps
long minSwaps(long arr[], long n)
{
    // Create an array of pairs where first element is array element and second element is position of first element
    pair<long, long> arrPos[n];
    for (long i = 0; i < n; i++)
    {
        arrPos[i].first = arr[i];
        arrPos[i].second = i;
    }
 
    // Sort the array by array element values to get right position of every element as second element of pair.
    sort(arrPos, arrPos + n);
 
    // To keep track of visited elements. Initialize all elements as not visited or false.
    vector<bool> vis(n, false);
 
    // Initialize result
    long ans = 0;
 
    // Traverse array elements
    for (long i = 0; i < n; i++)
    {
        // already swapped and corrected or already present at correct pos
        if (vis[i] || arrPos[i].second == i)
            continue;
 
        // find out the number of node in this cycle and add in ans
        long cycle_size = 0;
        long j = i;
        while (!vis[j])
        {
            vis[j] = 1;
 
            // move to next node
            j = arrPos[j].second;
            cycle_size++;
        }
 
        // Update answer by adding current cycle.
        ans += (cycle_size - 1);
    }
 
    // Return result
    return ans;
}
 
// Driver program to test the above function
int main()
{
    long arr[100000];
    long i,n;
    cin >> n;
	for(i=0; i<n; i++)
		cin >> arr[i];
    cout << minSwaps(arr, n) << "\n";
    return 0;
}
