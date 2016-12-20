-- Solution to Project Euler Problem 7
-- https://projecteuler.net/problem=7

-- What is the 10001st prime number?

-- Using Haskell to make the most of Lazy evaluation there.


nth :: Int -> Int
nth = (primes !!).pred

primes :: [Int]
primes = 2 : sieve [3,5..]
    where
        sieve (p:xs) = p : sieve [x | x <- xs, x `mod` p /= 0] 

main :: IO ()
main = do
    t <- readLn :: IO Int
    input <- getContents
    mapM_ putStrLn $ map (show . nth . read) $ words input
