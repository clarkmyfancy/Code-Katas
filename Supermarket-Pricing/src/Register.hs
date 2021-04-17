module Register where

import ConcreteRegister

scanNewItem :: Double -> Double -> Double
scanNewItem previousCartTotal price = do
    ConcreteRegister.scanNewItem previousCartTotal price

