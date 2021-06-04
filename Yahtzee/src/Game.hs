module Game where


data State = State
    { 
        numPlayers :: Int
        , roundsRemaining :: Int
        , currentRound :: Int
    } deriving Show