### uruchamianie programu

program jest napisany w języku Python. Testowano go na systemie Linux Ubuntu 20.04. 
Z wykorzystaniem: Python 3.8.10
Uruchamiano go poprzez wywolanie: 
# /bin/python3 ~/projects/machine_learning/MDP_RL/mdp.py


program domyślnie wczytuje swiat z pliku znajdujacego sie w katalogu worlds o nazwie world.data. 
Mozliwe jest rowniez podanie sciezki do pliku poprzez opcje -f lub --filename.
Program obsluguje podawanie parametrow -g oraz -e (--gamma, --epsilon ), ktore wczytuja wartosci do odpowiednich parametrow swiata. 


w plikach plot-data-zad1*.data znajduja sie dane z ktorych korzystano do wygenerowania wykresow 
znajdujacych sie w raporcie. Domyslnie dane wynikowe sa zapisywane w pliku:
# results.data
Do wygrenerowania wykresow wykorzystano program gnuplot, ktory nalezy otworzyc w folderze glownym projektu
i wygenerowac wykres poprzez polecenie:
# plot for [n=2:*] 'results.data' u 1:(column(n)) w lines title columnhead(n)

'result.data' mozna zamienic na dowolny plik plot-data* aby wygenerowac wykresy z raportu.


program mdp.py wymaga nastepujacych bibliotek:
numpy 
random       
sys          
copy         
argparse     