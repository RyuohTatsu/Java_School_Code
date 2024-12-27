#include <iostream>
#include <fstream>
#include <cstring>
#include <ctime>
#include <unistd.h>

using namespace std;

void getPassword(char* dest, size_t n) {
    cout << "Enter password: ";
    // Use getpass() to securely read the password without echoing
    char* password = getpass("");
    strncpy(dest, password, n);
    dest[n - 1] = '\0'; // Ensure null-termination
}

int main() {
    char sharedSecret[15];
    getPassword(sharedSecret, sizeof(sharedSecret));

    // Read the shared secret from a secure location (e.g., environment variable)
    ifstream secretFile("sharedsecrets.txt");
    if (!secretFile.is_open()) {
        cerr << "Error: Failed to open shared secrets file." << endl;
        return 1;
    }
    secretFile >> sharedSecret;
    secretFile.close();

    cout << "Enter the shared secret: ";
    char userSecret[15];
    getPassword(userSecret, sizeof(userSecret));

    if (strcmp(sharedSecret, userSecret) == 0) {
        // Authentication successful, proceed with the menu
        // Securely handle sensitive operations here
        cout << "Authentication successful. Welcome to the menu." << endl;
    } else {
        // Authentication failed, log the event
        time_t now = time(nullptr);
        char timestamp[20];
        strftime(timestamp, sizeof(timestamp), "%Y-%m-%d %H:%M:%S", localtime(&now));

        ofstream auditLog("auditlog.txt", ios::app);
        if (auditLog.is_open()) {
            auditLog << "Authentication failure at " << timestamp << endl;
            auditLog.close();
        } else {
            cerr << "Error: Failed to open audit log file." << endl;
        }
        cerr << "Authentication failed. Invalid shared secret." << endl;
    }

    return 0;
}
