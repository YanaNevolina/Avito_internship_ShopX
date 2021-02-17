# Тестовые задания для Авито ShopX.

## Тестовое задание №1:

Автомат принимает накопительные скидочные карты и при своем расчете учитывает количество баллов, по которому начисляет процент скидки: От 0 до 100 баллов - скидка 1% От 100 до 200 баллов - скидка 3 % От 200 до 500 баллов - скидка 5% От 500 баллов - скидка 10%

**Задача:** Составить такой набор тестовых данных для автомата, при котором мы гарантированно будем знать, что в соответствии со своими накопленными баллами покупатель получит верную скидку.

[Решение](TaskTestData.md)


## Тестовое задание №2:

**Задание:** Написать end-to-end автотест, который должен:

 - авторизоваться на avito.ru. Для проверки работоспособности проверьте
   со своей или ново созданной учетной записью;
   
 - выбирать любое доставочное объявление из категории личные вещи;

 - перейти к оформлению заказа с доставкой;
 
 - проверить что поле телефон - пустое.

 [Решение](test_task_shopx/)