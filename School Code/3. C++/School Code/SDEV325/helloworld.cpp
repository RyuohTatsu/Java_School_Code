#include <iostream>
#include <ctime>

int main()
{
    // Get current date and time
    std::time_t now = std::time(nullptr);
    std::tm *local_time = std::localtime(&now);

    // Format date and time
    char time_buffer[80];
    std::strftime(time_buffer, sizeof(time_buffer), "%Y-%m-%d %H:%M:%S", local_time);

    // Print formatted message
    std::cout << "Hello, World!" << std::endl;
    std::cout << time_buffer << std::endl;
    std::cout << "Brian Walters (Developer)" << std::endl;
    std::cout << "Greetings, I am looking forward to SDEV 325." << std::endl;
    std::cout << "I have never played around with C++ yet but I am excited to learn." << std::endl;

    return 0;
}