-- Solution to Project Euler Problem 10

-- https://projecteuler.net/problem=10
-- Find the sum of all the primes below two million.

-- https://www.hackerrank.com/contests/projecteuler/challenges/euler010
-- The first line contains t, the number of the test cases, the next t lines will contain an integer N.

--reusing lazy prime evaluation from #7

sumprimes :: Int -> Int
sumprimes n = sum $ takeWhile (<=n) primes

primes :: [Int]
primes = 2 : sieve [3,5..]
    where
        sieve (p:xs) = p : sieve [x | x <- xs, x `mod` p /= 0] 

main :: IO ()
main = print $ sumprimes 2000000
--timeout?
