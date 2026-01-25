#include "ConfigManager.h" 
#include "utils.h"

#include <iostream>
#include <string>

class pb_controller {
    ConfigManager* cfg;
public:
    pb_controller(ConfigManager* config) : cfg(config) {}
    
    void play_file(const std::string& file) {
        std::string cmdline;
        std::string player = cfg->get_configvalue("player");
        if (player.empty()) {
            std::cerr << "Player not configured." << std::endl;
            return;
        }
        cmdline += player + " '" + utils::replace_all(file, "'", "%27") + "'";
        utils::run_interactively(cmdline, "pb_controller::play_file");
    }
};

int main() {
    ConfigManager config; // Assuming ConfigManager has a default constructor
    pb_controller controller(&config);
    
	// Ask the user for the file name
	std::string file_name;
	std::cout << "Enter the file name: ";
	std::cin >> file_name;
    controller.play_file(file_name);
    return 0;
}
