-- Solution to Project Euler Problem 7
-- https://projecteuler.net/problem=7

-- What is the 10001st prime number?

-- Using Haskell to make the most of Lazy evaluation there.

main :: IO ()
main = do
    t <- readLn :: IO Int
    input <- getContents
    mapM_ putStrLn $ map (show . nth . read) $ words input
