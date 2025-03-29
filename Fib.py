memo = [None] * 100
counter = 0


class DP:
    def fib(self,n):
        global counter
        counter += 1

        if memo[n] is not None:
            return memo[n]
        if n == 0 or n == 1:
            return n
        memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return memo[n]


print(DP.fib(35))
print(f"Counter: {counter}")
