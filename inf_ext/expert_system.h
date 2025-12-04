// наша недописанная expert_system
#include <string>
#include <iostream>

struct expert_system {
    struct node {  // узел, который хранит информацию: свинья ли это? и тп
        std::string Text{""};
        node* Y;  // ссылка на ответ
        node* N;  // ссылка на ответ

        node(const std::string& text, node* yes = nullptr, node* no = nullptr) {
            Text = text;
            Y = yes;
            N = no;
        }  // должны сразу передать суть
        
        ~node() {
            delete Y;
            delete N;
        }  // поели - убираем со стола
    };

    node* Root;

    expert_system() {}  // констуктор по умолчанию

    expert_system(const std::string& text = "Pig"): Root(new node(text)) {}

    ~expert_system() {
        delete Root;
    }

    void Session() {
        node** T = &Root;
        std::string Question, Definition, Answer;
        while ((*T)->Text != "") {
            std::cout << ((*T)->Text) << "?\n";  // задаем вопрос
            std::cin >> Answer;  // получаем ответ на вопрос
            if (Answer == "Y" || Answer == "y" || Answer == "Yes" || Answer == "yes") {
                if ((*T)->Y == nullptr) {  // если нет ветки для ответа, то мы дошли до предела, поздравим пользователя
                    std::cout << "Congratulations!\n";
                    return;
                } else { // если у нас уже есть ветка для ответа, то просто пойдем по ней дальше
                    T = &(*T)->Y;
                }
            } else {
                if ((*T)->N != nullptr) {  // если у нас уже есть ветка для ответа, то просто пойдем по ней дальше
                    T = &(*T)->N;

                    // return;  // ?? х
                } else {
                    std::string NewQ, NewT;
                    std:: cout << "New Question";
                    std::getline(std:: cin, NewQ) ;
                    std::cout << "New Answer";
                    std::getline(std:: cin, NewA);
                    *T = new node(NewQ, new node(NewA), *T) ;
                }

            }

            
            
        }
        
    }
};

void exper_system::Session() {
    
}
