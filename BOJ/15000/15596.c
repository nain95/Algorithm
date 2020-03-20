long long sum(int *a, int n) {
	long long ans = 0;
    while (n != 0) {
		ans += a[n-1];
		n--;
	}
	return ans;
}