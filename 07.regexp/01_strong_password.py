'''
При регистрации на сайте мы должны придумать пароль для своей учетной записи. Некоторые сайты при этом проверяют
сложность пароля и если он слабый, не дают зарегистрироваться. В этом испытании мы напишем регулярное выражение,
 которое проверяет сложность пароля.

solution
Напишите регулярное выражение, которое проверяет сложность пароля. Считаем, что пароль сильный, если:

Его длина не менее 8 символов
Содержит хотя бы одну цифру
Содержит хотя бы одну заглавную букву
Содержит хотя бы одну строчную букву
Содержит хотя бы один специальный символ
Например, Pas$w0rd – сложный пароль, а Password – слабый, так как не содержит цифр и спецсимволов.

Подсказка:
Опережающий просмотр вперед откатывает каретку обратно к своему началу после успешного сопоставления, исключая из
 результата сопоставления саму последующую часть текста. Это свойство позволяет более гибко определять условия без
 включения всех символов в результат.
'''