module Console where

import Date

printNBlankLines :: Int -> IO()
printNBlankLines 0 = putStr ""
printNBlankLines n = do 
    putStr "\n"
    printNBlankLines (n - 1)

displayDate :: IO()
displayDate = do
    Date.date

greetCustomer :: IO()
greetCustomer = do
    putStr "Hey! Let's scan some items!"
    printNBlankLines 1 

continuouslyPromptUserForItems :: IO()
continuouslyPromptUserForItems = do    
    item <- getLine
    putStr item
    if item == (show 0)
        then do 
            printNBlankLines 1
        else do 
            printNBlankLines 2
            continuouslyPromptUserForItems

    

-- prompt:
-- showUpperBoundPrompt :: IO() 
-- showUpperBoundPrompt = putStr "what is the upper bound?  -> "

-- getinputfromuser:
-- getUpperBoundAndDeriveResults :: IO()
-- getUpperBoundAndDeriveResults = do 
--     upperBound <- getLine
--     printNBlankLines 1
--     printTranslation (read upperBound :: Int)