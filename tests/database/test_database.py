import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_users_address_by_name('Stepan')

    assert user[0][0] == 'Stepana Bandery str, 2'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '2055'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_by_id():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печево', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30
    try:
        db.insert_product(5, 'молоко', 'рідке', 'сорок')
        # неправильний тип даних для кількості
    except ValueError as e:
        print(f"Error: {e}")

    try:
        db.insert_product(6, 123, 'рідке', 40)
        # неправильний тип даних для name
    except ValueError as e:
        print(f"Error: {e}")


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'test', 'mark', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("P", orders)

    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'
