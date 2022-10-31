echo "---BACKWARD COMPATIBILITY---"
cat backward | protoc --encode=org.lf.pbtutorial.v2.Account v2.proto | protoc --decode=org.lf.pbtutorial.v1.Account v1.proto

echo "---FORWARD COMPATIBILITY---"
cat forward | protoc --encode=org.lf.pbtutorial.v1.Account v1.proto | protoc --decode=org.lf.pbtutorial.v2.Account v2.proto
