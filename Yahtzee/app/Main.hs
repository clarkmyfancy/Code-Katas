module Main where

import Console

main :: IO ()
main = do
    printStartPrompt
    promptForHowManyPlayers
    getNumberOfPlayers

