
# Аналіз продуктивності алгоритмів пошуку підрядка / String Search Algorithms Benchmark

Цей проєкт порівнює ефективність трьох класичних алгоритмів пошуку підрядка в тексті:

- **Boyer-Moore**
- **Knuth-Morris-Pratt (KMP)**
- **Rabin-Karp**

## 📂 Вхідні дані / Input

- `text1.txt` — перший текстовий файл
- `text2.txt` — другий текстовий файл
- Пошукові шаблони:
  - `pattern_exist1 = "return middleIndex"`
  - `pattern_exist2 = "Робинсон Я., Вебер Д., Эифрем Э"`
  - `pattern_no_exist = "що краще js чи python?"`

---

### 🔍 Boyer-Moore
- Найшвидший алгоритм у більшості випадків, особливо коли шаблон **не знайдено**.
- Середній час: **~0.012 сек**, навіть на великих текстах.
- Підходить для **великих текстів** і **рідких входжень**.

### 🔍 KMP (Knuth-Morris-Pratt)
- Гарантує **лінійну складність**, але на практиці працює **повільніше за Boyer-Moore**.
- Час на великому тексті може перевищувати **0.1 сек**.
- Краще підходить для **частих входжень шаблону**.

### 🔍 Rabin-Karp
- Найповільніший із трьох, особливо коли шаблон **не знайдено**.
- Найгірша продуктивність при негативному результаті — до **0.22 сек**.
- Може бути корисним лише при **пошуку багатьох шаблонів одночасно**.

---

## 📊 Conclusions in English

### 🔍 Boyer-Moore
- The **fastest algorithm** overall, especially when the pattern is **not found**.
- Average runtime: **~0.012 seconds**, even on large texts.
- Best choice for **large texts** and **rare matches**.

### 🔍 KMP (Knuth-Morris-Pratt)
- Guarantees **linear time complexity**, but is **slower in practice** than Boyer-Moore.
- Runtime can exceed **0.1 seconds** on larger texts.
- Suitable for **frequent pattern matches**.

### 🔍 Rabin-Karp
- The **slowest algorithm** in this benchmark.
- Worst performance when the pattern is not found — up to **0.22 seconds**.
- Only advisable for **multi-pattern search scenarios**.

---

## ⏱ Приклад результатів / Sample Results

| Algorithm         | Text     | Pattern      | Result Index | Time (100 runs) |
|------------------|----------|--------------|---------------|-----------------|
| Boyer-Moore      | text1    | exist1       | 4448          | 0.0059 s        |
| Boyer-Moore      | text1    | not_exist    | -1            | 0.0121 s        |
| KMP              | text2    | exist2       | 17011         | 0.0980 s        |
| KMP              | text2    | not_exist    | -1            | 0.1033 s        |
| Rabin-Karp       | text2    | exist2       | 17011         | 0.2140 s        |
| Rabin-Karp       | text2    | not_exist    | -1            | 0.2245 s        |

---

## 📁 Структура проєкту / Project Structure

```
task3/
│
├── main.py                # Сценарій для запуску тестів
├── kmp.py                 # Реалізація KMP
├── boyer.py               # Реалізація Boyer-Moore
├── rabin.py               # Реалізація Rabin-Karp
├── text1.txt              # Текстовий файл 1
├── text2.txt              # Текстовий файл 2
└── README.md              # Документація (цей файл)
```

---

## ✅ Висновок / Final Verdict

Для практичного застосування:

- 🥇 **Boyer-Moore** — кращий вибір у 80% випадків.
- 🥈 **KMP** — якщо потрібно гарантоване O(n+m).
- 🥉 **Rabin-Karp** — підходить для особливих випадків (наприклад, багато шаблонів).
