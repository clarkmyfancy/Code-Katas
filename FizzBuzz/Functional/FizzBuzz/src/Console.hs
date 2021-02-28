module Console where

import Translator

printHeader :: IO() 
printHeader = do
    putStrLn "__________________________"
    putStrLn "         welcome          "
    putStrLn "       to FixxBucks       "

printBlankLine :: IO()
printBlankLine = putStr "\n"

showUpperBoundPrompt :: IO() 
showUpperBoundPrompt = putStr "what is the upper bound?  -> "

showRangeWith :: Int -> [Char]
showRangeWith upperBound = "[1.." ++ (show upperBound) ++ "]"

getUpperBoundAndDeriveResults :: IO()
getUpperBoundAndDeriveResults = do 
    upperBound <- getLine
    printBlankLine
    printTranslation (read upperBound :: Int)

printTranslation :: Int -> IO()
printTranslation upperBound = do 
    explainWhatWillHappenWith upperBound
    envokeTranslator [1..upperBound]

explainWhatWillHappenWith :: Int -> IO()
explainWhatWillHappenWith upperBound = do 
    putStr "running FixxBucks agains the list: "
    putStrLn (showRangeWith upperBound)

envokeTranslator :: [Int] -> IO()
envokeTranslator [] = printBlankLine
envokeTranslator (x:xs) = do
    putStrLn (translate x)
    envokeTranslator xs