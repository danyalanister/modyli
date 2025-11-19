﻿#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

// Проверка, упорядочен ли массив по убыванию
bool isDescending(const int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] < arr[i + 1]) {
            return false;
        }
    }
    return true;
}

// Сортировка выбором по убыванию
void selectionSortDescending(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int maxIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] > arr[maxIndex]) {
                maxIndex = j;
            }
        }
        swap(arr[i], arr[maxIndex]);
    }
}

// Проверка на чётность
bool isEven(int x) {
    return x % 2 == 0;
}

// Пузырьковая сортировка ТОЛЬКО чётных элементов (по возрастанию)
void bubbleSortEven(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (isEven(arr[j]) && isEven(arr[j + 1])) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr[j], arr[j + 1]);
                }
            }
        }
    }
}

int main() {
    setlocale(LC_ALL, "ru");
    const int N = 10;
    int arr[N];


    srand(static_cast<unsigned int>(time(0)));
    for (int i = 0; i < N; i++) {
        arr[i] = rand() % 90 + 10;
    }


    int original[N];
    for (int i = 0; i < N; i++) {
        original[i] = arr[i];
    }

    cout << "=== ЗАДАНИЕ 1: Сортировка по убыванию ===\n";
    cout << "Исходный массив:\n";
    for (int x : arr) cout << x << " ";
    cout << "\n";

    selectionSortDescending(arr, N);

    cout << "Отсортирован по убыванию:\n";
    for (int x : arr) cout << x << " ";
    cout << "\n\n";


    cout << "=== ЗАДАНИЕ 2: Проверка упорядоченности по убыванию ===\n";
    cout << "Проверяем исходный массив:\n";
    for (int x : original) cout << x << " ";
    cout << "\n";

    if (isDescending(original, N)) {
        cout << "Результат: массив УЖЕ упорядочен по убыванию.\n\n";
    }
    else {
        cout << "Результат: массив НЕ упорядочен по убыванию.\n";

        int temp[N];
        for (int i = 0; i < N; i++) temp[i] = original[i];
        selectionSortDescending(temp, N);
        cout << "После сортировки по убыванию:\n";
        for (int x : temp) cout << x << " ";
        cout << "\n\n";
    }


    cout << "=== ЗАДАНИЕ 3: Сортировка чётных элементов (пузырёк) ===\n";
    cout << "Исходный массив:\n";
    for (int x : original) cout << x << " ";
    cout << "\n";

    bubbleSortEven(original, N);

    cout << "После сортировки чётных элементов:\n";
    for (int x : original) cout << x << " ";
    cout << "\n";

    return 0;
}