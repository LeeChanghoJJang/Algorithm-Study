#include <stdio.h>

long long a, b, c;

long long rem(long long num) {
	if (num == 1) return a % c;
	else if (num % 2 == 0) return (rem(num / 2) % c) * (rem(num / 2) % c) % c;
	else return ((rem(num / 2) % c) * (rem(num / 2) % c) % c) * (a%c) % c;
}

int main() {

	scanf("%lld %lld %lld", &a, &b, &c);

	printf("%lld", rem(b));

	return 0;
}