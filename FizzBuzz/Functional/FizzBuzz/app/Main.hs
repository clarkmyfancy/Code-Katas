module Main where

import Console

main :: IO ()
main = do 
    printHeader
    printBlankLine
    showUpperBoundPrompt
    getUpperBoundAndDeriveResults
    