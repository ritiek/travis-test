CXX=/home/ritiek/Downloads/Amazon-Kindle-Cross-Toolchain/arm-kindle-linux-gnueabi/bin/arm-kindle-linux-gnueabi-g++

$CXX -g -Wall -Werror -Wno-unknown-pragmas  -std=c++14 -c -o src/main.o src/main.cpp -MMD -MT src/main.o -MF src/main.d
$CXX -g -Wall -Werror -Wno-unknown-pragmas  -std=c++14 -c -o src/daemon.o src/daemon.cpp -MMD -MT src/daemon.o -MF src/daemon.d
$CXX -g -Wall -Werror -Wno-unknown-pragmas  -std=c++14 -c -o src/writer.o src/writer.cpp -MMD -MT src/writer.o -MF src/writer.d
$CXX -g -Wall -Werror -Wno-unknown-pragmas  -std=c++14 -c -o src/reader.o src/reader.cpp -MMD -MT src/reader.o -MF src/reader.d
$CXX -g -Wall -Werror -Wno-unknown-pragmas  -std=c++14 -c -o src/socket.o src/socket.cpp -MMD -MT src/socket.o -MF src/socket.d
$CXX -g  -o netevent src/main.o src/daemon.o src/writer.o src/reader.o src/socket.o
