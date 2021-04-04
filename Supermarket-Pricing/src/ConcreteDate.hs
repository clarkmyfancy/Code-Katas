module ConcreteDate where

import Data.Time

date :: IO()
date = print =<< getCurrentTime