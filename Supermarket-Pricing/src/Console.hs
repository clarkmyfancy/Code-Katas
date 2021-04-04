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

-- prompt:
-- showUpperBoundPrompt :: IO() 
-- showUpperBoundPrompt = putStr "what is the upper bound?  -> "

-- getinputfromuser:
-- getUpperBoundAndDeriveResults :: IO()
-- getUpperBoundAndDeriveResults = do 
--     upperBound <- getLine
--     printNBlankLines 1
--     printTranslation (read upperBound :: Int)