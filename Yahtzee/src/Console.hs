module Console where

printStartPrompt :: IO()
printStartPrompt = do
    printNBlankLines 3
    putStrLn "____________________________"
    putStrLn " Welcome to Yahtzee!"
    printNBlankLines 3

printNBlankLines :: Int -> IO()
printNBlankLines 0 = putStr ""
printNBlankLines n = do 
    putStr "\n"
    printNBlankLines (n - 1)

promptForHowManyPlayers :: IO()
promptForHowManyPlayers = do
    putStrLn "How many players?"
    putStr " > "

getNumberOfPlayers :: IO()
getNumberOfPlayers = do 
    playerCount <- getLine
    putStrLn playerCount
