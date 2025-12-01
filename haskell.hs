#!/usr/bin/env runhaskell
module Main where
import System.Environment (getArgs)

-- | Solve the puzzle
-- TODO: Replace with actual implementation
solve :: String -> Int
solve input =
    let ls = lines input
    in length ls

-- | Main entry point
main :: IO ()
main = do
    args <- getArgs
    input <- case args of
        [filename] -> readFile filename
        _          -> getContents
    print $ solve input
