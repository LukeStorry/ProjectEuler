-- Solution to Project Euler Problem 12
-- https://projecteuler.net/problem=12
-- What is the value of the first triangle number to have over five hundred divisors?

-- Uses haskell to use lazy evaluation of triangle generation

euler12 :: Int -> Int
euler12 n = head $ filter ((>n) . numberOfDivisors) triangleNumbers

triangleNumbers = scanl1 (+) [1..]

numberOfDivisors :: Int -> Int
numberOfDivisors n = length [ x | x <- [1..n], n `mod` x == 0]


main = do		 
t <- readLn :: IO Int		
input <- getContents
mapM_ putStrLn $ map (show . euler12 . read) $ take t $ words input
