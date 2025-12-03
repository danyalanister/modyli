#include <iostream>
using namespace std;
#include <vector>
//1 Рекурсивный алгоритм НОД 
int gcd(int a, int b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

int main() {
    setlocale(LC_ALL, "ru");
    int a, b;
    cout << "Введите два числа: ";
    cin >> a >> b;
    cout << "НОД(" << a << ", " << b << ") = " << gcd(a, b) << endl;
    return 0;
}

//2 Рекурсивное вычисление числа Фибоначчи
int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    setlocale(LC_ALL, "ru");
    int n;
    cout << "Введите номер числа Фибоначчи: ";
    cin >> n;
    cout << "Число Фибоначчи №" << n << " = " << fibonacci(n) << endl;
    return 0;
}

//3 Рекурсивная функция для переворота числа
int reverseNumber(int num, int rev = 0) {
    if (num == 0) {
        return rev;
    }
    return reverseNumber(num / 10, rev * 10 + num % 10);
}

int main() {
    setlocale(LC_ALL, "ru");
    int num;
    cout << "Введите число: ";
    cin >> num;
    cout << "Перевернутое число: " << reverseNumber(num) << endl;
    return 0;
}

//4 Разбиение числа n на m слагаемых
void printPartition(vector<int>& part) {
    for (int i = 0; i < part.size(); i++) {
        cout << part[i] << " ";
    }
    cout << endl;
}

void partition(int n, int m, vector<int>& part, int last = 1) {
    if (m == 1) {
        if (n >= last) {
            part.push_back(n);
            printPartition(part);
            part.pop_back();
        }
        return;
    }

    for (int i = last; i <= n - m + 1; i++) {
        part.push_back(i);
        partition(n - i, m - 1, part, i);
        part.pop_back();
    }
}

int main() {
    setlocale(LC_ALL, "ru");
    int n, m;
    cout << "Введите n и m: ";
    cin >> n >> m;
    vector<int> part;
    partition(n, m, part);
    return 0;
}

//5 Двойной факториал n!!
int doubleFactorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * doubleFactorial(n - 2);
}

int main() {
    setlocale(LC_ALL, "ru");
    int n;
    cout << "Введите n: ";
    cin >> n;
    cout << n << "!! = " << doubleFactorial(n) << endl;
    return 0;
}

//6 Количество единиц в двоичном представлении числа
int countOnes(int n) {
    if (n == 0) {
        return 0;
    }
    return (n % 2) + countOnes(n / 2);
}

int main() {
    setlocale(LC_ALL, "ru");
    int n;
    cout << "Введите число: ";
    cin >> n;
    cout << "Количество единиц в двоичном представлении: " << countOnes(n) << endl;
    return 0;
}

//7 Сложение двух чисел через прибавление единицы
int add(int a, int b) {
    if (b == 0) {
        return a;
    }
    return add(a + 1, b - 1);
}

int main() {
    setlocale(LC_ALL, "ru");
    int a, b;
    cout << "Введите два числа: ";
    cin >> a >> b;
    cout << a << " + " << b << " = " << add(a, b) << endl;
    return 0;
}

