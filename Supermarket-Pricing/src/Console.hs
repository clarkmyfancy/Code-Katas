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

continuouslyPromptUserForItems :: Double -> IO()
continuouslyPromptUserForItems previousCartTotal = do  
    userInput <- getLine
    let price = convertToDouble userInput
    let newTotal = scanNewItem price previousCartTotal
    putStr ("Total: " ++ (show newTotal))
    if userInput == (show 0)
        then do 
            printNBlankLines 1
        else do 
            printNBlankLines 2
            continuouslyPromptUserForItems newTotal

convertToDouble :: [Char] -> Double
convertToDouble x = read x :: Double

scanNewItem :: Double -> Double -> Double
scanNewItem previousCartTotal price = do 
    previousCartTotal + price