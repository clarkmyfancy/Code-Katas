module ConcreteRegister where

scanNewItem :: Double -> Double -> Double
scanNewItem previousCartTotal price = do 
    previousCartTotal + price