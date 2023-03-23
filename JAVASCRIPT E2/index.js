// Задание 1 Дан массив, вывести число нулей, четных и нечетных цифр. Учесть, что на входе не только цифры
function determinEven(array){
    let zero = 0;
    let even = 0;
    let notEven = 0;
    for(number of array){
        if(Number.isInteger(number)){
            if(number == 0){
                zero += 1
            }
            else if(number % 2 === 0){
                even += 1
            }
            else if(number % 2 !== 0){
                notEven += 1
            };
        }
        else{
            console.log('Не число', number)
        };
    };
    console.log(`
    Нулей: ${zero};
    Четных: ${even};
    Нечетных: ${notEven}
    `);
};

console.log('Работает функция 1, массив [1,2,3,4,5,6, null, 0]')
determinEven([1,2,3,4,5,6, null, 0])

// Задание 2. Дано число до 1000, определеить, простое или нет.
function determinPrime(number){
    if(number > 1000){
        console.log('Нельзя вводить число больше 1000 по заданию');
    }
    else if(number == 0 | number == 1){
        console.log('Ноль и единицу не относят ни к простым ни к составным');
    }
    else{
        for(let i = 2; i < number; i++){
            if (number % i == 0){
                console.log('Это число составное')
                return false
            };
        };
        console.log('Это число простое');
        return true
    };
};


console.log('Работает функция 2. На входе число 100');
determinPrime(100)

// Задание 3. Функция, которая принимает число, как аргумент, и возвращает функцию, которая тоже принимает число и возвращает сумму
function sumTwo(first, second){
    function innerSum(numberOne, numberTwo){
        console.log(numberOne + numberTwo);
        return numberOne + numberTwo
    }
    return innerSum(first, second)
};

console.log('Работает функция 3. Ниже сумма чисел 1 и 2')
sumTwo(1, 2)





// Задание 5. Стрелочная функция возведения в степень

const toPowerOf = (number, power) => {
    let result = 1
    for(let i = 0; i < power; i++){
        result *= number
    }
    console.log(result)
};

console.log('Работает функция 5. Возведение 3 в 10 степень')
toPowerOf(3, 10)
console.log('На этом все, спасибо за внимание')


// задание 4. Вывод чисел через определенный промежуток времени

function showNumbers(start, end){
    let interval = setInterval(() => {
        console.log(start);
        start ++
        if(start == end + 1){
            clearInterval(interval)
        };
    }, 1000)
    
};

console.log('Работает функция 4. Печать чисел от 1 до 10')
showNumbers(1,10)