#include <iostream>
#include <boost/asio.hpp>
#include <string>

int main(int argc, char* argv[])
{
    if(argc < 3) {
        std::cout << "Error: Please run with the fallow arguments" << std::endl;
	std::cout << "./client ip porta message" << std::endl;
        exit(1);
    }    
    
    boost::asio::io_service io_service;
    boost::asio::ip::tcp::socket socket(io_service);
    boost::asio::ip::tcp::resolver resolver(io_service);
    boost::asio::connect(socket, resolver.resolve({argv[1], argv[2]}));
    
    std::size_t _size = 1024;
    std::string msg = argv[3]; 
    boost::asio::write(socket, boost::asio::buffer(msg.c_str(), _size));
    return 0;
}

//http://www.boost.org/doc/libs/1_55_0/doc/html/boost_asio/examples/cpp11_examples.html
