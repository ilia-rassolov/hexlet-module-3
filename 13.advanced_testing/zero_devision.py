def function_with_exception(divider):
    return int(11/divider)


# print(function_with_exception(0))



# def test_exception():
#     try:
#         function_with_exception(1)
#     except Exception as e:
#         assert e

#
import pytest

# def test_exception():
#     with pytest.raises(KeyError):
#         function_with_exception(0)


def test_exception():
    # Добавляем: as e. Здесь e – произвольное имя переменной, содержащей исключение
    with pytest.raises(ZeroDivisionError) as e:
        function_with_exception(0)

    # assert str(e.value) == 'expected message from exception'