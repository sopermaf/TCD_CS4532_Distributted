import Network
import System.Environment
import System.IO
import Network.HTTP
import Data.List.Split

main :: IO ()
main = do
    [port, message] <- getArgs
    tcpHandler <- connectTo "localhost" $ PortNumber $ toEnum $ read port
    hSetBuffering tcpHandler  LineBuffering
    hPutStr tcpHandler $ buildHTTPMessage message
    hGetContents tcpHandler >>= putStr . parseResponse 

buildHTTPMessage :: String -> String
buildHTTPMessage msg = "GET /echo-server.php?message=" ++ msg ++ " HTTP/1.1\r\n\r\n"

parseResponse :: String -> String
parseResponse httpMsg = "Response:\n" ++ last (splitOn "\r\n\r\n" httpMsg) ++ "\n"
