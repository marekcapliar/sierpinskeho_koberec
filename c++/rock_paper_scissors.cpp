#include <iostream>
#include <ctime>

std::string pc_guess(){
    srand(std::time(NULL));
    int choice = rand() % 3;
    switch (choice){
    case 0:
        return "rock";
        break;
    case 1:
        return "paper";
        break;
    case 2:
        return "scissors";
        break;
    default:
        std::cout << "error in pc_guess";
        break;
    }
    return "0";
}

std::string player_guess(){
    std::string player;
    std::cout << "guess rock, paper or scissors: ";
    std::cin >> player;
    if (player == "rock" || player == "paper" || player == "scissors"){
        return player;
    }
    else{
        std::cout << "invalid guess\n";
        player = player_guess();
    }
    return player;
}

std::string winner(std::string player, std::string pc){
    if (player == pc){
        return "tie";
    }
    else if (player == "rock"){
        if (pc == "paper"){
            return "Computer won";
        }
        else if (pc == "scissors"){
            return "You won";
        }
    }
    else if (player == "paper"){
        if (pc == "scissors"){
            return "Computer won";
        }
        else if (pc == "rock"){
            return "You won";
        }
    }
    else if (player == "scissors"){
        if (pc == "rock"){
            return "Computer won";
        }
        else if (pc == "paper"){
            return "You won";
        }
    }
    return "0";
}

int main(){
    std::string win;
    int player_score = 0;
    int pc_score = 0;
    while (player_score < 3 && pc_score < 3)
    {
        win = winner(player_guess(), pc_guess());
        if (win == "You won"){
            player_score++;
        }
        else if (win == "Computer won"){
            pc_score++;
        }
        std::cout << win << '\n'
                  << "player score: " << player_score 
                  << "\npc score: " << pc_score << "\n\n";
    }
    
    if (player_score == 3){
        std::cout << "CONGRATULATIONS\nYOU WON\n";
    }
    else if (pc_score == 3){
        std::cout << "YOU LOSE\n";
    }
    
    return 0;
}
