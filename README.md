# Państwa Miasta - gra sieciowa 
##### Autorzy: Łukasz Kolarz, Adrian Bąk

## 1. Opis projektu
Celem projektu było stworzenie gdy w państwa-miasta. Serwer gry jest w stanie obsługiwać wielu klientów jednocześnie, co turę naliczając każdemu z nich odpowiednią ilość punktów (zgodnie z wartością zdobytą przez nich w danej turze). Po połączeniu klientów, praz podaniu nazw użytkownika (nicków) odbywa się losowanie litery, która zostaje następnie wysłana do graczy. Każdy z nich udziela 5 odpowiedzi, z których każda musi zaczynać się na wylosowana literę [państwo, miasto, roślina, zwierzę, rzecz]. W dalszej kolejności odpowiedzi są wysyłane w postaci wektora do serwera. Po otrzymaniu odpowiedzi od wszystkich graczy serwer łączy je w wektor wektorów oraz wysyła do klienta który połączył się jako pierwszy. Gracz ten dokonuje weryfikacji odpowiedzi, zastępując błędne odpowiedzi wartością 0. Następnie wysyła tak zmodyfikowany wektor wektorów do serwera gdzie odbywa się zliczanie punktów oraz jest tworzony kolejny wektor wektorów, jednak tym razem zawiera on nick oraz ilość punktów każdego gracza. Jest on odsyłany do każdego gracza, aby miał on pogląd na ilość punktów zdobytą przez innych użytkowników w danej rundzie. Po wyświetleniu ilości punktów każdy z graczy może wybrać czy chce powtórzyć partię, jeśli odpowiedź jest twierdząca partia jest kontynuowana. Pakiety między klientem, a serwerem są wysyłany w protokole SCTP, natomiast w celu wysyłania oraz odbierania wektorów wykorzystywany jest moduł „pickle”. Obsługa wielu klientów jest możliwa dzięki wykorzystaniu wątków przy pomocy modułu Threadig.  

## 2. Pliki składające sie na projekt
##### Serwer:
- Server.py – plik zawierający obsługę serwera  
- Game_For_Sever.py – plik zawierający klasę ThreadServer, która zawiera w sobie obsługę wątków  
- var.py – plik zawierający zmienne globalne używane w pozostałych plikach serwera
##### Klient:
- Network.py – plik zawierający obsługę podstawowych funkcji sieciowych klienta takich: tworzenie gniazda, nawiązywanie połączenia, odbiór, wysyłanie itd.  
- Game.py – plik zawierający klasę wraz metodami odpowiedzialną za obsługę fukncji gry  
- Gui.py – plik zawierający Gui oraz obsługę clienta  
- Gui_Test.py – plik służący do uruchomienia Gui  
- Client.py - konsolowa wersja klienta z okrojonymi funkcjami pozwalająca na sprawdzenie jego działania w praktyce
</br>
Dodatkowo w trakcie działania programu tworzone są pliki z logami, odpowiednio server.log oraz client.log   

## 3. Moduły wykorzystane podczas w projekcie
- Tkinter – moduł umożliwiający tworzenie Gui  
- Logging – moduł, który umożliwia korzystanie z logów, gdzie każde odebranie/wysłanie wiadomości, nawiązanie/zerwanie połączenia jest zapisywane  
- Threading – moduł pozwalający na korzystanie z wątków  
- Pickle – moduł pozwalający na wygodne przesyłanie takich danych jak obiekty, wektory czy tablice  
- Time – moduł zawierający funkcje zależne od rzeczywistego czasu. Używany w celu synchronizacji wątków  
- Numpy – moduł zawierający funkcje matematyczne  
- Random – moduł pozwalający na wybieranie losowej liczby spośród zbioru. Używany podczas losowania litery  

## 4. Napotkane problemy
Znaczna ich większość problemów napotkanych podczas tworzenia projektu dotyczyła tematu wątków, a konkretnie ich synchronizacja. Trudnści z utworzeniem zostały rozwiązane dzięki stworzeniu klasy, która reprezentuje wątek oraz zawiera wszystkie jego metody oraz metodologię działania. Bardziej zożony problem - synchronizacji wątków - wynikał z tego, że operują one na wspólnych zmiennych oraz, aby gra miała sens muszą one wspólne wchodzić w poszczególne jej etapy. Udało się go rozwiązać dzięki użyciu pliku var.py zawierającego zmienne globalne, służące do synchronizacji oraz przechowywania wspólnych zasobów każdego wątku.
